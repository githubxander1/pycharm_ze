# 这是一个特殊的pytest模块，可以放置在任意目录下，用于定义fixture、钩子函数、共享的测试配置和初始化代码。它可以被pytest自动发现并使用。
import base64
import json
import hashlib
import random
import re
import string
import time

import pytest
from Crypto.Cipher import AES
import requests

from CompanyProject.Fastbull.Api_fastbull.common.requests_handler import RequestsHandler
from CompanyProject.Fastbull.Api_fastbull.common.yaml_handler import YamlHandler

# nonce = generate_nonce()
req=RequestsHandler()
yamlhandler=YamlHandler('../data/Api.yaml')
# 公共常量
DEVELOPMENT_KEY = "c0iOcX2p1v782YUY"
DEVELOPMENT_IV = "Bai1unC1ub1sBest"

common_data = {
    'uid' : '205050',#8@qq.com
    # uid = "204830" #7@qq.com
    'uuid' : "22fe60c8ab2abcf803c386d8edd4353f",
    'deviceNo' : "51cee82782f69741d228946af2d2cda3",
    'client_type' : "4",
    'client_version':"latest",
    'device_no' : "51cee82782f69741d228946af2d2cda3",
    # 'uuid':"2a3cd0189ea31b1d5f177b66df8705f8"
    'postId':'3707814_1'
}
# print(common_data['uid'])
# uid = "205050" #8@qq.com
# # uid = "204830" #7@qq.com
# uuid="22fe60c8ab2abcf803c386d8edd4353f"
# deviceNo = "51cee82782f69741d228946af2d2cda3"

timestamp = str(int(time.time() * 1000) // 100)
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
# 定义生成nonce方法
def generate_nonce():
    return ''.join([random.choice('0123456789ABCDEF') for _ in range(8)])
def headers1(nonce):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(common_data["client_type"], common_data["client_version"], common_data['uuid'],
                                  common_data['device_no']),
        "cache-control": "no-cache",
        "client-type": common_data["client_type"],
        "clientversion": common_data["client_version"],
        "content-type": "application/json",
        "deviceid": "2a3cd0189ea31b1d5f177b66df8705f8",  # 根据实际情况填写设备ID
        "deviceno": "2a3cd0189ea31b1d5f177b66df8705f8",  # 根据实际情况填写设备号
        "langid": "实例25_批量生成PPT版荣誉证书",
        "nonce": nonce,
        "pragma": "no-cache",
        # 下面是浏览器相关头信息，如果在非浏览器环境下可以不设置
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": generate_sign_login(common_data['uid'], generate_token(get_identity()), timestamp, nonce),
        "timestamp": timestamp,
        "uid": common_data['uid']
        # "uid": '205050'
    }
    return headers

def generate_token(identity):
    key_test = 'c0iOcX2p1v782YUY'
    iv_test = 'Bai1unC1ub1sBest'
    cipher = AES.new(key_test.encode(), AES.MODE_CBC, iv_test.encode())
    token = cipher.decrypt(base64.b64decode(identity)).decode().rstrip('\0')
    return token

# 实现签名生成逻辑
def generate_sign_notLogin():
    deviceNo = "51cee82782f69741d228946af2d2cda3"  # edge
    # URI保持不变
    uri = "/fastbull-news-service/api/postComment"
    # 生成10位时间戳
    timestamp = str(int(time.time()))
    # 生成长度为8位的随机16进制字符串作为nonce
    nonce = ''.join(random.choices(string.hexdigits, k=8))
    # 计算签名
    sign_data = deviceNo + uri + timestamp + nonce
    sign_notLogin = hashlib.md5(sign_data.encode('utf-8')).hexdigest().upper()
    # print(f'sign：{sign_notLogin}')  # C828E14487F0DE9A4E4322F0A7D80AB8
    return sign_notLogin

def generate_sign_login(uid, token, timestamp, nonce):
    # 创建登录用户的签名
    login_sign_data = f'{uid}{token}{timestamp}{nonce}'
    sign_login = hashlib.md5(login_sign_data.encode()).hexdigest().upper()
    return sign_login

# 根据文档内容模拟生成bToken（这里假设uuid等是预先获取到的）
def generate_btoken(client_type, client_version, uuid, device_no):
    if device_no is None:
        # 如果设备号非必传，则可以省略或使用默认值
        device_no = "51cee82782f69741d228946af2d2cda3"

    b_token_data = f"{client_type}_{client_version}_{uuid}_{device_no}"
    b_token = hashlib.md5(b_token_data.encode()).hexdigest()
    return b_token

@pytest.fixture(scope='session')
def login():
    data=yamlhandler.read_yaml()['login']
    url = data['url']
    method = data['method']
    body = data['body']

    response = req.visit(method, url, json=body)

    assert response.status_code == 200, f"登录请求失败，状态码为：{response.status_code}"

    response_json = response.json()
    return response_json
# @pytest.fixture(scope='session')
def get_identity():
    response_json=login()
    body_message_str = response_json['bodyMessage']
    # 使用正则表达式提取 identity 字段的值
    match_result = re.search(r'"identity":"([^"]+)"', body_message_str)
    extracted_identity = match_result.group(1)
    # print(extracted_identity)
    return extracted_identity
# def get_identity():
#     url = "https://testfbapi.tostar.top/fastbull-user-service/api/postLoginByAccount"
#     # 请求体数据
#     data = {
#         # "requestData": "OqRZEG9mm9B/y92h7+muv9Wo/hqLayfEHblOiW/1ePColbT1ffuMo1ApsQPHr4G02+zbOMm2tnftFXUAhKjlxV6rosUNFayqQABV7DhESBjMTNzgCI3tF5P5afpnQFK0Ux09uC6F4gHEE+MN4Ydt32pu25IbXW0GVRzoSjAaDxB+cQVsBQ2JKGlXPVEI+FfU",
#         # 8@qq.com
#         "requestData": "OqRZEG9mm9B/y92h7+muvwcxB8yVV/QwIWGPo5b44f6kMu6+64Nx3ZHpA/BbJRO7RKBB48RGqfRNBe+fehjZmu2L1wAKO884B1+7MKqDorE99P4QKtg9NrlPjtthAoaWXozHS7SJEboLxvkw0R5DK3jpe1JcPK05mOYHmHPkNps6laBE5o5z9cr5yv1aNiap",
#     }
#     response = requests.post(url, json=data)
#
#     # 验证响应状态码
#     assert response.status_code == 200, f"登录请求失败，状态码为：{response.status_code}"
#
#     # 检查并打印返回的JSON数据（假设API返回的是JSON格式）
#     response_json = response.json()
#     # print(response_json)
#     body_message_str = response_json['bodyMessage']
#     # 使用正则表达式提取 identity 字段的值
#     match_result = re.search(r'"identity":"([^"]+)"', body_message_str)
#     extracted_identity = match_result.group(实例25_批量生成PPT版荣誉证书)
#     # print(extracted_identity)
#     return extracted_identity
# print(get_identity())