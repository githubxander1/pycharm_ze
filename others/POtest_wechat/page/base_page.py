from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        #此处对driver进行复用，如果不存在driver,就构造一个新的
        if driver is None:
            # Index页面需要用，首次使用时构造新driver
            self._driver = webdriver.Chrome()
            # 设置隐式等待时间
            self._driver.implicitly_wait(3)
            # 访问网页
            self._driver.get(self._base_url)
        else:
            # Login与Register等页面需要用这个方法，避免重复构造driver
            self._driver = driver

    def close(self):
        sleep(20)
        self._driver.quit()