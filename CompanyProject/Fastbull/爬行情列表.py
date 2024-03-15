import requests
from lxml import etree

sourse=requests.get('https://beta.fastbull.com/cn/market/stocks/all-all_106').text#股票
html=etree.HTML(sourse)

count=0
quotation_list=html.xpath('//div[@class="module_wrap module_wrap_functional"]/div[2]')
for quotation in quotation_list:
    # title = quotation.xpath('//span/a[@class="ltr_ar_dir"]/text()')
    # tubiao = quotation.xpath('//*[@class="ltr_ar_dir openchart-btn"]/text()')
    title_name = quotation.xpath('.//a/text()')
    for title in title_name:
        pass
        # print(title)
    # sub_title = quotation.xpath('.//h2[@class="sub-title"]/text()')
    # one_ellipsis = quotation.xpath('.//span[@class="one_ellipsis"]/text()')
    # lastest_price_denkuan_risecolor = quotation.xpath('.//span[contains(@class,"lastest-price")]/text()')
    # change_percent_denkuan_fallcolor = quotation.xpath('.//span[@class="change-percent denkuan fallcolor"]/text()')
    # # print(lastest_price_denkuan_risecolor)
    # # print(change_percent_denkuan_fallcolor)
    # print(one_ellipsis)
    # print(title)

    # for i in lastest_price_denkuan_risecolor:
    #     print(i)
    #     count += 1
    #     print(f"记录 {count + 1}: {i}")

    # print(one_ellipsis)
    # for items in one_ellipsis:
    # 打印one_ellipsis并显示当前记录数
    #     print(f"记录 {count + 1}: {items}")
    count += 1

# 最后打印总数
print(f"\n共抓取到 {count} 条记录")
