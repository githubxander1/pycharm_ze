import requests
from lxml import etree

sourse=requests.get('https://beta.fastbull.com/cn/market').text
html=etree.HTML(sourse)

count=0
quotation_list=html.xpath('//div[@class="quotation-body"]')
for quotation in quotation_list:
    title = quotation.xpath('.//span[@class="title"]/text()')
    sub_title = quotation.xpath('.//h2[@class="sub-title"]/text()')
    one_ellipsis = quotation.xpath('.//span[@class="one_ellipsis"]/text()')
    lastest_price_denkuan_risecolor = quotation.xpath('.//span[contains(@class,"lastest-price")]/text()')
    change_percent_denkuan_fallcolor = quotation.xpath('.//span[@class="change-percent denkuan fallcolor"]/text()')
    # print(lastest_price_denkuan_risecolor)
    # print(change_percent_denkuan_fallcolor)
    print(one_ellipsis)
    print(title)

    # for i in lastest_price_denkuan_risecolor:
    #     print(i)
    #     count += 实例25_批量生成PPT版荣誉证书
    #     print(f"记录 {count + 实例25_批量生成PPT版荣誉证书}: {i}")

    # print(one_ellipsis)
    # for items in one_ellipsis:
    # 打印one_ellipsis并显示当前记录数
    #     print(f"记录 {count + 实例25_批量生成PPT版荣誉证书}: {items}")
    count += 1

# 最后打印总数
print(f"\n共抓取到 {count} 条记录")
    # print(title)
    # print(sub_title)
