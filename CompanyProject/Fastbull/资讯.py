import requests
from lxml import etree

import requests

params = {
    'r': '0.776842234943709',
    'stockId': '7200_MSFT',
    'pageSize': '60',
}

sourse = requests.get('https://api.fastbull.com/fastbull-news-service/api/findQuotesNewsByStockId', params=params)
# sourse=requests.get('https://beta.fastbull.com/cn/quotation-detail/7200_MSFT').text
print(sourse)
# html=etree.HTML(sourse)

# new_name=html.xpath('//p[@class="news_name"]/text()')
# print(new_name)