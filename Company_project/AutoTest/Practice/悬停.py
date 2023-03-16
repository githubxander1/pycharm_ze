import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d=webdriver.Chrome()

d.get('http://the-internet.herokuapp.com/')
d.find_element(By.CSS_SELECTOR,'#content > ul > li:nth-child(9) > a').click()
ele=d.find_element(By.CSS_SELECTOR,'#content > div > ul > li:nth-child(2) > a')
ActionChains(d).move_to_element(ele).perform()

time.sleep(3)
d.close()