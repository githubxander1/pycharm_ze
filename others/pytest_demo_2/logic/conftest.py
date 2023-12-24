from random import random

import allure
import pytest

from others.pytest_demo_2.api_keyword.api_key import ApiKey
from others.pytest_demo_2.params.allParams import URL


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 项目级fix，整个项目只初始化一次
# @pytest.fixture(scope='session')
def token_fix():
    # 初始化工具类
    ak = ApiKey()
    with allure.step("发送登录接口请求，并获取token，整个项目只生成一次"):
        # 请求接口
        url = URL+ '/api/user/login'
        # 请求参数
        data = {
            'email': "2695418206@qq.co",
            'pw': "f2d8ddfc169a0ee6f8b0ecd924b1d300"
        }
        # post请求
        res = ak.post(url=url, json=data)
        data = res.text
        print(data)
        # 获取token
        token = ak.get_text(data,'token')
        print(token)
        # # 验证代码，验证token只生成一次
        # token_random = random()
        # return ak, token, res, token_random

print(token_fix())