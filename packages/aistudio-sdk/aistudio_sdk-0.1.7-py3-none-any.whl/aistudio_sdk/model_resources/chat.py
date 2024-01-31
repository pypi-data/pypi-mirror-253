# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
本文件实现了模型对话

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2023/07/24
"""
from aistudio_sdk.model_resources.abstract import APIResource, check_auth
from aistudio_sdk.api_requester import request_aistudio_completion
from aistudio_sdk.util import convert_to_dict_object

__all__ = [
    "create",
]


class Chat(APIResource):
    OBJECT_NAME = "chat"
    
    @check_auth
    def create(self, **kwargs):
        resp = request_aistudio_completion(**kwargs)
        return convert_to_dict_object(resp)


def create(**kwargs):
    return Chat().create(**kwargs)
    