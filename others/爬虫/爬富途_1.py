import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 目标URL
url = "https://news.futunn.com/main?lang=zh-cn&global_content=%7B%22promote_id%22%3A13766,%22sub_promote_id%22%3A3%7Dts"

# 自定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 发送请求
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("网页请求成功")
else:
    print(f"网页请求失败，状态码：{response.status_code}")
    exit()

# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 定位元素
items = soup.find_all('div', class_='market-wrap')
# print(items)
if items:
    print("找到目标div元素")

    # 准备数据存储
    data = []

    counter = 1  # 初始化计数器
    for wrap_div in items:
        # 直接在market-wrap下找所有的a标签，这些a标签代表每个新闻条目
        news_items = wrap_div.find_all('a', class_='market-item list-item')
        for news_item in news_items:
            title = news_item.find('h2', class_='market-item__title')
            link = news_item.get('href')  # 直接从当前a标签获取链接
            source = news_item.find(class_='footer-source') or news_item.find(class_='footer-topic')
            timestamp = news_item.find(class_='footer-time')

            if title and source and timestamp:
                # 提取并清理数据
                title_text = title.text.strip()
                link_text = link
                source_text = source.text.strip()
                timestamp_text = timestamp.text.strip()

                # 打印或存储每条新闻的详细信息
                print(f"{counter}. 标题：{title_text}")
                counter += 1  # 每处理完一条新闻，计数器加1
                # print(f"标题：{title_text}")
                print(f"链接地址：{link_text}")
                print(f"来源：{source_text}")
                print(f"时间：{timestamp_text}")

                # 将数据按字段分类并添加到data列表
                data.append({
                    '序号': counter - 1,  # 因为counter已经加1，所以这里减1以保持准确性
                    '标题': title_text,
                    '链接地址': link_text,
                    '来源': source_text,
                    '时间': timestamp_text
                })

        # 数据提取完成后，data列表将包含所有条目的分类数据
    # print(data)
#
    # 写入Excel
    df = pd.DataFrame(data, columns=['序号','标题', '链接地址', '来源', '时间'])

    # 在D盘创建Excel文件
    excel_path = '富途_要闻.xlsx'
    df.to_excel(excel_path, index=False)
    print(f"数据已保存至：{excel_path}")
else:
    print("未找到目标div元素")

# 延迟请求，避免频繁访问
time.sleep(2)  # 延时2秒，可根据需要调整
