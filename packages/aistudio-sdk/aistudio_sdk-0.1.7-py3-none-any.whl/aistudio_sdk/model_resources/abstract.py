
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
本文件实现了模型方法的父类

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2023/07/24
"""
import os
from aistudio_sdk import err_code
from aistudio_sdk.util import convert_to_dict_object, err_resp


def check_auth(f):
    """check user info"""
    def wrapper(self, **kwargs):
        if not self.user_id or not self.token:
            resp = err_resp(err_code.ERR_FAILED, 
                            "No authentication info.")
            return convert_to_dict_object(resp)

        # add user info
        kwargs.update({
            "user_id": self.user_id,
            "token": self.token,
        })
        return f(self, **kwargs)
    return wrapper


class APIResource:
    OBJECT_NAME = ""

    def __init__(self):
        self.__user_id = os.getenv("WEBIDE_USERID", default="")
        self.__token = os.getenv("STUDIO_MODEL_API_SDK_USER_JWT_TOKEN", default="")

    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def token(self):
        return self.__token

    @check_auth
    def create(self, **kwargs):
        """子类实现"""
        pass
