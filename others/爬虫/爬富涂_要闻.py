import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 发送请求
response = requests.get(
    'https://news.futunn.com/main?lang=zh-cn&global_content=%7B%22promote_id%22%3A13766,%22sub_promote_id%22%3A3%7Dts',
    headers=headers)

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 定位class=market-wrap的div标签
market_wrap = soup.find('div', class_='market-wrap')

# 提取class="market-item__title"的h2标签的文本内容
title = market_wrap.find('h2', class_='market-item__title').text.strip()
print(f"提示词标题: {title}")

# 提取div标签里面所有的a标签的href链接和文本内容
links = market_wrap.find_all('a')
link_addresses = [link.get('href') for link in links]
link_texts = [link.text.strip() for link in links]
print(f"链接地址: {link_addresses}")
print(f"链接文本: {link_texts}")

# 提取class="footer-source"或class="footer-topic"的span标签的文本内容
source = market_wrap.find('span', class_='footer-source').text.strip()
topic = market_wrap.find('span', class_='footer-topic').text.strip()
print(f"提示词来源: {source}")
print(f"提示词主题: {topic}")

# 提取class="footer-time"的span标签的全部文本内容
time_info = market_wrap.find('span', class_='footer-time').text.strip()
print(f"提示词时间: {time_info}")

# 创建DataFrame
data = {
    '提示词：标题': [title],
    '链接地址': link_addresses,
    '提示词：来源': [source],
    '提示词：时间': [time_info]
}
df = pd.DataFrame(data)

# 将数据写入Excel文件
df.to_excel(' 提示词.xlsx', index=False)

print("数据已成功写入Excel文件。")