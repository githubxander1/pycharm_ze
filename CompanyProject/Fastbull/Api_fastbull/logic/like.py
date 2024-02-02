import time

import requests
import json

from CompanyProject.Fastbull.Api_fastbull.logic.common import generate_sign_login, get_identity, generate_btoken, \
    generate_nonce, generate_token


def post_like_operate(postId,like_type):
    """点赞操作
    1.postId:被点赞的帖子id
    2.like_type:1:点赞 2:取消点赞

    """
    url = "https://testfbapi.tostar.top/fastbull-news-service/api/postLikeOperate"

    uid = "205050"  # 8@qq.com
    btoken = "881c64f16359dc75180efa784ad047db"
    client_type = "4"
    client_version = "latest"
    device_no = "51cee82782f69741d228946af2d2cda3"
    uuid = "2a3cd0189ea31b1d5f177b66df8705f8"
    vip = "0"  # 根据实际情况填写会员状态
    timestamp = str(int(time.time()))[:10]  # 获取当前时间戳
    nonce = generate_nonce()

    headers = {
        "authority": "testfbapi.tostar.top",
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
        "beta": "true",
        "btoken": generate_btoken(client_type, client_version, uuid,device_no),
        "cache-control": "no-cache",
        "client-type": "4",
        "clientversion": "latest",
        "content-type": "application/json",
        "deviceid": "51cee82782f69741d228946af2d2cda3",
        "deviceno": "51cee82782f69741d228946af2d2cda3",
        "dnt": "1",
        "langid": "1",
        "nonce": nonce,
        "origin": "https://testfb.tostar.top",
        "pragma": "no-cache",
        "referer": "https://testfb.tostar.top/",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sign": generate_sign_login(uid, generate_token(get_identity()), timestamp, nonce),
        "timestamp": timestamp,
        "uid": uid,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    data = {
        "postId": postId,
        "operate": like_type    #点赞
        # "operate": 0 #取消点赞
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    assert response.status_code == 200  # 检查响应状态码是否为200（成功）
    # 根据实际需要添加更多断言，例如检查响应内容、头部信息等。
    print(response.json())  # 打印响应内容（假设响应是JSON格式）