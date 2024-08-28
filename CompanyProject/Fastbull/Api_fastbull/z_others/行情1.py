import requests

from CompanyProject.Fastbull.Api_fastbull.logic.comment import nonce
from CompanyProject.Fastbull.Api_fastbull.logic.conftest import generate_sign_login, generate_token, get_identity, \
    timestamp, generate_nonce
from CompanyProject.Fastbull.Api_fastbull.testcases.conftest import common_data
# nonce = generate_nonce()
url='https://testfbapi.tostar.top/fastbull-quotes-service/api/postSnapshotByIds'
data = {
  "needDetail": True,
  "stockIds": [
    "7300_A"
  ],
  "isDetail": True
}
headers={
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
    "beta": "true",
    "btoken": "17344adea43d8262befa394ab296e6b7",
    "client-type": "4",
    "clientversion": "latest",
    "content-type": "application/json",
    "deviceid": "6926c70151a9ab929aa533f31db08fe2",
    "deviceno": "6926c70151a9ab929aa533f31db08fe2",
    "langid": "实例25_批量生成PPT版荣誉证书",
    "nonce": "nqznxnkU",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sign":  generate_sign_login(common_data['uid'], generate_token(get_identity()), timestamp, nonce),
    "timestamp": "1709628304",
    "uid": "412968"
  }
# headers={
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
#     "beta": "true",
#     "btoken": "17344adea43d8262befa394ab296e6b7",
#     "client-type": "4",
#     "clientversion": "latest",
#     "content-type": "application/json",
#     "deviceid": "6926c70151a9ab929aa533f31db08fe2",
#     "deviceno": "6926c70151a9ab929aa533f31db08fe2",
#     "langid": "实例25_批量生成PPT版荣誉证书",
#     "nonce": nonce,
#     "sec-ch-ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "sign": generate_sign_login(common_data['uid'], generate_token(get_identity()), timestamp, nonce),
#     "timestamp": timestamp
#   }
res=requests.post(url,headers=headers,data=data).json()
print(res)