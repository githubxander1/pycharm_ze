import urllib.request
import random

url = 'http://www.baidu.com'
# 方法1，模拟请求头,字典
# 常见请求头https://blog.csdn.net/mouday/article/details/80182397   https://www.cnblogs.com/zrmw/p/9332801.html
headers = {
    'Accept': 'application/json,application/javascript,*/*;q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
}
# 设置一个请求体
req = urllib.request.Request(url, headers=headers)
# 发起请求
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
# print(type(data)) # <class 'str'>
# print(data) # 打印出来的就是百度首页的内容

# 方法2
agentList = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.实例25_批量生成PPT版荣誉证书 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.实例25_批量生成PPT版荣誉证书; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.实例25_批量生成PPT版荣誉证书 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
]
agentStr = random.choice(agentList)  # 随机拿一个
# print(agentStr)
req = urllib.request.Request(url)
req.add_header('User-Agent', agentStr)  # 逗号，不是冒号
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
print(type(data))
print(data)