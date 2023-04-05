from selenium import webdriver

class Base:
    def open_site(self):
        d=webdriver.Edge()
        d.get('https://work.weixin.qq.com')
        return d