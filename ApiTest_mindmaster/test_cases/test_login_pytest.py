import unittest
import pytest
from pprint import pprint
import allure

from ApiTest_mindmaster.common.read_yaml import readYaml
from ApiTest_mindmaster.common.requests_handler import RequestsHandler

@allure.feature('登录')
class TestLogin:
    @pytest.fixture()
    def set_init(self):
        # 请求类实例化
        self.req = RequestsHandler()
        yield
        self.req.close_session()

    @pytest.mark.parametrize('items',readYaml())
    @allure.story('登录用例')
    def test_login_success(self,set_init,items):
        res = self.req.visit(url=items['url'],
                             method=items['method'],
                             data=items['data'])
        print(res['status'])

        try:
            # 断言：预期结果与实际结果对比:第一个是预期，第二个是实际
            assert items['expected_result'] == res['status']
            result = 'Pass'
        except AssertionError as e:
            result = 'Fail'
            raise e
        # finally:
        #     # 将响应的状态码，写到excel的第9列，即写入返回的状态码
        #     TestLogin.excel.write_excel('../data/openpyxl_mindmaster2.xlsx', 'login',items['case_id'] + 1, 8, res['status'])
        #     # 如果断言成功，则在第10行(测试结果)写入Pass,否则，写入Fail
        #     TestLogin.excel.write_excel('../data/openpyxl_mindmaster2.xlsx', 'login',items['case_id'] + 1, 9, result)


if __name__ == '__main__':
    # pytest.main(['test_login_pytest.py'])
    pytest.main(["-sq", 'test_login_pytest.py', '--alluredir=report'])

# 1.excel里面字符串要用双引号
# 2.ddt(*data):* 表示对 case_data1 进行序列解包，将其作为独立的参数进行传递。也就是说，如果 case_data1 是一个列表或元组，这两种写法的效果一样。但是，如果 case_data1 是一个字典，则不能使用 @data(case_data1,) 这种写法。
        # 如果强制使用，会出现以下错误：TypeError: 'dict' object is not iterable
        # ddt(data,)表示将 case_data1 作为一个单独的元素放入元组中，并将该元组作为参数传递给装饰器,
        # 因此，在传递一个字典对象时，应该使用 @data(case_data1,) 的方式，而不是 @data(*case_data1)
# 3.字符串和json格式转换“
        # res_dict = json.dumps(res)  # 将字典字符串转换成json字符串
        # res_dict = json.loads(res)  # 将 JSON 字符串转换成字典