from selenium import webdriver

from

# d=webdriver.Chrome()
# d.get('https://www.baidu.com/')
#
# d.find_element_by_id('kw').send_keys('selenium')
# d.find_element_by_id('su').click()
from selenium.webdriver.common.by import By

from others.PO_test.PO_baidu3.Common.base import BasePage


class Search(BasePage):
    loc=(By.ID,'kw')

    def search_content(self,loc):
        self.ele(loc).click()

