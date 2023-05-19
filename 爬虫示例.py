import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_list = soup.find_all('div', class_='billboard-bd')[0].find_all('li')

for movie in movie_list:
    name = movie.find_all('a')[0].text.strip()
    release_info = movie.find_all('p')[0].text.strip()
    rating_info = movie.find_all('p')[1].text.strip()
    print(name)
    print(release_info)
    print(rating_info + '\n')