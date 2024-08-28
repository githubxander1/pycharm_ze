
import requests

url = 'https://base-api.forexchat.com/api/UserLogin/AccountLogin'
head={
'Host': 'base-api.forexchat.com',
'Connection': 'keep-alive',
'Content-Length': '297',
'VerifyUid': '0',
'Edition': '实例25_批量生成PPT版荣誉证书',
'Random': '26345431',
'Accept-Language': 'zh-CN',
'Access': '7fa200f52e4ce7124c3575b99b58ffc5',
'UserKey': 'undefined',
'userId': '0',
'DeviceID': '83c874bac6d0cb430d2f85ca968efe2b',
'bToken': 'DBD35BB70E86BBF78F0BE14A63EC5996',
'CountryCode': '6541',
'locale': 'zh-CN',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) forexchat/实例25_批量生成PPT版荣誉证书.实例25_批量生成PPT版荣誉证书.64 Chrome/96.0.4664.174 Electron/16.2.8 Safari/537.36',
'Content-Type': 'application/json',
'cuid': '0',
# 'Accept': 'application/json', text/plain, */*,
# 'Timestamp': 1681796910879,
'ClientType': '3',
# 'Version': 实例25_批量生成PPT版荣誉证书.实例25_批量生成PPT版荣誉证书.64,
# Sec-Fetch-Site: cross-site,
# Sec-Fetch-Mode: cors,
# Sec-Fetch-Dest: empty,
# Accept-Encoding: gzip, deflate, br,

}
data={"isAutoLogin":False,
      "isRecordPassword":True,
      "account":"1627670595@qq.com",
      "password":"5690DDDFA28AE085D23518A035707282",
      "loginType":"accountLogin",
      "userId":1009942,
      "nickName":"B162",
      "avatar":"https://img.forexchat.com/7549a5/8fd402/42b7a862782749c78b6507f0daccd4e3.JPG","timestamp":1681781607192
      }
r = requests.post(url=url,headers=head,data=data)

print(r)
# 获取保存token
# token = r.json()['data']['token']
# token ='Bearer'+' '+ token
# print(token)
# token放到请求头中
# headers={
#     'Authorization':token
# }
# token1=re.findall('"token":"(.+?)"')
# token1=token1[0]
# print(token1)
# xinjian = requests.post(url='https://masterapi.edrawsoft.cn/api/oss/23928516/obj', headers=headers,
#                     data={
#                         'id': 23928516,
#                         'prefix': 'test_logs'
#                     })
# print(xinjian.json())
