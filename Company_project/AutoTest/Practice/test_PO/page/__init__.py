"""__init__.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
from selenium.webdriver.common.by import By

"""以下为服务器域名配置地址"""
url = "http://cal.apple886.com/"

"""以下为登录页面配置信息"""
# cal_num = By.CSS_SELECTOR,"#simple"
cal_add = By.CSS_SELECTOR, "#simpleAdd"
cal_eq = By.CSS_SELECTOR, "#simpleEqual"
cal_result = By.CSS_SELECTOR, "#resultIpt"
cal_clear = By.CSS_SELECTOR, "#simpleClearAllBtn"