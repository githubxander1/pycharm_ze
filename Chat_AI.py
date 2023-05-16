import requests

url='http://lemurchat.anfans.cn/api/chat/conversation-trial'
# data={
# 	"messages":"[
#                 {"content":"",
#                 "id ":"",
#                 "LEMUR_AI_SYSTEM_SETTING ":"",
#                 "isSensitive ":"false",
#                 "needCheck ":"false",
#                 "role ":"system "},
#                 {"content ":"linshiyou.com ",
#                  "isSensitive ":"false",
#                  "needCheck ":"true",
#                  "role ":"user "},
#                 {"content ":"UI自动化测试主流设计模式， 并案例讲解一下 ",
#                  "isSensitive ":"false",
#                  "needCheck ":"true",
#                  "role ":"user "},
#                 {"content ":"192 ",
#                  "isSensitive ":"false",
#                  "needCheck ":"true",
#                  "role ":"user "},
#                 {"content ":"UI自动化测试主流设计模式， 案例讲解一下 ",
#                  "isSensitive ":"false",
#                  "needCheck ":"true",
#                  "role ":"user"}]"
#     }
data='messages=[{"content":"","id":"LEMUR_AI_SYSTEM_SETTING","isSensitive":false,"needCheck":false,"role":"system"},{"content":"linshiyou.com","isSensitive":false,"needCheck":true,"role":"user"},{"content":"UI自动化测试主流设计模式，并案例讲解一下","isSensitive":false,"needCheck":true,"role":"user"},{"content":"192","isSensitive":false,"needCheck":true,"role":"user"},{"content":"UI自动化测试主流设计模式，案例讲解一下","isSensitive":false,"needCheck":true,"role":"user"},{"content":"你好","isSensitive":false,"needCheck":true,"role":"user"}]'
r=requests.post(url,json=data)
print(r)

# data1={
#     "messages":["{"content":"","id":"LEMUR_AI_SYSTEM_SETTING","isSensitive":"false","needCheck":"false","role":"system"},
#                     {"content":"linshiyou.com ","isSensitive":"false","needCheck":"true","role":"user"},
#                     {"content":"UI自动化测试主流设计模式， 并案例讲解一下","isSensitive":"false","needCheck":"true","role ":"user "},
#                     {"content ":"192 ","isSensitive ":"false","needCheck ":"true","role ":"user "},
#                     {"content ":"UI自动化测试主流设计模式， 案例讲解一下 ","isSensitive ":"false","needCheck ":"true","role ":"user "}"
#         }