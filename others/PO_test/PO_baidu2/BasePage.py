# https://blog.51cto.com/u_15333574/5301015

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, Find_Element等
    """
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
    # __init__方法不能有返回值，只能返回None

    def __init__(self,selenium_driver,base_url):
        self.driver = selenium_driver
        self.base_url = base_url
        # self.pagetitle = pagetitle

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def open(self):
        self._open(self.base_url,self.pagetitle)

    def find_element(self,*loc): #*loc任意数量的位置参数（带单个星号参数）
        # return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:

            print("%s 页面未能找到 %s 元素"%(self,loc))

    def script(self,src):
        self.driver.excute_script(src)

    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc) # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))
