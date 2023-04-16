from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from others.POtest_wechat.ztest.page.base import BasePage
from others.POtest_wechat.ztest.page.register import Register


class Login(BasePage):
    def scan_login(self):
        pass

    def goto_register(self):
        self._d.find_element(By.LINK_TEXT, "企业注册").click()
        return Register(self._d)

Login().register()