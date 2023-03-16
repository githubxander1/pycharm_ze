import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d=webdriver.Chrome()

d.get('http://the-internet.herokuapp.com/dynamic_content')

a=d.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/text()')

print(a)