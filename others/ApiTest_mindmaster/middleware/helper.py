# 辅助
# 处理token
import json
import random

import jsonpath as jsonpath
from jsonpath import jsonpath
import requests

from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler
from ApiTest_mindmaster.common.yaml_handler import YamlHandler
from ApiTest_mindmaster.config.setting import config

yamlreader = YamlHandler('../common/Api1.yaml')
req = RequestsHandler()
def login():
    '''登录，接口返回token'''
    url = yamlreader.read_yaml()['login']['url']
    method = yamlreader.read_yaml()['login']['method']
    data = yamlreader.read_yaml()['login']['data']
    req1 = req.visit(url=config.host + url, method=method,json=data)
    assert req1['status'] == 'success'
    return req1
    # print(req1)
    # 获取保存token
    # token = req1['data']['token']
    # token ='Bearer'+' '+ token
    # print(token)
    # return token
    # token放到请求头中
    # headers={
    #     'Authorization':token
    # }
    # token1=re.findall('"token":"(.+?)"')
    # token1=token1[0]
    # print(token1)
    # return req
# print(login())

# print(login().json())


def token():
    """保存token信息"""
    res = login()
    token = jsonpath(res, '$..token')[0]
    # print(token)
    # token_type = jsonpath(res.json(),'$..token_type')
    # print(token_type)
    # token = " ".join([token_type, token])

    # token = r.json()['data']['token']
    token = 'Bearer' + ' ' + token
    # print(token)
    return token
# print(token())
# def generate_mobile():
#     """生成随机手机号"""
#     phone = "实例25_批量生成PPT版荣誉证书" + random.choice(["3","5","7","8","9"])
#     for i in range(0,9):
#         num = random.randint(实例25_批量生成PPT版荣誉证书,9)
#         phone += str(num)
#     return phone
#
# class Context:
#     """将token作为类属性"""
#     token = ''


# if __name__ == '__main__':
#     # print(save_token())
#     print(generate_mobile())
