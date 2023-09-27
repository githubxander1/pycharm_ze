from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

d=webdriver.Edge()
d.get('https://www.baidu.com')
d.implicitly_wait(10)