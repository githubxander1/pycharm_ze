import time

from selenium.webdriver.common.by import By

from others.PO_test.POtest_wechat.ztest.base import BasePage
from others.PO_test.POtest_wechat.ztest.page.login import Login
from others.PO_test.POtest_wechat.ztest.page.regester import Register


class Index(BasePage):
    def goto_login(self):
        self.d.find_element(By.XPATH,'//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return Login(self.d)

    def goto_register(self):
        # self._d.find_element(By.CSS_SELECTOR,'#tmp > div.index_head_info > a').click()
        self.d.find_element(By.XPATH,'//*[@id="tmp"]/div[1]/a').click()
        return Register(self.d)

# Index().goto_login()
Index().goto_register()
time.sleep(5)