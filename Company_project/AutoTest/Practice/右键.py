from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get('http://the-internet.herokuapp.com/context_menu')

#1。先定位到该元素
a=d.find_element(By.ID,'hot-spot')
#2.ActionChains类，执行右键
ActionChains(d).context_click(a).perform()

time.sleep(3)
d.switch_to.alert.accept()


d.close()
