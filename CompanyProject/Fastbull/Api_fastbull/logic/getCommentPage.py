import hashlib
import random
import time

import pytest
import requests
from CompanyProject.Fastbull.Api_fastbull.logic.common import generate_btoken, generate_sign_login, generate_token, \
    get_identity, generate_nonce


uid = "205050" #8@qq.com
# uid = "204830" #7@qq.com
btoken = "881c64f16359dc75180efa784ad047db"
# btoken参数
client_type = "4"
client_version="latest"
device_no = "51cee82782f69741d228946af2d2cda3"
uuid="2a3cd0189ea31b1d5f177b66df8705f8"

postId='4279312_1'

vip = "0"  # 根据实际情况填写会员状态
timestamp = str(int(time.time()))[:10]  # 获取当前时间戳
# nonce = generate_nonce()

def test_get_comment_page_endpoint():
    url = f"https://testfbapi.tostar.top/fastbull-news-service/api/getCommentPage?r=0.27805524689164374&pageIndex=1&pageSize=20&sortType=1&postId={postId}"
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(client_type, client_version, uuid,device_no),
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
        "deviceid": "51cee82782f69741d228946af2d2cda3",
        "deviceno": "51cee82782f69741d228946af2d2cda3",
        "langid": "1",
        "nonce": generate_nonce(),
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": generate_sign_login(uid, generate_token(get_identity()), timestamp, generate_nonce()),
        "timestamp":timestamp,
        "uid": uid
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    assert response.status_code == 200  # 或您期望的其他状态码
    # 添加更多的断言来验证响应头和响应体内容