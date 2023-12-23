import os
import time

import allure
import pytest
from pytest_assume.plugin import assume

from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.common.common import common
from CompanyProject.APP_Fastbull2.operation.home.home_search import home_search

@allure.epic('epic:测试首页全局搜索')
@allure.feature('feature:搜索')
class Test_home_search:
    def setup_class(self):
        with allure.step('step：打开应用'):
            Base1().startApp()
            time.sleep(4)


    def teardown_class(self):
        with allure.step('step：关闭应用'):
            Base1().closeApp()

    def setup_method(self):
        pass
        # home_search().click_searchBox_out()

    def teardown_method(self):
        with allure.step('step：点击取消'):
            home_search().click_cancel()

    @pytest.mark.run(order=1)
    @allure.severity('critical')
    @allure.feature('feature:搜索')
    @allure.story('story:搜索全部')
    @allure.title('title:搜索全部')
    # @pytest.mark.xfail(reason='功能未实现')  #用例在运行时如果失败了，不会被报告为错误，而是会被报告为预期失败（xfailed）。如果预期失败的用例意外地通过了，那么它会被报告为意外通过（xpassed）。
    def test_home_search_all(self):
        '''描述：这是搜索全部的测试用例'''
        text='1'
        with allure.step('点击首页搜索框'):
            home_search().search_all(text)
        file_basename = os.path.basename(__file__)
        with allure.step('截图'):
            screen=common().take_screenshot(file_basename, text)
            # print(f'截图路径：{screen}')
            allure.attach(f'{screen}',name='截图',attachment_type=allure.attachment_type.PNG)
        with assume: assert home_search().unfold.exists
        # with assume: assert 2 == 3

    # @pytest.mark.skip()
    @pytest.mark.run(order=2)
    @allure.title('title:搜索好友')
    def test_home_search_friend(self):
        text = '好友'
        with allure.step('点击找好友'):
            home_search().click_searchBox_out()
        home_search().search_friend(text)
        file_basename = os.path.basename(__file__)
        common().take_screenshot(file_basename, text)

    # @pytest.mark.skip()
    @allure.title('title:搜索群聊')
    def test_home_search_group(self):
        text = '群'
        with allure.step('点击找群聊'):
            home_search().search_group(text)
        file_basename = os.path.basename(__file__)
        common().take_screenshot(file_basename, text)

    # @pytest.mark.skip()
    @allure.title('title:搜索聊天记录')
    def test_home_search_chat_record(self):
        text = '聊天'
        with allure.step('点击找聊天记录'):
            home_search().search_chat_record(text)
        file_basename = os.path.basename(__file__)
        common().take_screenshot(file_basename, text)

if __name__ == '__main__':
    # pytest.main(['-vs', '--rerun 2','Test_home_search.py','--alluredir=./allure_result'])
    # pytest.main(['-s', '-q', '--alluredir', './report'])
    # os.system('allure generate ./allure_result -o allure_result/html open')
    pytest.main(['test_home_search.py', '-vs', '--alluredir=./allureTemps'])
    # 加3秒延迟时为了让用例能完整执行，并生成临时文件
    time.sleep(3)
    # 通过 os.system 向系统终端输入指令 allure generate 表示生成 html 报告，
    # ./allureTemps 表示用来生成html的JSON临时文件目录
    # ./reports 表示html文件生成目录
    # --clean 表示生成前清空之前的文件
    os.system("allure generate ./allureTemps -o ./reports --clean")
