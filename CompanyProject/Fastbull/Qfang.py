import requests
from bs4 import BeautifulSoup
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    # 'User-Agent':ua.random
}
sourse=requests.get('https://m.qfang.com/shenzhen/sale',headers=headers).text#股票
html=etree.HTML(sourse)

# count=0
# quotation_list=html.xpath('//div[@class="house-list"]')
# for quotation in quotation_list:
#     # title = quotation.xpath('//span/a[@class="ltr_ar_dir"]/text()')
#     # tubiao = quotation.xpath('//*[@class="ltr_ar_dir openchart-btn"]/text()')
#     title_name = quotation.xpath('.//h3[@class="tit twoline-ellips"]/text()')
#     for title in title_name:
#         print(title)

soup=BeautifulSoup(sourse,'lxml')
quotation_list=soup.find_all('div',class_='house-list')
for quotation in quotation_list:
    title_name=quotation.find('h3',class_='tit twoline-ellips').text
    print(title_name)