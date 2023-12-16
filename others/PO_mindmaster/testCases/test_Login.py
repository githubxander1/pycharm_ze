import os
import time

import pytest
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from seleniumwire import webdriver

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

    # @pytest.mark.parametrize("username, password", [("", "mind0103@xl")])
    # def test_login_usernull(self,username,password):
    def test_login_usernull(self):
        '''账号为空'''
        # dr=webdriver.Edge()
        loginpage = LoginPage()
        # loginpage.login_mind_pro('2695418206@qq.com', 'your_password')
        loginpage.openLoginPage('2695418206@qq.com', 'your_password')
        SaveImage(self.dr,'login_usernull.png')
        # assert self.dr.title == '登录页面'  # 假设正确的页面标题是'登录页面'

    # @pytest.mark.allure_story('登录')
    # @pytest.mark.parametrize('logindata', help.readyaml('../data/login.yaml'))
    # def test_login(self, logindata):
    #     self.loginpage = LoginPage()
    #     '''登录成功'''
    #     help.makelog('输入用户名和密码')
    #     self.loginpage.openLoginPage(logindata['username'], logindata['password'])
    #     time.sleep(2)
    #     help.makelog('成功的截图')
    #     SaveImage(self.dr, 'login_success.png')

        # 等待错误提示出现
        # error_message = WebDriverWait(dr, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR,'#pane-account > div > div.el-row.is-justify-space-around.el-row--flex > form > div.el-form-item.is-error.is-required.is-no-asterisk > div > div.el-form-item__error')))

        # 断言验证错误提示内容
        # assert error_message.text == "账号或密码错误"  # 断言错误提示内容是否正确
        # assert error_message.text == logindata['preresult'], "登录失败-账密错误"

    # # @pytest.mark.webtest
    # #
    # def test_login_pwdnull(self):
    #     '''密码为空'''
    #     self.loginpage.openLoginPage('2695418206@qq.com','')


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir=../allure-results', 'test_Login.py'])
    os.system('allure generate ../allure-results -o open ../allure-results/report/html --clean ')
    # pytest.main(['-vs', '--alluredir=../allure-results', 'test_Login.py', '-m', 'webtest','-k', 'login_pwdnull'])
    # os.system('allure generate ../allure-test_results -o ./reports --clean && allure')
