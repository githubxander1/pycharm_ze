# 用于处理token

import jsonpath as jsonpath
from jsonpath import jsonpath
import requests

from ApiTest_mindmaster.config.setting import config

from ApiTest_mindmaster.config.yaml_handler import yaml_data


def login():
    '''登录，接口返回token'''
    req = requests.post(url=config.host + '/api/user/login', json=yaml_data)
    return req


# print(login().json())


def save_token():
    """保存token信息"""
    res = login()
    # print(res.json())
    token = jsonpath(res.json(), '$..token')[0]
    # print(token)
    # token_type = jsonpath(res.json(),'$..token_type')
    # print(token_type)
    # token = " ".join([token_type, token])

    # token = r.json()['data']['token']
    token = 'Bearer' + ' ' + token
    # print(token)
    return token


class Context:
    """将token作为类属性"""
    token = ''


if __name__ == '__main__':
    print(save_token())
