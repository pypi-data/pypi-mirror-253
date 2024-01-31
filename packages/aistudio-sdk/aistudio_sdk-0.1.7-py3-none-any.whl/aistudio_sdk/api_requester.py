# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
本文件实现了请求过程

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2023/07/24
"""
import os
import time
import tqdm
import json
import requests
import logging
from urllib.parse import quote
from aistudio_sdk import err_code
from aistudio_sdk import config, log
from aistudio_sdk.util import err_resp
from aistudio_sdk.util import gen_ISO_format_datestr
from aistudio_sdk.util import file_to_base64
from aistudio_sdk.util import create_sha256_file_and_encode_base64
from aistudio_sdk.version import VERSION

CONNECTION_RETRY_TIMES = config.CONNECTION_RETRY_TIMES
CONNECTION_TIMEOUT = config.CONNECTION_TIMEOUT
CONNECTION_TIMEOUT_DOWNLOAD = config.CONNECTION_TIMEOUT_DOWNLOAD
CONNECTION_TIMEOUT_UPLOAD = config.CONNECTION_TIMEOUT_UPLOAD


def _request(method, url, headers, data):
    """
    Params
        :url: http url
        :headers: dictionary of HTTP Headers to send
        :json_data: json data to send in the body
        :data: dictionary, list of tuples, bytes, or file-like object to send in the body
    Returns
        response data in json format
    """
    for _ in range(CONNECTION_RETRY_TIMES):
        try:
            err_msg = ''
            response = requests.request(method, url, headers=headers, data=data, timeout=CONNECTION_TIMEOUT)
            return response.json()
        except requests.exceptions.JSONDecodeError:
            err_msg = "Response body does not contain valid json: {}".format(response)
        except Exception as e:
            err_msg = 'Error occurred when request for "{}": {}.'.format(url, str(e))

    log.debug(err_msg)
    return err_resp(err_code.ERR_FAILED, 
                    err_msg[:500])


#################### AIStudio API ####################
def _post_aistudio(model_url, **kwargs):
    """请求AIStudio API"""
    url = "{}{}".format(
        os.getenv("STUDIO_MODEL_API_URL_PREFIX", default=config.STUDIO_MODEL_API_URL_PREFIX_DEFAULT),
        model_url
    )
    authorization = kwargs.pop("authorization", "")
    body = {k: v for k, v in kwargs.items()}
    log.debug(body)
    
    payload = json.dumps(body)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': authorization,
        'SDK-Version': str(VERSION),
    }
    resp = _request('POST', url, headers, payload)

    def extract_ernie_response(resp):
        """
        extract ernie bot response from aistudio response
        Param
            :resp: {'logId': '67635a456177a8665cc5e4060e4b7f76', 'errorCode': 0, 'errorMsg': 'success', 'result': <ernie_bot_response_info...>}
        Return
            <ernie_bot_response_info>
        """
        # no response
        if not resp:
            return err_resp(err_code.ERR_FAILED,
                            "Ernie response is empty.")
        
        # not aistudio-formatted
        if "logId" not in resp:
            return resp
        
        error_code = resp.get("errorCode", None)
        # success
        if error_code == err_code.ERR_OK:
            return resp.get("result", None)
        # error
        log.debug(resp)
        error_msg = resp.get("errorMsg", None)
        return err_resp(error_code, error_msg)

    return extract_ernie_response(resp)


def request_aistudio_completion(**kwargs):
    """
    请求AIStudio chat completion
    """
    url = config.COMPLETION_URL
    kwargs.update({'authorization': 'token {} {}'.format(kwargs.pop("user_id", ""), kwargs.pop("token", ""))})
    return _post_aistudio(url, **kwargs)


def request_aistudio_embedding(**kwargs):
    """
    请求AIStudio embed
    """
    url = config.EMBEDDING_URL
    kwargs.update({'authorization': 'token {} {}'.format(kwargs.pop("user_id", ""), kwargs.pop("token", ""))})
    return _post_aistudio(url, **kwargs)


#################### 文心千帆官方API ####################
def _post_wenxinworkshop(url, **kwargs):
    """
    请求文心千帆官方API
    Params
        url: http url后缀
    """
    url = "{}{}".format(config.WENXIN_URL_PREFIX, url)
    body = {k: v for k, v in kwargs.items()}
    payload = json.dumps(body)
    headers = {
        'Content-Type': 'application/json'
    }
    return _request('POST', url, headers, payload)


def request_wenxin_ernie_bot(**kwargs):
    """
    请求文心千帆 ERNIE-Bot 模型
    - doc: https://cloud.baidu.com/doc/WENXINWORKSHOP/s/jlil56u11
    """
    url = config.WENXIN_ERNIE_BOT_URL
    return _post_wenxinworkshop(url, **kwargs)


def request_wenxin_embedding_v1(**kwargs):
    """
    请求文心千帆 Embedding-V1 模型
    - doc: https://cloud.baidu.com/doc/WENXINWORKSHOP/s/alj562vvu
    """
    url = config.WENXIN_EMBEDDING_V1_URL
    return _post_wenxinworkshop(url, **kwargs)


#################### AIStudio 云端模型库 API ####################
def _request_aistudio_hub(method, url, headers, data):
    """
    request aistudio hub
    """
    for _ in range(CONNECTION_RETRY_TIMES):
        try:
            err_msg = ''
            response = requests.request(method, url, headers=headers,
                                        data=data, timeout=CONNECTION_TIMEOUT)
            return response.json()
        except requests.exceptions.JSONDecodeError:
            err_msg = "Response body does not contain valid json: {}".format(response)
            biz_code = response.status_code

    log.debug(err_msg)
    return err_resp(err_code.ERR_FAILED, 
                    err_msg[:500],
                    biz_code)


def request_aistudio_hub(**kwargs):
    """
    请求AIStudio hub
    """
    headers = _header_fill(token=kwargs['token'])
    kwargs.pop('token')

    url = "{}{}".format(
        os.getenv("STUDIO_MODEL_API_URL_PREFIX", default=config.STUDIO_MODEL_API_URL_PREFIX_DEFAULT), 
        config.HUB_URL
    )

    body = {k: v for k, v in kwargs.items()}
    log.debug(body)

    payload = json.dumps(body)
    resp = _request_aistudio_hub('POST', url, headers, payload)

    return resp


def request_aistudio_repo_visible(**kwargs):
    """
    请求AIStudio hub 查看repo可见权限
    """
    headers = _header_fill(token=kwargs['token'])

    url = "{}{}".format(
        os.getenv("STUDIO_MODEL_API_URL_PREFIX", default=config.STUDIO_MODEL_API_URL_PREFIX_DEFAULT), 
        config.HUB_URL_VISIBLE_CHECK
    )
    url = url + f"?repoId={quote(kwargs['repoId'], safe='')}&authorization=1"
    method = 'GET'
    try:
        err_msg = ''
        response = requests.request(method, url, headers=headers,
                                    timeout=CONNECTION_TIMEOUT)
        return response.json()
    except requests.exceptions.JSONDecodeError:
        err_msg = "Response body does not contain valid json: {}".format(response)
        biz_code = response.status_code

    return err_resp(err_code.ERR_FAILED, 
                    err_msg[:500],
                    biz_code)


#################### AIStudio Gitea API ####################
def _request_gitea(method, url, headers, data):
    """
    request gitea
    """
    for _ in range(CONNECTION_RETRY_TIMES):
        session = requests.Session()
        response = session.request(method, url, headers=headers, data=data, timeout=CONNECTION_TIMEOUT)
        session.close()

        if response.status_code not in (200, 201):
            return err_resp(err_code.ERR_GITEA_DOWNLOAD_FILE_FAILED if
                            method == "GET" else err_code.ERR_GITEA_UPLOAD_FILE_FAILED,
                            response.content.decode()[:500],
                            biz_code=response.status_code)
        else:
            return response.json()


def timing_decorator(func):
    """
    time cost decorator
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} done, time cost: {elapsed_time:.2f}s")
        return result
    return wrapper


