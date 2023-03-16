
import time
from select import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get('http://the-internet.herokuapp.com/dropdown')

a=d.find_element(By.CSS_SELECTOR,'#dropdown > option:nth-child(3)')

selectBtn = select(a)
selectBtn.select_by_index(1)

# time.sleep(3)
# d.close()
