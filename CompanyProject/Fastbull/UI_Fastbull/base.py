from selenium import webdriver


class Base:
    def __init__(self,driver):
        self.d = driver
        self.d.implicitly_wait(10)

    def open_url(self,url):
        self.url=url
        self.d.get(self.url)

