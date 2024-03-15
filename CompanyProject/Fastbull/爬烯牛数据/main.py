import requests
import base64
import json
import time
import execjs

# 假设这里的 payload 和 sig 是经过处理后得到的base64编码字符串
payload_b64_encoded = "eyJwYXlsb2FkIjoiTGI3c3V0QjplMHN5MXRNQyVRJz0kRGJSQVFXcyRqYnhsOUMySSIsInNpZyI6IkNFODBFNkMxQzRDRTc3QjFFOTE3NzMwMjAyNzU5MDQiLCJ2IjoxfQ=="
sig = "CE704F132C4E47B31E91773020275904"

# 解码payload
payload_json_str = base64.b64decode(payload_b64_encoded).decode('utf-8')
payload_dict = json.loads(payload_json_str)

headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "cookie": "btoken=CHD5CV2MKHYQZC5IY6NVUFDML6XZ6C2C; hy_data_2020_id=18e3c341163d7b-0b979a8a27e662-4c657b58-2073600-18e3c3411641250; hy_data_2020_js_sdk={\"distinct_id\":\"18e3c341163d7b-0b979a8a27e662-4c657b58-2073600-18e3c3411641250\",\"site_id\":211,\"user_company\":105,\"props\":{},\"device_id\":\"18e3c341163d7b-0b979a8a27e662-4c657b58-2073600-18e3c3411641250\"}; sajssdk_2020_cross_new_user=1; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1710407029; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1710407763",
    "dnt": "1",
    "origin": "https://www.xiniudata.com",
    "referer": "https://www.xiniudata.com/industry/newest?from=data",
    "sec-ch-ua": '"Microsoft Edge";v="123", "Not\\A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
}

data = {
    "payload": payload_dict,
    "sig": sig,
    "v": 1,
}

url = "https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort"

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
    # 处理返回的结果
else:
    print(f"请求失败，状态码：{response.status_code}")

data=result['d']
print(data)

cxt = execjs.compile(open('犀牛数据.js', 'r', encoding='utf-8').read()).call('main', data)
print(cxt)