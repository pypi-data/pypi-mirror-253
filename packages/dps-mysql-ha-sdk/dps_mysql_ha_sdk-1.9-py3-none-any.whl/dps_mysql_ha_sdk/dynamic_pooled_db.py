import os
import threading
import time
import logging


from dbutils.pooled_db import PooledDB

from dps_mysql_ha_sdk.db.db_utils import get_db_properties
from dps_mysql_ha_sdk.utils.check_utils import check_data_source, calculate_initial_delay_6, calculate_initial_delay_22, \
    test_mysql_credentials
from dps_mysql_ha_sdk.utils.log_utils import to_serializable


class DynamicPooledDB(PooledDB):
    def __init__(self, *args, **kwargs):
        self.password = None
        self.user = None
        self.database = None
        self.port = None
        self.host = None
        self.svcCode = None
        self.platDsnKey = None
        self.platUrlMain = None
        self._mincached = kwargs['mincached']
        self.platUrlMain = kwargs['platUrlMain']
        self.platUrl = kwargs['platUrl']
        self.platDsnKey = kwargs['platDsnKey']
        self.svcCode = kwargs['svcCode']
        self.get_db_info(**kwargs)

        kwargs.pop('platUrlMain', None)
        kwargs.pop('platUrl', None)
        kwargs.pop('platDsnKey', None)
        kwargs.pop('svcCode', None)
        kwargs['host'] = self.host
        kwargs['port'] = self.port
        kwargs['database'] = self.database
        kwargs['user'] = self.user
        kwargs['password'] = self.password
        test_mysql_credentials(self.host, self.port, self.user, self.password)
        super().__init__(*args, **kwargs)
        # 开启定时检查任务
        check_thread = threading.Thread(target=self._init_check_task)
        check_thread.daemon = True  # 设置为守护线程，程序退出时自动退出
        check_thread.start()
        # 开启切换数据源任务
        update_thread = threading.Thread(target=self._init_update_task)
        update_thread.daemon = True  # 设置为守护线程，程序退出时自动退出
        update_thread.start()

    def get_db_info(self, **kwargs):
        """
        获取数据库连接信息，账号密码改变则更新对象的属性。

        Args:
        - kwargs: 传递的关键字参数，用于获取数据库连接信息的配置。

        Returns:
        - 无返回值。
        """
        if 'platUrlMain' in kwargs and kwargs['platUrlMain'] is not None:
            url = kwargs['platUrlMain']
        else:
            url = self.platUrl
        platkey = os.environ.get("PLATKEY", None)
        profile = os.environ.get("PROFILE", None)
        if platkey is None:
            logging.error("Please configure environment variable PLATKEY!")
        if profile is None:
            logging.error("Please configure environment variable PROFILE!")
        user_agent = self.svcCode
        databases = None
        logging.warning(
            to_serializable("WARNING", "dynamic_pooled_db",
                            "url:" + url + " platkey:" + platkey + " svcCode:" + self.svcCode
                            + " profile:" + profile + " user_agent:" + user_agent))
        try:
            databases = get_db_properties(self.platUrlMain, platkey, self.svcCode, profile, user_agent)
        except Exception as e:
            logging.error(f"Error while getting database properties: {e}")
            logging.error(
                to_serializable("ERROR", "dynamic_pooled_db",
                                "Exception in calling the data source platform to obtain MYSQL database parameters "
                                "interface! url:" + url))

        # 设置对象的属性
        if databases is not None:
            self.host = databases.get(self.platDsnKey).get("ip")
            self.port = databases.get(self.platDsnKey).get("port")
            self.database = databases.get(self.platDsnKey).get("sid")
            logging.warning(
                to_serializable("WARNING", "dynamic_pooled_db",
                                "host:" + self.host + " port:" + str(self.port) + " sid:" + self.database
                                + " username:" + databases.get(self.platDsnKey).get("username") + " password:"
                                + databases.get(self.platDsnKey).get("password")))
            if self.user is None or self.password is None:
                self.user = databases.get(self.platDsnKey).get("username")
                self.password = databases.get(self.platDsnKey).get("password")
            elif check_data_source(databases.get(self.platDsnKey).get("username"),
                                   databases.get(self.platDsnKey).get("password"),
                                   self.user, self.password):
                # 账号密码发生变化暂时将账号密码保存在内存中
                logging.warning(
                    to_serializable("WARNING", "dynamic_pooled_db",
                                    "Custom resource labels " + self.platDsnKey + ", The account password has "
                                                                                  "changed. Please temporarily save "
                                                                                  "the account password in memory!"
                                    + self.user + "->" + databases.get(self.platDsnKey).get("username")))
                self.user = databases.get(self.platDsnKey).get("username")
                self.password = databases.get(self.platDsnKey).get("password")
            else:
                logging.warning(
                    to_serializable("WARNING", "dynamic_pooled_db",
                                    "Custom resource labels " + self.platDsnKey + ", Account password remains "
                                                                                  "unchanged! "))

    def connection(self, shareable=True):
        """
        获取数据库连接，可选择共享已存在的连接。

        Args:
        - shareable (bool): 是否可共享已存在的连接，默认为 True。

        Returns:
        - con: 获取到的数据库连接。
        """
        with self._lock:
            # 调用父类的 connection 方法
            con = super(DynamicPooledDB, self).connection(shareable)
            if not hasattr(con, 'userName') or con.userName is None:
                con._con.userName = self._kwargs['user']
                return con
            else:
                if con._con.userName != self._kwargs['user']:
                    try:
                        con._con.close()
                        self._connections -= 1
                        if len(self._idle_cache) == 0:
                            # 创建新的连接保存到 _idle_cache 中
                            self._idle_cache.extend([self.dedicated_connection() for i in range(self._mincached)])
                        return self.connection()
                    except Exception:
                        pass
            return con

    def _init_check_task(self):
        """
        初始化检查账号和密码变更的定时任务。

        在初始化时，通过计算初始延迟时间（由 calculate_initial_delay_6 函数提供）启动定时任务。同时，记录警告日志，说明启动了检查账号和密码变更的任务，并指定了初始延迟时间。

        Returns:
        - 无返回值。
        """
        # 计算初始延迟时间
        initial_delay = calculate_initial_delay_6()
        # 记录警告日志，说明启动了检查账号和密码变更的任务，指定初始延迟时间
        logging.warning(
            to_serializable("WARNING", "dynamic_pooled_db",
                            "Start checking account and password changes task in "
                            + os.environ.get("check.init") + " seconds" if os.environ.get("check.init") else
                            "Start checking account and password changes task in " + str(
                                initial_delay) + " seconds"))
        # 通过 sleep 函数等待初始延迟时间
        time.sleep(int(os.environ.get("check.init")) if os.environ.get("check.init") else initial_delay)

        # 启动定时任务
        self._start_check_task()

    def _start_check_task(self):
        """
        启动定时检查任务，定期执行检查数据库连接状态的逻辑。

        定时任务的间隔时间由环境变量 "check.period" 指定，如果未设置则默认为12小时。

        Returns:
        - 无返回值。
        """
        # 创建一个 Timer 对象，指定定时任务的函数和间隔时间
        timer = threading.Timer(int(os.environ.get("check.period")) if os.environ.get("check.period") else 12 * 60 * 60,
                                self._check_task)

        # 设置为守护线程，程序退出时自动退出
        timer.daemon = True

        # 启动定时任务
        timer.start()

    def _check_task(self):
        """
        定时任务逻辑，用于检查数据源平台连接信息是否有更新。

        在任务执行期间，调用 get_db_info 方法检查数据库连接状态，然后重新启动下一个定时任务。

        Returns:
        - 无返回值。
        """
        logging.warning(
            to_serializable("WARNING", "dynamic_pooled_db",
                            "Custom resource label " + self.platDsnKey + " check if the account password has been "
                                                                         "changed"))
        # 检查数据源平台连接信息是否有更新
        self.get_db_info()

        # 重新启动下一个定时任务
        self._start_check_task()

    def _init_update_task(self):
        """
        初始化更新账号和密码的定时任务。

        在初始化时，通过计算初始延迟时间（由 calculate_initial_delay_22 函数提供）启动定时任务。同时，记录警告日志，说明启动了更新账号和密码的任务，并指定了初始延迟时间。

        Returns:
        - 无返回值。
        """
        # 计算初始延迟时间
        initial_delay = calculate_initial_delay_22()
        # 记录警告日志，说明启动了更新账号和密码的任务，指定初始延迟时间
        logging.warning(
            to_serializable("WARNING", "dynamic_pooled_db",
                            "Start the update account and password task in "
                            + os.environ.get("update.init") + " seconds" if os.environ.get("update.init") else
                            "Start the update account and password task in " + str(
                                initial_delay) + " seconds"))
        # 通过 sleep 函数等待初始延迟时间
        time.sleep(int(os.environ.get("update.init")) if os.environ.get("update.init") else initial_delay)

        # 启动定时任务
        self._start_update_task()

    def _start_update_task(self):
        """
        启动定时任务，定期执行更新数据源任务。

        定时任务的间隔时间由环境变量 "update.period" 指定，如果未设置则默认为24小时。

        Returns:
        - 无返回值。
        """
        # 创建一个 Timer 对象，指定定时任务的函数和间隔时间
        timer = threading.Timer(
            int(os.environ.get("update.period")) if os.environ.get("update.period") else 24 * 60 * 60,
            self._update_task)

        # 设置为守护线程，程序退出时自动退出
        timer.daemon = True

        # 启动定时任务
        timer.start()

    def _update_task(self):
        """
        更新数据源任务，用于检测并更新数据库连接凭据。

        在任务执行期间，会记录警告日志并检查数据库连接凭据的有效性，如果凭据有效则更新数据源参数，并重新启动定时任务。

        Returns:
        - 无返回值。
        """
        # 记录警告日志，说明执行了更新数据源任务
        logging.warning(
            to_serializable("WARNING", "dynamic_pooled_db",
                            "Custom resource label " + self.platDsnKey + " executes update data source task"))
        if check_data_source(self.user, self.password, self._kwargs["user"], self._kwargs["password"]):
            # 检查数据库连接凭据的有效性，连续检查3次
            if test_mysql_credentials(self.host, self.port, self.user, self.password) \
                    and test_mysql_credentials(self.host, self.port, self.user, self.password) \
                    and test_mysql_credentials(self.host, self.port, self.user, self.password):
                # 如果凭据有效，更新数据源参数
                self._kwargs["user"] = self.user
                self._kwargs["password"] = self.password
                logging.warning("Custom resource label " + self.platDsnKey + " Switching successful! " + "userName:"
                                + self._kwargs["user"])
            else:
                logging.error(
                    to_serializable("ERROR", "dynamic_pooled_db",
                                    "The backup account password is abnormal, and the data source will not be switched!"))
        # 重新启动下一个定时任务
        self._start_update_task()
