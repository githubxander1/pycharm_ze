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
    @pytest.mark.parametrize('userdata', load_yaml('./data/user.yaml'))
    def test_case01(self, userdata):
        self.actions1.params_login(userdata)

    @allure.feature("02.个人查询")
    @allure.story("01.典型场景")
    @allure.title("个人查询")
    def test_case02(self, token_fix):
        self.actions1.params_getuserinfo(token_fix)

    @allure.feature("03.添加商品到购物车")
    @allure.story("01.典型场景")
    @allure.title("添加商品到购物车")
    def test_case03(self, token_fix):
        self.actions1.params_addcart(token_fix)

    @allure.feature("04.下单")
    @allure.story("01.典型场景")
    @allure.title("下单")
    def test_case04(self, token_fix):
        self.actions1.params_createorder(token_fix)