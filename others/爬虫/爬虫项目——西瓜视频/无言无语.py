import requests
from lxml import etree
from fake_useragent import UserAgent
ua=UserAgent()
headers={
    'User-Agent':ua.random
}

def get_text(times):
    count=0
    while True:
        with open('污言污语.txt','a',encoding='utf-8') as f:
            sourse=requests.get('https://www.nihaowua.com/',headers=headers).text
            html=etree.HTML(sourse)

            data=html.xpath('//section/div/*/text()')[0]

            f.write(data+'\n')
            count+=1
            print(f'正在抓取，第{count}次，内容为：{data}')
            if count==times:
                break
get_text(10)