@timing_decorator
def _upload(method, url, headers, data):
    """
    _upload proc
    """
    session = requests.Session()
    response = session.request(method, url, headers=headers, data=data, 
                               stream=True, timeout=CONNECTION_TIMEOUT_UPLOAD)
    session.close()

    if response.status_code not in (200, 201):
        return err_resp(err_code.ERR_GITEA_UPLOAD_FILE_FAILED, 
                        response.content[:500],
                        biz_code=response.status_code)
    else:
        return response.json()


@timing_decorator
def _download(url, download_path, headers):
    """
    Params
        :url: http url
        :download_path: download path
        :headers: headers
    Returns
        file
    """
    # 默认allow_redirects=True，即自动重定向，如果是LFS文件会直接从BOS下载
    response = requests.request('GET', url, stream=True, headers=headers, 
                                timeout=CONNECTION_TIMEOUT_DOWNLOAD)

    if response.status_code == 200:
        ret = {}
    elif response.status_code == 404:
        try:
            message = response.json()["message"]
        except requests.exceptions.JSONDecodeError:
            message = response.content.decode()

        ret = err_resp(err_code.ERR_FILE_NOT_FOUND, 
                        message,
                        response.status_code)
    else:
        ret = err_resp(err_code.ERR_GITEA_DOWNLOAD_FILE_FAILED, 
                        f'Download failed, response code: {response.status_code}',
                        response.status_code)

    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024 * 100
    progress_bar = tqdm.tqdm(total=total_size, ncols=50, unit='iB', unit_scale=True, 
                             desc='Downloading file')

    with open(download_path, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()
    if total_size != 0 and progress_bar.n != total_size:
        print("ERROR, something went wrong")

    return ret


def request_aistudio_git_download(url, download_path, token):
    """
    请求AIStudio gitea文件下载
    """
    headers = _header_fill(token=token)
    res = _download(url, download_path, headers)
    return res


def request_aistudio_git_file_info(call_host, user_name, repo_name, file_path, 
                                   revision, token):
    """
    请求AIStudio gitea 文件info
    GET /api/v1/repos/{owner}/{repo}/contents/{filepath} 返回的文件的数据、大小、编码等metadata信息+文件内容，或者文件夹中的文件列表
    """
    # 构建查询url
    url = f"{call_host}/api/v1/repos/{quote(user_name, safe='')}/" \
      f"{quote(repo_name, safe='')}/contents/{quote(file_path, safe='')}"
    if revision != 'master':
        url += f"?ref={quote(revision, safe='')}"

    headers = _header_fill(token=token)
    res = _request_gitea('GET', url, headers, "")
    logging.debug(f"...result of GET /contents/{file_path}: {res}")
    return res


def request_aistudio_git_file_type(call_host, user_name, repo_name, revision, 
                                   path_in_repo, token):
    """
    请求AIStudio gitea 确认文件类型
    """
    headers = _header_fill(token=token)

    url = f"{call_host}/{quote(user_name, safe='')}/{quote(repo_name, safe='')}/preupload/{quote(revision, safe='')}"
    
    params = {
        "files": [{
            "path": path_in_repo # 远程文件路径（相对于仓库根路径）
        }]
    }

    payload = json.dumps(params)
    result = _request_gitea('POST', url, headers, data=payload)
    logging.debug(f"...result of POST /preupload: {result}")
    if 'error_code' in result:
        res = result
    elif 'files' not in result or not result['files'] or 'lfs' not in result['files'][0]:
        res = err_resp(err_code.ERR_GITEA_FAILED, 
                        str(result)[:500])
    else:
        res = {
            'is_lfs': result['files'][0]['lfs']
        }

    return res

def _parse_sts_token(upload_section: dict) -> dict:
    """
    解析sts_token

    "upload": {
        "href": "https://some-download.com",
        "header": {
            "Key": "value"
        },
        "sts_token": {
            "bosHost":""
            "bucketName": "",
            "key":"",
            "accessKeyId":"",
            "secretAccessKey":"",
            "sessionToken":"",
            "createTime":"",
            "expiration":""
            }
        "expires_at": "2016-11-10T15:29:07Z"
    }
    """
    sts_token = upload_section.get("sts_token", {})
    if sts_token and sts_token.get("accessKeyId"):
        return {
            "bos_host": sts_token.get("bosHost"),
            "bucket_name": sts_token.get("bucketName"),
            "key": sts_token.get("key"),
            "access_key_id": sts_token.get("accessKeyId"),
            "secret_access_key": sts_token.get("secretAccessKey"),
            "session_token": sts_token.get("sessionToken"),
            "expiration": sts_token.get("expiration")
        }
    return {}



def request_aistudio_git_upload_access(call_host, user_name, repo_name, revision, file_size, 
                                       sha256, token):
    """
    请求AIStudio gitea 申请上传LFS文件.
    只支持单文件
    """
    params = {
        'Content-Type': 'application/vnd.git-lfs+json; charset=utf-8',
        'Accept': 'application/vnd.git-lfs+json'
    }
    headers = _header_fill(params=params, token=token)

    url = f"{call_host}/{quote(user_name, safe='')}/{quote(repo_name, safe='')}.git/info/lfs/objects/batch"

    params = {
        "operation": "upload", # 申请动作为上传
        "objects": [
            {
                "oid": sha256, # SHA256哈希
                "size": file_size  # 单位byte
            }
        ],
        "transfers": [
            "lfs-standalone-file", "basic"
        ],
        "ref": {
            "name": f"refs/heads/{revision}" # 分支
        },
        "hash_algo": "sha256"
    }
    
    payload = json.dumps(params)
    result = _request_gitea('POST', url, headers, payload)
    logging.debug(f"...result of POST /batch: {result}")
    if 'error_code' in result:
        res = result
    elif 'objects' not in result or not result['objects']:
        res = err_resp(err_code.ERR_GITEA_FAILED, 
                        str(result)[:500])
    else:
        tmp = result['objects'][0]
        # 已经存在的文件，不需要上传，actions为空
        res = {
            'upload': True if 'actions' in tmp and 'upload' in tmp['actions'] else False,
            'upload_href': tmp['actions']['upload']['href'] if 'actions' in tmp else '',
            'sts_token': _parse_sts_token(tmp['actions']['upload']) if 'actions' in tmp else {},
            'verify_href': tmp['actions']['verify']['href'] if 'actions' in tmp else ''
        }

    return res


@timing_decorator
def _lfs_upload(url, path_or_fileobj, headers):
    """
    上传LFS文件到bos
    """
    with open(path_or_fileobj, 'rb') as file:
        response = requests.request('PUT', url, headers=headers, data=file, 
                                    timeout=CONNECTION_TIMEOUT_UPLOAD, stream=True)
    return {'Content-Md5': response.headers['Content-Md5']}


def request_bos_upload(url, path_or_fileobj):
    """
    上传LFS文件到bos
    """
    params = {'Content-Type': 'application/octet-stream'}
    headers = _header_fill(params=params, token='')
    return _lfs_upload(url, path_or_fileobj, headers)


def get_exist_file_old_sha(info_res):
    """
    解析info_res
    """
    if 'error_code' in info_res and info_res['error_code'] != err_code.ERR_OK:
        return ''
    elif not info_res or 'sha' not in info_res:
        return ''
    else:
        old_sha = info_res['sha']
        return old_sha


def request_aistudio_git_upload_pointer(call_host, user_name, repo_name, revision, commit_message, 
                                        sha256, file_size, path_in_repo, token):
    """
    请求AIStudio gitea 上传LFS指针文件（到仓库）
    """
    # 检查指针文件是否已存在，存在的话，要调用更新接口
    info_res = request_aistudio_git_file_info(call_host, user_name, repo_name, path_in_repo, 
                                              revision, token)
    old_sha = get_exist_file_old_sha(info_res)
    if old_sha == '':
        method = 'POST'
    else:
        # 文件已存在，需要调用PUT接口更新
        method = 'PUT'

    headers = _header_fill(token=token)

    url = f"{call_host}/api/v1/repos/{quote(user_name, safe='')}/" \
      f"{quote(repo_name, safe='')}/contents/{quote(path_in_repo, safe='')}"

    params = {
        "branch": revision,     # 提交的分支
        "new_branch": revision, # 提交的分支
        "content": create_sha256_file_and_encode_base64(sha256, file_size),
        "lfsPointer": True,
        "dates": {
            "author": gen_ISO_format_datestr(),
            "committer": gen_ISO_format_datestr()
        },
        "message": commit_message
    }
    if method == 'PUT':
        params['sha'] = old_sha
    payload = json.dumps(params)

    res = _request_gitea(method, url, headers, payload)
    return res


def request_aistudio_git_upload_common(call_host, user_name, repo_name, revision, 
                                       commit_message, 
                                       path_or_fileobj, path_in_repo, token):
    """
    请求AIStudio gitea 上传普通文件（到仓库）
    """
    # 检查文件是否已存在，存在的话，要调用更新接口
    info_res = request_aistudio_git_file_info(call_host, user_name, repo_name, path_in_repo, 
                                              revision, token)
    old_sha = get_exist_file_old_sha(info_res)
    if old_sha == '':
        method = 'POST'
    else:
        # 文件已存在，需要调用PUT接口更新
        method = 'PUT'

    url = f"{call_host}/api/v1/repos/{quote(user_name, safe='')}/" \
      f"{quote(repo_name, safe='')}/contents/{quote(path_in_repo, safe='')}"
    headers = _header_fill(token=token)

    base64_data = file_to_base64(path_or_fileobj)

    params = {
        "branch": revision,     # 提交的分支
        "new_branch": revision, # 提交的分支
        "content": base64_data,
        "lfs": False,
        "dates": {
            "author": gen_ISO_format_datestr(),
            "committer": gen_ISO_format_datestr()
        },
        "message": commit_message
    }
    if method == 'PUT':
        params['sha'] = old_sha
    payload = json.dumps(params)

    res = _upload(method, url, headers, payload)

    return res

def request_aistudio_verify_lfs_file(call_host, oid: str, size: int, token=''):
    """
    param
        call_host: verify url
        oid: sha256, without sha256prefix
        size: file size

    """
    headers = {
        'Content-Type': 'application/vnd.git-lfs+json',
        'Accept': 'application/vnd.git-lfs+json'
    }
    params = {
        "oid": oid,
        "size": size
    }
    header = _header_fill(headers, token=token)
    res = requests.request("POST", call_host, headers=header, json=params, data=json.dumps(params))
    logging.debug(f"...result of POST /verify: {res.text}")
    if res.status_code not in (200, 201):
        return err_resp(err_code.ERR_GITEA_UPLOAD_FILE_FAILED,
                        res.json(),
                        biz_code=res.status_code)
    else:
        return res.json()


def _header_fill(params=None, token=''):
    """
    填充header
    """
    if token:
        auth = f'token {token}'
    else:
        auth = f'token {os.getenv("AISTUDIO_ACCESS_TOKEN", default="")}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth,
        'SDK-Version': str(VERSION)
    }
    if params:
        headers.update(params)
    return headers

