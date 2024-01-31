import base64

import requests
import time


from CompanyProject.Fastbull.Api_fastbull.logic.common import generate_btoken, generate_sign_login, generate_token, \
    get_identity, generate_nonce


uid = "205050" #8@qq.com
btoken = "881c64f16359dc75180efa784ad047db"
client_type = "4"
client_version="latest"
device_no = "51cee82782f69741d228946af2d2cda3"
uuid="2a3cd0189ea31b1d5f177b66df8705f8"
vip = "0"  # 根据实际情况填写会员状态
timestamp = str(int(time.time()))[:10]  # 获取当前时间戳
nonce = generate_nonce()


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
    "beta": "true",
    "btoken": generate_btoken(client_type, client_version, uuid,device_no),
    "cache-control": "no-cache",
    "client-type": client_type,
    "clientversion": client_version,
    "content-type": "application/json",
    "deviceid": "2a3cd0189ea31b1d5f177b66df8705f8",  # 根据实际情况填写设备ID
    "deviceno": "2a3cd0189ea31b1d5f177b66df8705f8",  # 根据实际情况填写设备号
    "langid": "1",
    "nonce": nonce,
    "pragma": "no-cache",
    # 下面是浏览器相关头信息，如果在非浏览器环境下可以不设置
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sign": generate_sign_login(uid, generate_token(get_identity()), timestamp, nonce),
    "timestamp": timestamp,
    "uid": uid
}

body = {
    "comment": "评论111",
    "imageInfoModel": [],
    "postId": "3707814_1",#新闻id：对当今世界的资产泡沫要敬而远之
    "type": 1
}

# response = requests.post("https://api.fastbull.com/fastbull-news-service/api/postComment", headers=headers, json=body)
response = requests.post("https://testfbapi.tostar.top/fastbull-news-service/api/postComment", headers=headers, json=body)

print(response.status_code)
print(response.json())
# comment_id=response.json()['bodyMessage']['Id']
# print(comment_id)
