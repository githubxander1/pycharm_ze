import os
import time

import pytest
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver

from others.PO_mindmaster.basepage.baseBase import BasePage
from others.PO_mindmaster.common.getImage import SaveImage
from others.PO_mindmaster.common.helper import help, Helper
from others.PO_mindmaster.page.loginpage import LoginPage

sys.path.append('../basepage')
sys.path.append('../page')
sys.path.append('../common')
sys.path.append('../data')


@pytest.mark.allure_feature('用户登录')
class TestLogin(BasePage):
    def setUp(self):
        print('运行')

    def tearDown(self):
        # self.dr.quit()
        print('结束')

        @pytest.mark.allure_story('登录')
        @pytest.mark.parametrize('logindata', help.readyaml('../data/login.yaml'))
        def test_login(self, logindata):
            self.loginpage = LoginPage()
            '''登录成功'''
            # help.makelog('输入用户名和密码')
            self.loginpage.openLoginPage(logindata['username'], logindata['password'])
            # time.sleep(2)
            # Helper.makelog('成功的截图')
            # SaveImage(self.dr, 'login_success.png')
            # assert res.json()

        # def test_login_usernull(self):
        #     '''账号为空'''
        #     self.loginpage.openLoginPage('','mind0103@xl')
        #     SaveImage(self.dr,'login_usernull.png')

        # def test_login_pwdnull(self):
        #     '''账号为空'''
        #     self.loginpage.openLoginPage('2695418206@qq.com','')

    if __name__ == '__main__':
        pytest.main(['-vs', '--alluredir=allure-results', 'test_Login.py'])
        os.system('allure generate ./allure-results -o ./reports --clean')