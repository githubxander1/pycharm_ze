from urllib import request
from fake_useragent import UserAgent

ua=UserAgent()
print(ua.chrome)
print(ua.firefox)

url='http://httpbin.org/get'
# #UA在线识别工具： https://useragent.buyaocha.com/
headers = {
# # 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
# 'User-Agent':'{}'.format(ua)}
# 'User-Agent':f'{ua}'}
'User-Agent':'%s'% ua}
# # 1、创建请求对象，包装ua信息
res=request.Request(url,headers=headers)
response=request.urlopen(res)
html=response.read().decode('utf-8')
print(html)
