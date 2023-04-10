from selenium import webdriver

class BasePage:
    def __init__(self):
        self.d = webdriver.Edge()
        self.d.implicitly_wait(10)
        self.d.get('https://work.weixin.qq.com')


    # def opensite(self):
    #     d=webdriver.Edge()
    #     d.get('https://work.weixin.qq.com')
    #     return d