
import requests

url='https://forexwaytestwebpcapi.tostar.top/api/login/loginByEmailAndPass'
headers={
    # "accept": "*/*",
    # "clientType": "1",
    # "locale": "zh_CN",
    "swagger": '1' ,
    # "uid": '16792',
    # "Content-Type": "application/json"
}
data={
    "email": "1@qq.com",
    "password": "5690dddfa28ae085d23518a035707282"
}
response = requests.post(url=url, headers=headers, json=data)

print(response.text)  # prints the response content as a string
print(response.status_code)  # prints the response status code, e.g. 200 or 404
# import requests
# import json
# #
# url = 'https://forexwaytestapi.tostar.top/api/login/loginByEmailAndPass'
#
# headers = {
#     'uid': '0',
#     'random': 'p4bnBwxL',
#     'clientType': '2',
#     'btoken': '377682b465d960c686efca8a255124fe',
#     'x-signature': '2cd1f056433f9731e0d57556b0e23a60',
#     'locale': 'zh_CN1',
#     'version': '2.3.5',
#     'deviceId': '3d18321ba7e437baaae5245e3f02be3d',
#     'channelId': '2',
#     'MD5Code': '0cc982ee09810d051d37916850c0e058',
#     'Content-Type': 'application/json; charset=utf-8',
#     'Accept-Encoding': 'gzip',
#     'User-Agent': 'okhttp/4.9.3'
# }
#
# data = {
#     'email': '1@qq.com',
#     'password': '5690dddfa28ae085d23518a035707282'
# }
#
# response = requests.post(url, headers=headers, data=json.dumps(data))
#
# print(response.status_code)
# print(response.json())