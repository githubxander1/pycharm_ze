# 百度首页po
from selenium.webdriver.common.by import By

from login import Login
from selenium import webdriver

from search import Search


class Index:

    # 初始方法
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://www.baidu.com')
        self._driver.maximize_window()
        self._driver.implicitly_wait(3)

    # 退出方法
    # def teardown(self):
    #     self._driver.quit()

    # 跳转登录
    def goto_login(self):
        self._driver.find_element(By.ID, 's-top-loginbtn').click()
        return Login(self._driver)

    # 跳转搜索
    def goto_search(self):
        return Search(self._driver)

Index().goto_login()