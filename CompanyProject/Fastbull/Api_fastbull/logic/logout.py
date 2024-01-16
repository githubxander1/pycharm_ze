import requests
import json
import time

# 定义请求头
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
    "uid": "204830",  # 用户ID应该由实际登录后的信息提供
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

# 根据实际情况进行断言验证，例如验证返回结果中是否包含预期的登出成功消息或错误信息
# assert 'expected_key' in response_json and response_json['expected_key'] == 'expected_value', "登出验证失败"

# 若登出成功后返回了特定的状态信息，可以提取并验证
# if 'logout_status' in response_json:
#     status = response_json['logout_status']
#     assert status == 'success', "登出状态验证失败"