import requests
import hashlib
import time
import random

def generate_nonce():
    return ''.join(['%02X' % random.randint(0, 255) for i in range(4)])

def generate_sign(uid, btoken, timestamp, nonce):
    raw_str = f"{uid}{btoken}{timestamp}{nonce}"
    sign = hashlib.md5(raw_str.encode('utf-8')).hexdigest().upper()
    return sign

# 填写真实值
uid = "205050"
btoken = "881c64f16359dc75180efa784ad047db"
client_type = "4"
vip = "0"  # 根据实际情况填写会员状态
timestamp = str(int(time.time()))[:10]  # 获取当前时间戳
nonce = generate_nonce()

sign = generate_sign(uid, btoken, timestamp, nonce)

post_id = "65a4c6b62751310001f2d599"  # 需要删除的评论postId

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
    "beta": "true",
    "btoken": btoken,
    "cache-control": "no-cache",
    "client-type": client_type,
    "clientversion": "latest",
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
    "sign": sign,
    "timestamp": timestamp,
    "uid": uid
}

url = f"https://api.fastbull.com/fastbull-news-service/api/deleteComment?postId={post_id}"

response = requests.post(url, headers=headers, json={})

print(response.status_code)
print(response.json())