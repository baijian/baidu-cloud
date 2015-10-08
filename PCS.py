# -*- coding: utf-8 -*-
"""
Personal Cloud Storage
"""
import Utils
import urllib
import Constants
import requests

ACCESS_TOKEN = Utils.read_config()['ACCESS_TOKEN']


def __get(url, params):
    params['access_token'] = ACCESS_TOKEN
    r = requests.get(url, params=params)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return False


def get_pcs_quota():
    """
    空间配额信息
    :return:
    """
    url = Constants.PCS_URL + Constants.PCS_COMMON_URI + Constants.PCS_USER_QUOTA_URI
    params = {
        'method': 'info',
    }
    quota_info = __get(url, params)
    if quota_info:
        quota_info['quota'] = Utils.format_disk_size(quota_info['quota'])
        quota_info['used'] = Utils.format_disk_size(quota_info['used'])
        return quota_info
    else:
        return False


def get_remote_file():
    url = Constants.PCS_URL + Constants.PCS_COMMON_URI
    pass


def add_pcs_dir(path):
    url = Constants.PCS_URL + Constants.PCS_COMMON_URI + Constants.PCS_FILE_RELATE_URI
    params = {
        'method': 'mkdir',
        'access_token': ACCESS_TOKEN,
        'path': path,
    }
    r = requests.post(url, params=params)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return False


def upload_file_to_pcs(path, file_path, overwrite=False):
    url = Constants.PCS_UPLOAD_URL + Constants.PCS_COMMON_URI + Constants.PCS_FILE_RELATE_URI
    print url
    params = {
        'method': 'upload',
        'access_token': ACCESS_TOKEN,
        'path': path,
    }
    if overwrite:
        params['ondup'] = 'overwrite'
    else:
        params['ondup'] = 'newcopy'
    f = open(file_path, "rb")
    r = requests.post(url + "?" + urllib.urlencode(params), files={'file': ('file', f)})
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return False
