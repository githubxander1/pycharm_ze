from pprint import pprint

import requests
import json

# API endpoint URL
url = "https://testfbapi.tostar.top/fastbull-user-service/api/postLoginByAccount"

# 请求头
# headers = {
#     # "accept": "application/json;charset=UTF-8",
#     # "appType": "1",
#     # "langId": "0",
#     # "Content-Type": "application/json"
# }

# 请求体数据
data = {
    # "requestData": "OqRZEG9mm9B/y92h7+muv9Wo/hqLayfEHblOiW/1ePColbT1ffuMo1ApsQPHr4G02+zbOMm2tnftFXUAhKjlxV6rosUNFayqQABV7DhESBjMTNzgCI3tF5P5afpnQFK0Ux09uC6F4gHEE+MN4Ydt32pu25IbXW0GVRzoSjAaDxB+cQVsBQ2JKGlXPVEI+FfU",
    "requestData": "OqRZEG9mm9B/y92h7+muvwcxB8yVV/QwIWGPo5b44f6kMu6+64Nx3ZHpA/BbJRO7RKBB48RGqfRNBe+fehjZmu2L1wAKO884B1+7MKqDorHUDKYA6ohMA1bSmt2HHxCGHtGWY/MNprVpWHaxH+CMTZIrkUhLdIGBAWQ1PmUodXpeFjFWexLpDv5HHi6XEOg1",
    # "account": "7@qq.com",
    # "activityId": 55,
    # "clientType": 1,
    # "deviceId": "2a3cd0189ea31b1d5f177b66df8705f8",
    # "deviceModel": "iPhone XXX",
    # "password": "5690dddfa28ae085d23518a035707282",
    # "regId": 123
}

# 发送POST请求
# response = requests.post(url, headers=headers, json=data)
response = requests.post(url, json=data)

# 验证响应状态码
assert response.status_code == 200, f"登录请求失败，状态码为：{response.status_code}"

# 检查并打印返回的JSON数据（假设API返回的是JSON格式）
response_json = response.json()
pprint(f"登录响应数据：{response_json}")

# 进一步验证响应内容，请根据实际API文档添加具体的断言
# 示例：验证用户ID是否存在
# assert 'userId' in response_json and response_json['userId'] is not None, "登录成功但返回结果中未包含用户ID"