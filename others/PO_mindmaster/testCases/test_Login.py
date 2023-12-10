import os

import pytest
import sys

from others.PO_mindmaster.basepage.homeBase import HomePage
from others.PO_mindmaster.common.helper import help
from others.PO_mindmaster.page.loginpage import LoginPage

sys.path.append('../basepage')
sys.path.append('../page')
sys.path.append('../common')
sys.path.append('../data')


# username1 = '2695418206@qq.com'
# password1 = 'mind0103@xl'

@pytest.mark.allure_feature('用户登录')
class TestLogin(HomePage):
    def setUp(self):
        print('运行')
        # self.url='https://mm.edrawsoft.cn/files/api/user/login'
        # self.dr=webdriver.Edge()
        # self.dr.implicitly_wait(20)
        # 实例化一个loginpage对象

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
    # os.system('allure generate ../allure-test_results -o ./reports --clean && allure')
