import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get('http://the-internet.herokuapp.com/tinymce')

time.sleep(3)
# d.Webdriverwait(10)
d.switch_to.frame('mce_0_ifr')
# a=d.find_element(By.ID,'tinymce').send_keys('内容')
a=d.find_element(By.XPATH,'//*[@id="tinymce"]/p').clear()
a=d.find_element(By.XPATH,'//*[@id="tinymce"]/p').send_keys('内容')


