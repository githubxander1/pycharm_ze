import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get('http://the-internet.herokuapp.com/entry_ad')
# d.find_element(By.ID,'modal')
time.sleep(2)
# d.find_element(By.CSS_SELECTOR,'#modal > div.modal > div.modal-footer > p').click()
# d.switch_to.alert.accept()
