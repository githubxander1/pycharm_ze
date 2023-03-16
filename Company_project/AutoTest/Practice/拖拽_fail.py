import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get('http://the-internet.herokuapp.com/drag_and_drop')

source1=d.find_element(By.ID,'column-a')
target1=d.find_element(By.ID,'column-b')
ActionChains(d).drag_and_drop(source1,target1).perform()

time.sleep(3)
# d.close()
