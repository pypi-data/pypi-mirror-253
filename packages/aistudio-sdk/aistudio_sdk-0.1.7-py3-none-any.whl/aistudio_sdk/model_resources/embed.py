# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
本文件实现了embedding方法

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2023/08/04
"""
from aistudio_sdk.model_resources.abstract import APIResource, check_auth
from aistudio_sdk.api_requester import request_aistudio_embedding
from aistudio_sdk.util import convert_to_dict_object

__all__ = [
    'embedding_v1',
]

class EmbeddingV1(APIResource):
    OBJECT_NAME = "embedding-v1"
    
    @check_auth
    def create(self, **kwargs):
        resp = request_aistudio_embedding(**kwargs)
        return convert_to_dict_object(resp)


def embedding_v1(**kwargs):
    return EmbeddingV1().create(**kwargs)
