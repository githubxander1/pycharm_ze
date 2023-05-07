# 辅助
# 处理token
import random

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
def generate_mobile():
    """生成随机手机号"""
    phone = "1" + random.choice(["3","5","7","8","9"])
    for i in range(0,9):
        num = random.randint(1,9)
        phone += str(num)
    return phone

class Context:
    """将token作为类属性"""
    token = ''


if __name__ == '__main__':
    # print(save_token())
    print(generate_mobile())
