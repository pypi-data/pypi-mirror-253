import os
import time
from datetime import datetime


def date_format(timestamp):
    """
    将时间戳转换为指定格式的日期字符串。

    Parameters:
    - timestamp: 待转换的时间戳，单位是毫秒。

    Returns:
    - 格式化后的日期字符串，格式为 "%Y-%m-%d %H:%M:%S"。
    """
    # 将毫秒级时间戳转换为秒级时间戳，并生成对应的日期对象
    date_obj = datetime.fromtimestamp(timestamp / 1000.0)

    # 使用 strftime 函数将日期对象格式化为字符串
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")


def to_serializable(level, logger, msg):
    """
    将日志信息转换为可序列化的 JSON 字符串。

    Parameters:
    - level: 日志级别。
    - logger: 日志记录器的名称。
    - msg: 日志消息。

    Returns:
    - 包含日志信息的 JSON 字符串。
    """
    # 构建日志事件的字典表示
    logstash_event = {
        "app_name": get_env_or_property("APPNAME"),  # 获取环境变量或属性中的应用程序名称
        "level": level,  # 设置日志级别
        "log_time": date_format(time.time() * 1000),  # 获取当前时间并格式化为指定格式
        "logger": logger,  # 设置日志记录器的名称
        "msg": msg  # 设置日志消息
    }

    # 调用 map_to_json_string 将字典转换为 JSON 字符串
    return map_to_json_string(logstash_event)


def get_env_or_property(key):
    """
    获取环境变量或属性的值。

    Parameters:
    - key: 环境变量或属性的键。

    Returns:
    - 如果存在对应的环境变量或属性，则返回其值；否则返回 None。
    """
    # 尝试获取环境变量的值，如果不存在则尝试获取属性的值，如果都不存在则返回 None
    return os.environ.get(key) or os.getenv(key) or None


def map_to_json_string(input_map):
    json_string = "{"
    first = True

    for key, value in input_map.items():
        if not first:
            json_string += ","
        json_string += f'"{key}":'

        if isinstance(value, str):
            json_string += f'"{value}"'
        else:
            json_string += str(value)

        first = False

    json_string += "}"
    return json_string
