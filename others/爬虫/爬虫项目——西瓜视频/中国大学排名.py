import requests
from lxml import etree

try:
    sourse=requests.get('https://www.shanghairanking.cn/rankings/bcur/2023').content.decode('utf-8')
    html=etree.HTML(sourse)
except Exception as e:
    print(e)

def fetch():
    # school_list=html.xpath('//table[@class="rk-table"]')
    school_list=html.xpath('//tbody/tr')
    count=0
    for i in school_list:
        cn_name=i.xpath('.//a[@class="name-cn"]/text()')[0].strip()
        en_name=i.xpath('.//a[@class="name-en"]/text()')[0].strip()
        tags=i.xpath('.//p[@class="tags"]/text()')[0].strip()
        address=i.xpath('./td[3]/text()')[0].strip()
        ranking=i.xpath('.//div[contains(@class,"ranking")]/text()')[0].strip()
        score=i.xpath('./td[5]/text()')[0].strip()
        # print(cn_name)
        # print(tags)
        # print(en_name)
        # print(address)
        # print(ranking)
        print(score)
        count+=1
    print(f"总共数据：{count}")

