
import requests

url='https://group-api.forexchat.com/api/member/updateNickName?groupId=BAF31C32-DAD0-4BA1-A399-0EEFC9CFF99D&groupNickname=162%E7%BE%A4%E6%98%B5%E7%A7%B0&userId=1009942&optUserId=1009942'

r=requests.put(url)
print(r)