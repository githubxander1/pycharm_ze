import pytest
import allure
from others.pytest_demo_2.api_keyword.api_key import ApiKey
from others.pytest_demo_2.params.allParams import URL, PORT


class ApiCase():
    # 登录逻辑
    def params_login(self, userdata):
        # 动态获取参数生成标题
        allure.dynamic.title(userdata['title'])
        # 初始化工具类
        ak = ApiKey()
        # 请求接口
        url = URL + PORT + '/api/login'
        # 请求参数
        userInfo = {
            'username': userdata['user']['username'],
            'password': userdata['user']['password']
        }
        res = ak.post(url=url, json=userInfo)
        with allure.step("接口返回信息校验及打印"):
            print("/api/login登录接口请求响应信息")
            print(res.text)
            # 获取响应结果
            msg = ak.get_text(res.text, 'msg')
            print(msg)
            # 断言
            assert msg == userdata['msg']

    def params_getuserinfo(self, token_fix):
        # 从fix中获取预置的工具类和token,所有返回值都需要接收
        ak, token, res, token_random01 = token_fix
        with allure.step("发送个人查询接口请求"):
            url = URL + PORT + '/api/getuserinfo'
            headers = {
                'token': token
            }
            res1 = ak.get(url=url, headers=headers)
        with allure.step("接口返回信息校验及打印"):
            print("/api/getuserinfo个人用户查询接口请求响应信息")
            print(res1.text)
            # print("验证的random值，测试用")
            # print(token_random01)
            name = ak.get_text(res1.text, 'nikename')
            # 断言
            assert "风清扬" == name
        return res1

    def params_addcart(self, token_fix):
        # 从fix中获取预置的工具类和token
        # 所有返回都要获取，不然会报错
        ak, token, res, token_random01 = token_fix
        with allure.step("调用getuserinfo接口获取返回信息"):
            res1 = self.params_getuserinfo(token_fix)
        with allure.step("发送添加商品到购物车请求"):
            # 添加商品到购物车,基于token、userid、openid、productid
            url = URL + PORT + '/api/addcart'
            hd = {
                "token": token
            }
            data = {
                "userid": ak.get_text(res1.text, 'userid'),
                "openid": ak.get_text(res1.text, 'openid'),
                "productid": 8888
            }
            # 发送请求
            res2 = ak.post(url=url, headers=hd, json=data)
        with allure.step("接口返回信息校验及打印"):
            print("/api/addcart添加商品到购物车请求响应信息")
            print(res2.text)
            # print("验证的random值，测试用")
            # print(token_random01)
            result = ak.get_text(res2.text, 'result')
            assert 'success' == result
        return res2

    def params_createorder(self, token_fix):
        ak, token, res, token_random01 = token_fix
        with allure.step("调用addcart接口获取返回信息"):
            res1 = self.params_addcart(token_fix)
        with allure.step("发送下单请求"):
            url = URL + PORT + '/api/createorder'
            # 从项目级fix中获取token
            hd = {
                "token": token
            }
            # 从添加商品到购物车接口中获取userid,openid,cartid
            data = {
                "userid": ak.get_text(res1.text, 'userid'),
                "openid": ak.get_text(res1.text, 'openid'),
                "productid": 8888,
                "cartid": ak.get_text(res1.text, 'cartid')
            }
            res2 = ak.post(url=url, headers=hd, json=data)
        with allure.step("接口返回信息校验及打印"):
            print("/api/createorder下单请求响应信息")
            print(res2.text)
            # print("验证的random值，测试用")
            # print(token_random01)
            result = ak.get_text(res1.text, 'result')
            assert 'success' == result