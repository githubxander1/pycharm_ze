import time
from appium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By

device={}
device['platformName']='Android'
device['platformVersion']='7.1.2'
device['deviceName']='127.0.0.1:21513 device'
device['appPackage']='com.lemon.lv'
device['appActivity']='com.vega.main.MainActivity'

d=webdriver.Remote('127.0.0.1:4723/wd/hub',device)
time.sleep(2)

# d.close_app()
# d.install_app(r'C:\Users\Admin\Desktop\1base(4).apk')
# 同意
d.find_element(By.ID,'com.lemon.lv:id/privacy_ok').click()
time.sleep(3)
d.find_element(By.ID,'com.lemon.lv:id/confirm_ok').click()
time.sleep(3)
d.find_element(By.ID,'com.lemon.lv:id/begin_edit_text_view').click()
# d.find_element(By.NAME,'开始创作').click()
# d.find_element(By.CSS_SELECTOR,'#sourceContainer > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li:nth-child(3) > ul > li > ul > li:nth-child(5) > ul > li > span.ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal.ant-tree-node-selected > span > span > b').click()
# d.find_element(By.ID,'com.lemon.lv:id/confirm_ok').click()
# d.find_element(By.ACCESSIBILITY_ID,'照片').click()
# d.find_element(By.RESOURCE_ID,'com.lemon.lv:id/backPic').click()
