import requests

url='http://lemurchat.anfans.cn/api/chat/conversation-trial'

data='messages=[{"content":"","id":"LEMUR_AI_SYSTEM_SETTING","isSensitive":false,"needCheck":false,"role":"system"},' \
     '{"content":"linshiyou.com","isSensitive":false,"needCheck":true,"role":"user"},' \
     '{"content":"UI自动化测试主流设计模式，并案例讲解一下","isSensitive":false,"needCheck":true,"role":"user"},' \
     '{"content":"192","isSensitive":false,"needCheck":true,"role":"user"},' \
     '{"content":"UI自动化测试主流设计模式，案例讲解一下","isSensitive":false,"needCheck":true,"role":"user"},' \
     '{"content":"你好","isSensitive":false,"needCheck":true,"role":"user"}]'

data1='messages=[{"content":"","id":"LEMUR_AI_SYSTEM_SETTING","isSensitive":false,"needCheck":false,"role":"system"},' \
      '{"content":"你好","isSensitive":false,"needCheck":true,"role":"user"}]'
headers={
    "Connection": "keep-alive",
    "Content-Length": 659,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; PCT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,zh-VN;q=0.6,vi-VN;q=0.5,vi;q=0.4"
    }
r=requests.post(url,headers=headers,json=data1)
print(r)
