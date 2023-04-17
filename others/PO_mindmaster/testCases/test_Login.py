import sys
import time
import unittest

import pytest
import logging
from selenium.webdriver.common.by import By

from others.PO_mindmaster.common.getImage import SaveImage
from others.PO_mindmaster.common.helper import Helper
from others.PO_mindmaster.page.loginpage import LoginPage
from others.PO_mindmaster.basepage.homeBase import HomePage
# import Helper

sys.path.append('../basepage')
sys.path.append('../page')
sys.path.append('../common')

from selenium import webdriver

username1='2695418206@qq.com'
password1='mind0103@xl'

class TestLogin(HomePage):
    def setUp(self):
        pass
        # self.url='https://mm.edrawsoft.cn/files/api/user/login'
        # self.dr=webdriver.Edge()
        # self.dr.implicitly_wait(20)
        # 实例化一个loginpage对象

    def tearDown(self):
        # self.dr.quit()
        pass

    def test_login_sus(self):
        self.loginpage = LoginPage()
        '''登录成功'''
        Helper().makelog('输入用户名和密码')
        self.loginpage.openLoginPage(username1, password1)
        time.sleep(2)
        Helper.makelog('成功的截图')
        SaveImage(self.dr,'login_success.png')
        # assert res.json()

    # def test_login_usernull(self):
    #     '''账号为空'''
    #     self.loginpage.openLoginPage('','mind0103@xl')
    #     SaveImage(self.dr,'login_usernull.png')

    # def test_login_pwdnull(self):
    #     '''账号为空'''
    #     self.loginpage.openLoginPage('2695418206@qq.com','')


if __name__ == '__main__':
    pytest.main()
