"""page_cal.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
from time import sleep

from PO import page
from PO.base.base import Base
from selenium.webdriver.common.by import By


class PageCal(Base):
    def page_click_num(self, num):
        s = By.CSS_SELECTOR, "#simple2"
        self.base_find_element(s)
        for n in str(num):
            loc = By.CSS_SELECTOR, "#simple{}".format(n)
            self.base_click(loc)

    def page_click_add(self):
        self.base_click(page.cal_add)

    def page_click_eq(self):
        self.base_click(page.cal_eq)

    def page_get_value(self):
        return self.base_get_value(page.cal_result)

    def page_click_clear(self):
        self.base_click(page.cal_clear)

    def page_get_img(self):
        self.base_get_img()

    def page_add_cal(self, a, b):
        self.page_click_num(a)
        sleep(0.5)
        self.page_click_add()
        self.page_click_num(b)
        sleep(0.5)
        self.page_click_eq()
        sleep(0.5)