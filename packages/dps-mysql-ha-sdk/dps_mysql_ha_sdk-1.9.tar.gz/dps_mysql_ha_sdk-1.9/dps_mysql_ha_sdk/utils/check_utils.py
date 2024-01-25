import hashlib
import logging
import random
from datetime import datetime, timedelta
from dps_mysql_ha_sdk.utils.log_utils import to_serializable

import pymysql


def check_data_source(new_username, new_password, use_username, use_password):
    """
    检查两组用户名和密码的 MD5 散列是否不相等

    Parameters:
    - new_username: 新的用户名
    - new_password: 新的密码
    - use_username: 已使用的用户名
    - use_password: 已使用的密码

    Returns:
    - 如果新用户名和密码的 MD5 散列不等于已使用的用户名和密码的 MD5 散列，返回 True，否则返回 False
    """
    # 比较用户名的 MD5 散列
    use_username_md5 = calculate_md5(use_username)
    new_username_md5 = calculate_md5(new_username)

    # 计算密码的 MD5 散列
    use_password_md5 = calculate_md5(use_password)
    new_password_md5 = calculate_md5(new_password)

    return use_username_md5 != new_username_md5 or use_password_md5 != new_password_md5


def calculate_md5(data):
    """
    计算字符串的 MD5 散列值。

    Parameters:
    - data: 要计算散列值的字符串。

    Returns:
    - 计算得到的 MD5 散列值的十六进制表示。
    """
    # 创建 MD5 对象
    md5 = hashlib.md5()

    # 将字符串编码为字节并更新 MD5 对象
    md5.update(data.encode('utf-8'))

    # 返回计算得到的 MD5 散列值的十六进制表示
    return md5.hexdigest()


def calculate_initial_delay_6():
    now = datetime.now().time()
    target_time = datetime.strptime("06:00", "%H:%M").time()

    if now < target_time:
        # 如果当前时间在6:00之前，返回当前时间到6:00的时间差
        time_difference = datetime.combine(datetime.today(), target_time) - datetime.combine(datetime.today(), now)
        return time_difference.total_seconds() + random.randint(0, 16 * 60 * 60)
    else:
        # 如果当前时间在6:00之后，返回当前时间到明天6:00的时间差
        tomorrow_target_time = datetime.combine(datetime.today() + timedelta(days=1), target_time)
        time_difference = tomorrow_target_time - datetime.combine(datetime.today(), now)
        return time_difference.total_seconds() + random.randint(0, 16 * 60 * 60)


def calculate_initial_delay_22():
    now = datetime.now().time()
    target_time = datetime.strptime("22:00", "%H:%M").time()

    # 获取今天的日期
    current_date = datetime.today().date()

    # 获取今天的22:00时间
    today_target_datetime = datetime.combine(current_date, target_time)

    # 如果当前时间在22:00之前，返回当前时间到22:00的时间差
    if now < target_time:
        time_difference = today_target_datetime - datetime.combine(current_date, now)
        return time_difference.total_seconds() + random.randint(0, 8 * 60 * 60)
    else:
        # 如果当前时间在22:00之后，返回当前时间到明天22:00的时间差
        tomorrow_target_datetime = today_target_datetime + timedelta(days=1)
        time_difference = tomorrow_target_datetime - datetime.combine(current_date, now)
        return time_difference.total_seconds() + random.randint(0, 8 * 60 * 60)


def test_mysql_credentials(host, port, username, password):
    """
    测试 MySQL 数据库的连接凭据是否有效。

    Parameters:
    - host: MySQL 主机名或 IP 地址。
    - port: MySQL 端口号。
    - username: MySQL 用户名。
    - password: MySQL 密码。

    Returns:
    - 如果连接凭据有效，返回 True；否则返回 False。
    """
    try:
        # 尝试建立数据库连接，设置连接超时时间为5秒
        connection = pymysql.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            connect_timeout=5
        )
        connection.close()
        # 如果连接成功，表示账号密码有效
        return True

    except Exception as e:
        # 捕捉异常，记录错误日志，并返回账号密码无效
        logging.error(f"Invalid MySQL credentials. Error: {e}")
        logging.error("Cannot connect to database!" + " host:" + host + " port:" + str(port) + " username:" + username
                      + " password:" + password)
        return False

