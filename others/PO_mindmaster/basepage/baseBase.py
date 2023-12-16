from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# url='https://mm.edrawsoft.cn/files'
# dr=webdriver.Edge()

class BasePage:

    def __int__(self, dr):
        # self.url = url
        self.dr = dr

    def open_url(self,url):
        # self.dr=webdriver.Edge()
        self.dr.get(url)

    def locator(self, loc):
        return self.dr.find_element(*loc)
        # try:
        #     WebDriverWait(self.dr, 20).until(EC.visibility_of_element_located(*loc))
        #     return self.dr.find_elememt(*loc)
        # except:
        #     print(*loc + "无法找到该元素")

    def send_keys(self,loc,value):
        self.locator(loc).send_keys(value)

    def click(self,loc):
        self.locator(loc).click()
    # def __init__(self):
    #     self.dr=webdriver.Edge()
    #     self.url = 'https://mm.edrawsoft.cn/files'
    # def locator(self,*loc):
    #     try:
    #         WebDriverWait(self.dr,20).until(EC.visibility_of_element_located(loc))
    #         return self.dr.find_elememt(*loc)
    #     except:
    #         print(f"{loc}无法找到该元素")

# base=HomePage(url,dr)
# url='https://mm.edrawsoft.cn/files'
# dr=webdriver.Edge()
