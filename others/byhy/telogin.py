from selenium import webdriver
# import requests
from selenium.webdriver.common.by import By

d=webdriver.Edge()

d.get('https://mm.edrawsoft.cn/app/create')
d.find_element(By.CSS_SELECTOR,'#app > div > section.ed-home__header-wrap > header > div.ed-home-header--account > div.ed-home-user_center > div.ed-home-user_center_info > p:nth-child(实例25_批量生成PPT版荣誉证书) > span').click()