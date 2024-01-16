import requests
import json

url = "https://testfbapi.tostar.top/fastbull-news-service/api/postComment"

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
    "beta": "true",
    "btoken": "881c64f16359dc75180efa784ad047db",
    "cache-control": "no-cache",
    "client-type": "4",
    "clientversion": "latest",
    "content-type": "application/json",
    "deviceid": "2a3cd0189ea31b1d5f177b66df8705f8",
    "deviceno": "2a3cd0189ea31b1d5f177b66df8705f8",
    "langid": "1",
    "nonce": "b7JVrV2K",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sign": "51681BA0A71575D528E5480B2B62405E",
    "timestamp": "1705309004",
    "uid": "205050"
}

data = {
    "comment": "1",
    "imageInfoModel": [],
    "postId": "4279312_1",
    "type": 1
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)  # 输出响应状态码
print(response.json())  # 输出响应JSON数据（如果响应内容为JSON）