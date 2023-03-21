"""get_driver.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
from selenium import webdriver
from PO import page


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver == None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            """置空,一定要置空"""
            cls.driver = None