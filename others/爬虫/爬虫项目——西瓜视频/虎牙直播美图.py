import requests
from lxml import etree
'''
解析：
    html.xpath()
'''
sourse=requests.get('https://www.huya.com/g/2168').text
# print(sourse)
html=etree.HTML(sourse)
pic_list=html.xpath("//img[@class='pic']")
# 循环获取图片
for pic in pic_list:
    # 图片路径
    pic_src=pic.xpath('./@data-original')[0]
    big_pic_src=pic_src.split('?')[0]
    # 名称
    name=pic.get('alt')
    # 保存图片
    imgs=requests.get(big_pic_src)
    with open("./imgs/%s.jpg"%name,'wb') as f:
        f.write(imgs.content)
    # print(pic_src)
    print('<%s>保存成功'%name)