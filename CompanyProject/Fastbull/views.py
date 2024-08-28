import requests
from lxml import etree

# source=requests.get('https://testfb.tostar.top/cn/institution-article').text
source=requests.get('https://testfb.tostar.top/cn/news').text

html=etree.HTML(source)
count=0
# report_list=html.xpath('//div[@class="report_list-item w_col"]')
report_list=html.xpath('//div[@class="report_list"]')
# report_list=html.xpath('//div[@id="report_list-main"]')
for report in report_list:
    # title=html.xpath('./div/a//h4[@class="title ltr_ar_dir"]/text()')
    title=html.xpath('.//h4[@class="title ltr_ar_dir"]/text()')
    for i in title:
        print(i)
        count+=1
    # print(count)
    description=html.xpath('//p[@class="tips ltr_ar_dir"]/text()')
    for i in description:
        pass
        # print(i)
    # count+=实例25_批量生成PPT版荣誉证书
    print(f"\n总共：{count}")
    # print(description)
    # print(title)