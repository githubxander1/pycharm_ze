import time
from appium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By

device={}
device['platformName']='Android'
device['platformVersion']='7.1.2'
device['deviceName']='127.0.0.1:21513 device'
# device['appPackage']='com.lemon.lv'
# device['appActivity']='com.vega.main.MainActivity'
device['appPackage']='com.brokersview.official'
device['appActivity']='com.bv.official.main.splash.SplashActivity'

d=webdriver.Remote('127.0.0.1:4723/wd/hub',device)
time.sleep(3)
d.find_element(By.ID,'com.brokersview.official:id/tv_confirm').click()

