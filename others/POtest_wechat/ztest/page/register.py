from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Register:
    def register(self):
        d=webdriver.Edge()
        d.get('https://work.weixin.qq.com')
        d.find_element(By.ID,'corp_name').send_keys('名称')
        # 选择框
        sel1=d.find_element(By.CSS_SELECTOR,'#corp_industry > a')
        Select(sel1).select_by_value('教育').click()
        d.find_element(By.CSS_SELECTOR,'#corp_industry > div > table > tbody > tr > td:nth-child(2) > div:nth-child(7) > div:nth-child(1) > a > span').click()
