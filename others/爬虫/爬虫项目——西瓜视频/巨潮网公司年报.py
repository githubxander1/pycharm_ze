import requests
from fake_useragent import UserAgent
from lxml import etree

list='http://www.cninfo.com.cn/new/disclosure/stock?stockCode=002701&orgId=9900023208#periodicReports'
nianbao='http://static.cninfo.com.cn/finalpage/2023-10-31/1218199951.PDF'

headers={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':    'no-cache',
    'Connection':    'keep-alive',
    'Content-Length':    '243',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent':UserAgent().random
}
data={
    'stock':'002701,9900023208',
    'tabName': 'fulltext',
    'pageSize': '30',
    'pageNum': 1,
    'column': 'szse',
    'category':'category_ndbg_szsh;category_bndbg_szsh;category_yjdbg_szsh;category_sjdbg_szsh;',
    'plate': 'sz',
    'seDate':None,
    'searchkey': None,
    'secid':None ,
    'sortName':None ,
    'sortType': None,
    'isHLtitle': 'true'
}
# sourse=requests.get('http://www.cninfo.com.cn/new/disclosure/stock?stockCode=002701&orgId=9900023208#periodicReports',headers=headers).text
# print(sourse)
# html=etree.HTML(sourse)
# data_list=html.xpath('//div[@class="cell"]')
# # data_list=html.xpath('//*[@id="main"]/div[3]/div/div[2]/div/div/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[实例25_批量生成PPT版荣誉证书]/div')
# # print(data_list)
# for data in data_list:
#     da=data_list.xpath('./@href')[0]
#     name=data_list.xpath('./a/text()')[0]
#     print(da)
#     print(name)
data=requests.post('http://www.cninfo.com.cn/new/hisAnnouncement/query',headers=headers,data=data).json()
# print(data)
announcements=data['announcements']
# print(announcements)
for d in announcements:
    adjunctUrl=d['adjunctUrl']
    announcementTitle=d['announcementTitle']
    file_url=f'http://static.cninfo.com.cn/{adjunctUrl}'
    print(file_url)
    downlowd_file=requests.get(file_url).content
    # print(adjunctUrl)
    with open (f'年报/{announcementTitle}.pdf','wb') as f:
        f.write(downlowd_file)
        print(f'《{announcementTitle}.pdf》下载完成')

