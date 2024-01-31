# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
本文件实现了sdk日志的功能

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2023/07/24
"""
import os
import logging
from aistudio_sdk import config

logger = logging.getLogger("aistudio_sdk")
logger.setLevel(logging.INFO)

# 日志输出格式
formatter = logging.Formatter(fmt='%(message)s')

# 控制台输出
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

__all__ = [
    "info",
    "debug",
    "warn",
    "error",
]

def set_log_level(f):
    """设置日志级别: info / debug"""
    def wrapper(*args, **kwargs):
        """log wrapper"""
        level = os.environ.get("AISTUDIO_LOG", config.DEFAULT_LOG_LEVEL)
        if level == "info":
            logger.setLevel(logging.INFO)
        else:
            logger.setLevel(logging.DEBUG)
        
        return f(*args, **kwargs)
    return wrapper


@set_log_level
def info(msg):
    """log evel: INFO"""
    logger.log(logging.INFO, msg)

@set_log_level
def debug(msg):
    """log evel: DEBUG"""
    logger.log(logging.DEBUG, msg)

@set_log_level
def warn(msg):
    """log evel: WARN"""
    logger.log(logging.WARN, msg)

@set_log_level
def error(msg):
    """log evel: ERROR"""
    logger.log(logging.ERROR, msg)
