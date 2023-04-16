from selenium import webdriver

class BasePage:

    def __init__(self):
        self.d=webdriver.Edge()
        self.d.get('https://www.baidu.com/')

    def ele(self,loc):
        self.d.find_element(loc)