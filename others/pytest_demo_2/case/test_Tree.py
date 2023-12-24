import os
import time

import allure
import pytest

from others.pytest_demo_2.data_driver.yaml_driver import load_yaml
from others.pytest_demo_2.logic.shopingApi import ApiCase


@allure.epic("shopXo电商平台接口-接口测试")
class TestTree():
    # 初始化用例库
    actions1 = ApiCase()

    @allure.feature("01.登陆")
    @allure.story("02.一般场景")
    @pytest.mark.parametrize('userdata', load_yaml('../data/user.yaml'))
    def test_case01(self, userdata):
        self.actions1.params_login(userdata)
        # assert
        # assert

    @pytest.mark.skip("跳过")
    @allure.feature("02.个人查询")
    @allure.story("01.典型场景")
    @allure.title("个人查询")
    def test_case02(self, token_fix):
        self.actions1.params_getuserinfo(token_fix)

    @pytest.mark.skip("跳过")
    @allure.feature("03.添加商品到购物车")
    @allure.story("01.典型场景")
    @allure.title("添加商品到购物车")
    def test_case03(self, token_fix):
        self.actions1.params_addcart(token_fix)

    @pytest.mark.skip("跳过")
    @allure.feature("04.下单")
    @allure.story("01.典型场景")
    @allure.title("下单")
    def test_case04(self, token_fix):
        self.actions1.params_createorder(token_fix)

# TestTree=TestTree()
# TestTree.test_case
if __name__ == '__main__':
    # 获取当前脚本所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pytest.main(['-vs'])
    # 加3秒延迟时为了让用例能完整执行，并生成临时文件
    time.sleep(3)
    # 通过 os.system 向系统终端输入指令 allure generate 表示生成 html 报告，
    # ./allureTemps 表示用来生成html的JSON临时文件目录
    # ./reports 表示html文件生成目录
    # --clean 表示生成前清空之前的文件
    os.system("allure generate ./allureTemps -o ./reports --clean")