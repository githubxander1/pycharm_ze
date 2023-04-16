from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __int__(self,url,dr):
        self.url=url
        self.dr=dr
        # self.url='https://mm.edrawsoft.cn/files'
        # self.dr=webdriver.Edge()

    def find_element(self,*loc):
        try:
            WebDriverWait(self.dr,20).until(EC.visibility_of_element_located(loc))
            return self.dr.find_elememt(*loc)
        except:
            print(*loc+"无法找到该元素")