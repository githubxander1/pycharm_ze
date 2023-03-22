"""1base.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
from selenium.webdriver.support.wait import WebDriverWait
import time


class Base:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 获取value属性方法
    def base_get_value(self, loc):
        return self.base_find_element(loc).get_attribute("value")

    def base_get_img(self):
        self.driver.get_screenshot_as_file("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))