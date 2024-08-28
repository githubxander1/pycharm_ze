import pandas as pd
import requests
from lxml import etree
from pyecharts.charts import Bar
'''
知识点“
    实例25_批量生成PPT版荣誉证书.python数据类型：
    str
    content.decode()
    2.
'''
sourse=requests.get('https://bj.lianjia.com/ershoufang/c1111027381003/').content.decode()
html=etree.HTML(sourse)
# print(sourse)
# 解析数据
home_list=html.xpath("//div[@class='info clear']")
ershoufang=[]
for home in home_list:
    name=home.xpath('./div/a/text()')[0]
    price=home.xpath('.//div[@class="unitPrice"]/span/text()')[0].replace(',','').replace('元/平','')
    # print(price)
    ershoufang.append([name,price])
# print(ershoufang)
table=pd.DataFrame(ershoufang,columns=['小区','单价(元/平)'])
print(table)
bar=Bar()
bar.add_xaxis(list(table['小区']))
bar.add_yaxis('单价(元/平)',table['单价(元/平)'].tolist())
bar.render('链家二手房.html')