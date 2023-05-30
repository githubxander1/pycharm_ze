import requests

# 手机号登录
# url='https://fastbulllive-testwebpcapi.tostar.top/api/login/loginBySms'
# data={
# 'clientType': 4,
# 'code': "1234",
# 'countryCode': 9795,
# 'platformType': 4,
# 'telephone': "911111110"
# }
# r=requests.post(url,data)
# print(r.json())
# 邮箱登录
# url='https://fastbulllive-testwebpcapi.tostar.top/api/login/loginByEmailAndPass'
# data={
# 'clientType':4,
# 'email':"1@qq.com",
# 'password':"5690dddfa28ae085d23518a035707282",
# 'platformType':4
# }
# r=requests.post(url,data)
# print(r.json())
# 汇聊
# url = 'http://192.168.7.46:32013/api/UserLogin/AccountLogin'
url='https://forexwaytestwebpcapi.tostar.top/api/login/loginByEmailAndPass'
# header = {
#     'accept': 'application/json',
#     'Accept-Language': 'zh-CN',
#     'swagger': '1',
#     'Content-Type': 'application/json'
# }
headers={
    "accept": "*/*",
    "clientType": "1",
    "locale": "zh_CN",
    "swagger": "1" ,
    "uid": "16792" ,
    "Content-Type": "application/json"
}
# data1 = {"account": "1@qq.com",
#          "password": "5690DDDFA28AE085D23518A035707282"}
data={
    "email": "1@qq.com",
    "password": "5690dddfa28ae085d23518a035707282"
}
r = requests.post(url=url, headers=headers, data=data)
print(r.json())
