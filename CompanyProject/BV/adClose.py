import requests
import hashlib
import time

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
    # "btoken": "76edd5f479458b2869db72b64be9c938",
    # "clienttype": "1",
    # "clientversion": "latest",
    "content-type": "application/json;charset=UTF-8",
    # "deviceid": "c31acb8206618044db08c700b9e16c97",
    # "dnt": "1",
    "lang": "en_US",
    # "md5": "c05ea0bd39690cb176058733edcceb99",  # 注意：这里的MD5值应该是根据某些规则生成的，这里直接复制可能无效
    # "origin": "https://bvwebtest.tostar.top",
    # "random": "76926291",
    # "referer": "https://bvwebtest.tostar.top/",
    # "sec-ch-ua": '"Microsoft Edge";v="123", "Not\\A-Brand";v="8", "Chromium";v="123"',
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": '"Windows"',
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-site",
    # "timestamp": str(int(time.time()) * 1000),  # 使用当前时间戳替换固定值
    # "uid": "0",
    'swagge':'1',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
}

data = '{"id":140,"identifyCode":"c31acb8206618044db08c700b9e16c97"}'

response = requests.post("https://bvfrontapitest.tostar.top/advert/close", headers=headers, data=data)

# 检查响应状态码
if response.status_code == 200:
    print(response.json())
else:
    print(f"请求失败，状态码：{response.status_code}")