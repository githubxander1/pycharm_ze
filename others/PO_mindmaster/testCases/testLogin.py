import sys
import time
import unittest

from selenium.webdriver.common.by import By

from others.PO_mindmaster.page.loginpage import LoginPage
from others.PO_mindmaster.basepage.homeBase import HomePage

sys.path.append('../basepage')
sys.path.append('../page')

from selenium import webdriver

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.url='https://mm.edrawsoft.cn/files/api/user/login'
        self.dr=webdriver.Edge()
        self.dr.implicitly_wait(20)
        # 实例化一个loginpage对象
        self.loginpage=LoginPage()

    def tearDown(self) :
        self.dr.quit()

    def testlogin_sus(self):
        '''登录成功'''
        self.loginpage.openLoginPage('2695418206@qq.com','mind0103@xl')
        time.sleep(2)
        # assert res.json()

    # def testlogin_usernull(self):
    #     '''账号为空'''
    #     self.loginpage.openLoginPage('','mind0103@xl')
    #
    # def testlogin_pwdnull(self):
    #     '''账号为空'''
    #     self.loginpage.openLoginPage('2695418206@qq.com','')

if __name__ == '__main__':
    unittest.main()

