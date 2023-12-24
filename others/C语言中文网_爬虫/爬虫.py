import requests
from bs4 import BeautifulSoup
url='http://www.cntour.cn/'
# 为避免被封 IP，在数据采集时经常会使用代理
proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
# strhtml=requests.get(url,proxies=proxies)
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data=soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
print(data)
# 清洗数据
import re
for item in data:
    result={
        "title":item.get_text(),
        "link":item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }
# print(result)