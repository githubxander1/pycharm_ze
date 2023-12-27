import os
import time

import allure
import pytest
from pytest_assume.plugin import assume

from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.common.common import Common
from CompanyProject.APP_Fastbull2.operation.directory.add_friend import Add_friend
from CompanyProject.APP_Fastbull2.operation.home.home_search import home_search


@allure.epic('epic:测试首页全局搜索')
@allure.feature('feature:搜索')
class Test_add_friend:
    def setup_class(self):
        with allure.step('step：打开应用'):
            Base1().startApp()
            time.sleep(6)
            Add_friend().click_add_home()
            Add_friend().click_add_friend()



    def teardown_class(self):
        with allure.step('step：关闭应用'):
            Base1().closeApp()

    def setup_method(self):
        time.sleep(2)

    def teardown_method(self):
        with allure.step('step：点击取消'):
            pass

    @pytest.mark.run(order=1)
    @allure.severity('critical')
    @allure.feature('feature:添加好友')
    @allure.story('story:添加好友')
    @allure.title('title:用户昵称')
    # @pytest.mark.xfail(reason='功能未实现')  #用例在运行时如果失败了，不会被报告为错误，而是会被报告为预期失败（xfailed）。如果预期失败的用例意外地通过了，那么它会被报告为意外通过（xpassed）。
    def test_nickname(self):
        '''描述：这是搜索全部的测试用例'''
        text='1'
        with allure.step("通过'用户昵称'搜索"):
            text='1316-测试'
            Add_friend().click_nickname_tab()
            Add_friend().send_edit_text(text)

        file_basename = os.path.basename(__file__)
        with allure.step('截图'):
            screen=Common().take_screenshot(file_basename, text)
            # print(f'截图路径：{screen}')
            allure.attach(f'{screen}',name='截图',attachment_type=allure.attachment_type.PNG)
        with assume: assert Add_friend().add_friend_top.exists
        # with assume: assert 2 == 3

    # @pytest.mark.skip()
    @pytest.mark.run(order=2)
    @allure.title('手机号')
    def test_phone(self):
        text = '13111111111'
        with allure.step("通过'手机号'搜索"):
            Add_friend().click_phone()
            Add_friend().send_edit_text(text)

        file_basename = os.path.basename(__file__)
        Common().take_screenshot(file_basename, text)

    # @pytest.mark.skip()
    @allure.title('title:FXID')
    def test_fxid(self):
        text = '5809513'
        with allure.step("通过'FXID'搜索"):
            Add_friend().click_fxid_tab()
            Add_friend().send_edit_text(text)
        file_basename = os.path.basename(__file__)
        Common().take_screenshot(file_basename, text)

    # @pytest.mark.skip()
    @allure.title('title:Email')
    def test_email(self):
        text = '1@qq.com'
        with allure.step("通过'Email'搜索"):
            Add_friend().click_email_tab()
            Add_friend().send_edit_text(text)
        file_basename = os.path.basename(__file__)
        Common().take_screenshot(file_basename, text)

if __name__ == '__main__':
    pytest.main(['-vs','--retun 2','test_add_friend.py', '--alluredir=./allureTemps'])
    # 加3秒延迟时为了让用例能完整执行，并生成临时文件
    time.sleep(3)
    os.system("allure generate ./allureTemps -o ./reports --clean")
