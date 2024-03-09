import time

import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# ua=UserAgent()

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    # 'User-Agent':ua.random
}
# print(headers)
def get_movie_info(url):
    try:
        res=requests.get(url,headers=headers)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f'请求失败:{e}')
        return None
    sourse=requests.get(url,headers=headers).text
    # print(sourse)
    soup=BeautifulSoup(sourse,'html.parser')
    all=soup.find_all('div',class_='hd')
    for i in all:
        link=i.find('a',href=True).get('href')
        name=i.find('span',class_='title').text
        return '电影名称：{}，链接：{}'.format(name,link)
start=0
filter_value='all'
while start < 1000:
    url =f'https://movie.douban.com/top250?start={start}'
    movie_info=get_movie_info(url)
    if movie_info:
        print(movie_info)
    else:
        print('爬取失败')
    start +=25
    time.sleep(1)