import time
from appium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By

device={}
device['platformName']='Android'
device['platformVersion']='7.1.2'
# device['deviceName']='127.0.0.1:21513 device'
device['deviceName']='5ENDU18C21003487        device'
device['appPackage']='com.sy.fxchat'
device['appActivity']='com.sy.flutter_huiliao.MainActivity'

d=webdriver.Remote('127.0.0.1:4723/wd/hub',device)
time.sleep(2)
# d.find_element(By.ACCESSIBILITY_ID,'邮箱/汇聊号/手机号').click()
d.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="邮箱/FXID/手机号"]').click()
d.find_element(By.NAME,'邮箱/FXID').send_keys('1627670595@qq.com')
d.find_element(By.NAME,'密码').send_keys('txj123456')
next=d.find_element(By.CLASS_NAME,'android.widget.ImageView')
next.pop(6).click()
time.sleep(3)
# d.find_element(By.XPATH,'//android.view.View[@content-desc="手机号 第 2 个标签，共 2 个"]').click()
# d.find_element(By.XPATH,'//android.view.View[@content-desc="登录"]/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText').send_keys()
# d.find_element(By.ANDRIOD_UIAUTOMATOR('newUiSelector().text("邮箱/汇聊号")').send_keys(7863192)
# d.find_element(By.CSS_SELECTOR,'#sourceContainer > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li > ul > li:nth-child(2) > ul > li:nth-child(2) > ul > li > ul > li > ul > li:nth-child(1) > span.ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal.ant-tree-node-selected > span > span > b').send_keys(7863192)
# d.find_element(By.NAME,'密码').send_keys('a1234567')
# d.find_element(By.NAME,'5').click()
