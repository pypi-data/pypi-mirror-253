#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
config

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2023/07/24
"""

# Set to either 'debug' or 'info', controls console logging
DEFAULT_LOG_LEVEL = "info"
CONNECTION_TIMEOUT = 30     # second
CONNECTION_RETRY_TIMES = 1
CONNECTION_TIMEOUT_UPLOAD = 60 * 60     # second
CONNECTION_TIMEOUT_DOWNLOAD = 60 * 60     # second

COMMON_FILE_SIZE_LIMIT = 5 * 1024 * 1024  # 5M
LFS_FILE_SIZE_LIMIT = 50 * 1024 * 1024 * 1024 # 50G
LFS_FILE_SIZE_LIMIT_PUT = 5 * 1024 * 1024 * 1024 # 5G

# host
STUDIO_GIT_HOST_DEFAULT = "http://git.aistudio.baidu.com"
STUDIO_MODEL_API_URL_PREFIX_DEFAULT = "https://aistudio.baidu.com"

# AI Studio API
COMPLETION_URL = "/llm/lmapi/api/v1/chat/completions"
EMBEDDING_URL = "/llm/lmapi/api/v1/embedding"
HUB_URL = "/studio/model/sdk/add"
HUB_URL_VISIBLE_CHECK = "/modelcenter/v2/models/sdk/checkPermit"

# 文心千帆官方API https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu
WENXIN_URL_PREFIX = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop"
WENXIN_ERNIE_BOT_URL = "/chat/completions?access_token=xxx"
WENXIN_EMBEDDING_V1_URL = "/embeddings/embedding-v1?access_token=xxx"
