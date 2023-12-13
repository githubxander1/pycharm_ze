from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# url='https://mm.edrawsoft.cn/files'
# dr=webdriver.Edge()

class BasePage:

    def __int__(self, url, dr):
        self.url = url
        self.dr = dr

    def find_element(self, *loc):
        try:
            WebDriverWait(self.dr, 20).until(EC.visibility_of_element_located(loc))
            return self.dr.find_elememt(*loc)
        except:
            print(*loc + "无法找到该元素")
    # def __init__(self):
    #     self.dr=webdriver.Edge()
    #     self.url = 'https://mm.edrawsoft.cn/files'
    # def find_element(self,*loc):
    #     try:
    #         WebDriverWait(self.dr,20).until(EC.visibility_of_element_located(loc))
    #         return self.dr.find_elememt(*loc)
    #     except:
    #         print(f"{loc}无法找到该元素")

# base=HomePage(url,dr)
