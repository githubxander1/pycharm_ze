import json
from pprint import pprint
from random import random

import allure
import requests

from CompanyProject.Fastbull.Api_fastbull.api_key import ApiKey
from CompanyProject.Fastbull.Api_fastbull.config import *


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

        # 检查响应状态码和内容
        if res.status_code == 200:
            print("登录成功")
            print("返回内容:", res.json())
        else:
            pprint("Request failed with status code:", res.status_code)

        token = ak.get_text(res)
        print(token)
        # 验证token只生成一次
        token_random=random()
        return ak,token,res,token_random

print(token_fix())