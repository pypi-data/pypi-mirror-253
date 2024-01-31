#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
error code

Authors: linyichong(linyichong@baidu.com)
Date:    2023/09/05
"""
# 成功
ERR_OK = 0
# SDK报错
ERR_FAILED = 10000

# 非法参数
ERR_PARAMS_INVALID = 10001
# 未设置token
ERR_TOKEN_IS_EMPTY = 10002
# 不能重复创建repo
ERR_REPO_EXISTS = 10003
# 找不到要下载的仓库文件
ERR_FILE_NOT_FOUND = 10004
# 找不到要上传的本地文件
ERR_UPLOAD_FILE_NOT_FOUND = 10005
# 上传文件过大
ERR_UPLOAD_FILE_TOO_LARGE = 10006
# 不支持上传文件夹
ERR_UPLOAD_FOLDER_NO_SUPPORT = 10007

# aistudio侧
# 报错
ERR_AISTUDIO_FAILED = 11000
# 创建仓库失败
ERR_AISTUDIO_CREATE_REPO_FAILED = 11001
# 没有仓库查看权限
ERR_AISTUDIO_NO_REPO_READ_AUTH = 11002

# gitea侧
# 报错
ERR_GITEA_FAILED = 12000
# 获取文件信息失败
ERR_GITEA_GET_FILEINFO_FAILED = 12001
# 下载文件失败
ERR_GITEA_DOWNLOAD_FILE_FAILED = 12002
# 上传文件失败
ERR_GITEA_UPLOAD_FILE_FAILED = 12003
