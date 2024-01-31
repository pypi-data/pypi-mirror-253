# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2023/07/24
"""
import os
from aistudio_sdk import config
from aistudio_sdk.version import VERSION
from aistudio_sdk.model_resources import chat, embed
from aistudio_sdk import hub

log_level = os.environ.get("AISTUDIO_LOG", config.DEFAULT_LOG_LEVEL)

__version__ = VERSION
__all__ = [
    "chat",
    "embed",
    "hub",
]
