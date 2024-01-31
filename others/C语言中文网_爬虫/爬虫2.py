import json
# import pandas as pd
import requests
from bs4 import BeautifulSoup


class AVSpider():
    def __init__(self):
        self.url='https://www.ldstv-0108.com:2083/video/52'
        self.userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

    # 1.  请求函数，得到页面
    def get_html(self,url):
        req=requests.get(url,headers={'User-Agent':self.userAgent})
        return req.content

    # 2. 解析函数，得到数据
    def parse_html(self,html):
        soup = BeautifulSoup(html, 'html.parser')
        # 找到所有class为"row col5 clearfix"的div元素
        list_items = soup.find_all('div', class_="row col5 clearfix")

        for item in list_items:
            dl_tags = item.find_all('dl')

            for dl in dl_tags:
                # 获取链接
                link = dl.find('dd').find('a')['href']
                # 获取标题（这里假设标题是"data-tip"属性中的加密内容，实际请根据网页实际情况处理）
                title_data_tip = dl.find('dd').find('a').find('h3').text
                # 解密title（此处仅为示例，实际解密方式取决于网站实际加密规则）
                # 注意：这段解密逻辑需要根据实际网站的数据加密方式来实现，以下为模拟解密过程
                title = title_data_tip  # 在这里插入解密函数或逻辑以获取真实标题

                # 获取封面图片URL
                img_url = dl.find('dt').find('img')['data-original']

                baseurl='https://www.ldstv-0108.com:2083'
                print(f'链接: {baseurl}{link}')
                print(f'标题: {title}')
                print(f'封面图片URL: {img_url}\n')

                # # 创建DataFrame并设置列名
                # data = {'链接': links, '标题': titles}
                # df = pd.DataFrame(data)
                #
                # # 输出表格样式
                # print(df.to_string(index=False))

    # 3.保存文件函数
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)


if __name__ == '__main__':
    spider=AVSpider()
    spider.get_html(spider.url)
    spider.parse_html(spider.get_html(spider.url))
    # spider.save_html('av.html',spider.get_html(spider.url))