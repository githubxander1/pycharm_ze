import base64
import io
import json
# import pandas as pd
import os
import re

import requests
from bs4 import BeautifulSoup


class AVSpider():
    def __init__(self):
        # self.url='https://www.b413d2c808c9.com/page/tupian/25'
        self.url='https://www.b413d2c808c9.com/s/chapter/tupian/20/427781'
        self.userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

    # https: // www.b413d2c808c9.com / s / chapter / tupian / 20 / 428525
    # https: // www.b413d2c808c9.com / s / chapter / tupian / 20 / 428524
    # https: // www.b413d2c808c9.com / s / chapter / tupian / 20 / 428523
    # 1.  请求函数，得到页面
    def get_html(self,url):
        req=requests.get(url,headers={'User-Agent':self.userAgent})
        return req.content

    # 2. 解析函数，得到数据
    def parse_html(self,html):
        soup = BeautifulSoup(html, 'html.parser')

        # 找到目标div标签
        # div = soup.find('div', class_='grid ffb525d39e f27ae460cd')
        div = soup.find('div', class_='mw1100 mt20')

        # 找到特定div下的所有img标签
        # 构建一个正则表达式来匹配div下img的src属性
        # 假设img标签的src属性在src="..."格式
        regex_src = re.compile(r'src="([^"]+)"')
        # 查找div下所有的img标签
        imgs = div.find_all('img')
        # 下载所有匹配的图片
        for img in imgs:
            src = img.get('src')
            if src:
                # 如果src是Base64编码，解码然后保存
                if src.startswith('data:image/'):
                    pass
                    # 分割数据URIscheme
                    # scheme, media_type, encoded_string = src.split(',', 2)
                    # # 解码Base64
                    # decoded_string = base64.b64decode(encoded_string)
                    # # 创建一个BytesIO对象，将其保存为文件
                    # with io.BytesIO(decoded_string) as image_io:
                    #     image = Image.open(image_io)
                    #     image.save('downloaded_image.jpg')  # 或者其他您想保存的文件名
                else:
                    # 如果不是Base64，则可以直接下载
                    response = requests.get(src)
                    with open('downloaded_image.jpg', 'wb') as file:
                        file.write(response.content)  # 或者根据实际情况调整文件名和保存路径

        # 创建一个目录来保存下载的图片
        # if not os.path.exists('downloaded_images'):
        #     os.makedirs('downloaded_images')

        # 遍历img标签并下载图片
        # for img in img_tags:
        #     img_url = img.get('src')
        #
        #     # 确保有src属性
        #     if img_url:
        #         # 图片内容
        #         img_data = requests.get(img_url).content
        #         print(img_data)

                # 图片名字
                # filename = os.path.join('downloaded_images', img_url.split('/')[-1])

                # 保存图片
                # with open(filename, 'wb') as file:
                #     file.write(img_data)
                #     print(f'Downloaded {filename}')

    # 3.保存文件函数
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)


if __name__ == '__main__':
    spider=AVSpider()
    spider.get_html(spider.url)
    spider.parse_html(spider.get_html(spider.url))
    # spider.save_html('av.html',spider.get_html(spider.url))