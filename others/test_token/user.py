# -*- coding:utf-8 -*-
import requests


def user_info(host, token):
    url = host + '/pub/api/v1/web/user_info'
    headers = {"token": token}  # token 放在请求头
    r = requests.get(url=url, headers=headers)
    return r

