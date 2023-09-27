from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get('https://letcode.in/draggable')
driver.implicitly_wait(10)

drag_element=driver.find_element(By.CSS_SELECTOR,'#sample-box')

ActionChains(driver).click_and_hold(drag_element).move_by_offset(150,0).release().perform()