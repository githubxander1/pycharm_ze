import re
from pprint import pprint

import requests
import json

def login():
    url = "https://testfbapi.tostar.top/fastbull-user-service/api/postLoginByAccount"
    # 请求体数据
    data = {
        # "requestData": "OqRZEG9mm9B/y92h7+muv9Wo/hqLayfEHblOiW/1ePColbT1ffuMo1ApsQPHr4G02+zbOMm2tnftFXUAhKjlxV6rosUNFayqQABV7DhESBjMTNzgCI3tF5P5afpnQFK0Ux09uC6F4gHEE+MN4Ydt32pu25IbXW0GVRzoSjAaDxB+cQVsBQ2JKGlXPVEI+FfU",
        # 8@qq.com
        "requestData": "OqRZEG9mm9B/y92h7+muvwcxB8yVV/QwIWGPo5b44f6kMu6+64Nx3ZHpA/BbJRO7RKBB48RGqfRNBe+fehjZmu2L1wAKO884B1+7MKqDorE99P4QKtg9NrlPjtthAoaWXozHS7SJEboLxvkw0R5DK3jpe1JcPK05mOYHmHPkNps6laBE5o5z9cr5yv1aNiap",
    }
    response = requests.post(url, json=data)

    # 验证响应状态码
    assert response.status_code == 200, f"登录请求失败，状态码为：{response.status_code}"

    # 检查并打印返回的JSON数据（假设API返回的是JSON格式）
    # response_json = response.json()['bodyMessage']
    response_json = response.json()
    print(response_json)
    # body_message_str = response_json['bodyMessage'][1:-1]  # 去除首尾单引号
    body_message_str = response_json['bodyMessage']
    # print(body_message_str)
    # print(type(body_message_str))
    # 使用正则表达式提取 identity 字段的值
    match_result = re.search(r'"identity":"([^"]+)"', body_message_str)
    extracted_identity = match_result.group(1)
    print(extracted_identity)
    # return extracted_identity
    # if match_result:
    #     extracted_identity = match_result.group(1)
    #     print("提取到的身份信息:", extracted_identity)
    # else:
    #     print("无法找到身份信息")

login()