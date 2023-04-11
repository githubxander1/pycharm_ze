from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Search:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    # 搜索功能封装
    def search(self):
        self._driver.find_element(By.ID, 'kw').send_keys('北京')
        self._driver.find_element(By.ID, 'su').click()
