import requests
from bs4 import BeautifulSoup

url = "https://weread.qq.com/"

# 发起GET请求获取页面内容
response = requests.get(url)

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(response.text, 'html.parser')

# 在页面中找到所有书籍的信息

books = soup.find_all('div', class_='ranking_block_book')
for book in books:
    title = book.find('div', class_='ranking_block_book_title_text').text.strip()
    author = book.find('a', class_='ranking_block_book_author').text.strip()
    print('书名：', title)
    print('作者：', author)