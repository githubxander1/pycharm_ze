from selenium import webdriver

from others.PO_test.POtest_wechat.ztest.base import BasePage
from others.PO_test.POtest_wechat.ztest.page.regester import Register

d=webdriver.Edge()

class Login(BasePage):
    def scanlogin(self):
        pass

    def goto_regester(self):
        d.find_element_by_css_selector('#wework_admin\.loginpage_wx2_\$ > main > div.login_registerBar > a').click()
        return Register(self.d)