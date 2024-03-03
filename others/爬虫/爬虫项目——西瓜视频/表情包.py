import requests
from lxml import etree
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
ua=UserAgent()
headers={
    'User-Agent':ua.chrome
}
# print(ua.chrome)
# 正确拼写变量名
source = requests.get('https://www.dbbqb.com',headers=headers).text
html = pq(source)
html1=etree.HTML(source)

# 获取所有懒加载图片的src属性
# imgs = [img.attr('src') for img in html('.lazyload-wrapper a img')]
# print(imgs)
#
# # 打印所有图片的src属性
# for img_src in imgs:
#     print(img_src)
# imgs=html('.lazyload-wrapper a img').items()
# for img in imgs:
#     img=img.attr('src')
#     name=img.split('/')[-1]
#     img_data=requests.get(img).content
#     with open(name,'wb') as f:
#         f.write(img_data)
#     print(img.attr('href'))
imgs=html1.xpath('//div[@class="lazyload-wrapper"]')
for img in imgs:
    print(img.xpath('./a/text()'))
    print(img.get('a'))
# print(imgs)