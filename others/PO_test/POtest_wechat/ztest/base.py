from selenium import webdriver

class BasePage:
    def __init__(self,driver,base_url):
        # 对driver复用，如果不存在则构造一个新的
        if driver is None:
            self.d = webdriver.Edge()
            self.d.implicitly_wait(10)
        else:
            self.d = driver


    # def opensite(self):
    #     d=webdriver.Edge()
    #     d.get('https://work.weixin.qq.com')
    #     return d