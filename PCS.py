# -*- coding: utf-8 -*-
import Utils
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
