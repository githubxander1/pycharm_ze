import re
import time

import requests

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

def logout(uid):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "btoken": "881c64f16359dc75180efa784ad047db",
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
        "content-type": "application/json",
        "deviceid": "2a3cd0189ea31b1d5f177b66df8705f8",
        "deviceno": "2a3cd0189ea31b1d5f177b66df8705f8",
        "langid": "1",
        "nonce": "zBYYHlR1",  # 这个值可能需要每次请求时动态生成
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": "1C6E1B73B0DB6465E34BB7C1338B03E9",  # 这个签名可能需要根据参数和密钥计算得出
        "timestamp": str(int(time.time())),  # 使用当前时间戳替换
        "uid": uid,  # 8@qq.com 用户ID应该由实际登录后的信息提供
        "x-http-method-override": "put"
    }

    # 登出请求体通常为空
    data = {}

    # 发送PUT请求
    response = requests.put(
        "https://testfbapi.tostar.top/fastbull-user-service/api/putLogout",
        headers=headers,
        json=data,
    )

    # 检查响应状态码
    assert response.status_code == 200, f"登出失败，状态码：{response.status_code}"

    # 解析并打印响应内容
    response_json = response.json()
    print(response_json)