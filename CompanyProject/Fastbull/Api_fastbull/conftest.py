import json
from pprint import pprint
from random import random

import allure
import pytest
import requests

from CompanyProject.Fastbull.Api_fastbull.api_key import ApiKey
from CompanyProject.Fastbull.Api_fastbull.config import *

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.fixture(scope='session')
def token_fix():
    ak=ApiKey()

    with allure.step('获取token'):
        headers = {
            "appType": '1',
            "langId": '1',
            "accept": "application/json;charset=UTF-8",
            "Content-Type": "application/json"
        }

        request_data = "OqRZEG9mm9B/y92h7+muv9Wo/hqLayfEHblOiW/1ePColbT1ffuMo1ApsQPHr4G02+zbOMm2tnftFXUAhKjlxV6rosUNFayqQABV7DhESBjMTNzgCI3tF5P5afpnQFK0Ux09uC6F4gHEE+MN4Ydt32pu25IbXW0GVRzoSjAaDxB+cQVsBQ2JKGlXPVEI+FfU"

        res = ak.post(url, headers=headers, data=json.dumps({"requestData": request_data}))
        bodyMessage=res.json()['bodyMessage']

        token = ak.get_text(bodyMessage,'rcToken')
        # print(token[0])
        # print(type(token))
        # print(token)
        # 验证token只生成一次
        token_random=random()
        return ak,token,res,token_random

# print(token_fix())