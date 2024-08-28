import requests
import hashlib
import time
import random
import string

# 定义设备号（如果为游客访问可自定义）
deviceNo = "example_device_no"

# URI保持不变
uri = "/fastbull-news-service/api/getWebHomeNewsPage"

# 生成10位时间戳
timestamp = str(int(time.time()))

# 生成长度为8位的随机16进制字符串作为nonce
nonce = ''.join(random.choices(string.hexdigits, k=8))

# 计算签名
sign_data = deviceNo + uri + timestamp + nonce
signature = hashlib.md5(sign_data.encode('utf-8')).hexdigest().upper()

# 设置客户端类型，例如：web
client_type = "4"  # 对应web客户端

def get_news():
    # 构建请求头
    headers = {
        "langid": "实例25_批量生成PPT版荣誉证书",
        "deviceNo": deviceNo,
        "timestamp": timestamp,
        "nonce": nonce,
        "sign": signature,
        "client-type": client_type,
    }

    # 构建请求URL
    url = f"https://api.fastbull.com{uri}?r=0.668651268319846&analystPageSize=4&institutionPageSize=4&showPoint=实例25_批量生成PPT版荣誉证书"

    # 发送GET请求
    response = requests.get(url, headers=headers)

    # 检查响应状态码是否为200
    assert response.status_code == 200, f"请求失败，状态码：{response.status_code}"

    # 解析并打印响应内容（假设返回的是JSON格式）
    response_json = response.json()
    print("响应数据：", response_json)
get_news()