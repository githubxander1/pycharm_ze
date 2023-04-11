# 基本测试场景
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("Bela") #输入框
# driver.find_element_by_xpath("//input[@id='su']").click() #百度一下按钮
#
# sleep(3)
# driver.quit()

# 优化后的测试场景
from selenium.webdriver.common.by import By
from BasePage import BasePage #假设baidu.py、BasePage.py均在PODemo.BasePage目录下
from selenium import webdriver

class SearchPage(BasePage):

    # 定位元素
    search_loc = (By.ID,"kw")
    btn_loc = (By.ID,"su")

    def open(self):
        self._open(self.base_url)

    def search_content(self,content):
        BaiduContent = self.find_element(*self.search_loc)
        BaiduContent.send_keys(content)

    def btn_click(self):
        BaiduBtn = self.find_element(*self.btn_loc)
        BaiduBtn.click()

base_url='http://www.baidu.com'
SearchPage()