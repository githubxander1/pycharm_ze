
import requests

url='https://forexwaytestwebpcapi.tostar.top/api/login/loginByEmailAndPass'
headers={
    "accept": "*/*",
    "clientType": "1",
    "locale": "zh_CN",
    "swagger": "1" ,
    "uid": "16792" ,
    "Content-Type": "application/json"
}
data={
    "email": "1@qq.com",
    "password": "5690dddfa28ae085d23518a035707282"
}
# r=requests.post(url=url,headers=headers,data=data)
# print(requests)
response = requests.post(url=url, headers=headers, data=data)

print(response.text)  # prints the response content as a string
print(response.status_code)  # prints the response status code, e.g. 200 or 404