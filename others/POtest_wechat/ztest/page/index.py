from selenium import webdriver
from selenium.webdriver.common.by import By
import base
import os
os.path
d=webdriver.Edge()

class index:
    def goto_login(self):
        d.get('https://work.weixin.qq.com')
        d.find_element(By.CSS_SELECTOR,'#indexTop > div.index_top_inside > aside > a.index_top_operation_loginBtn').click()

    def goto_register(self):
        d.find_element(By.CSS_SELECTOR,'#tmp > div.index_head_info > a').click()
