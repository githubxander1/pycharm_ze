import unittest
from pprint import pprint
from ddt import ddt,data

from ApiTest_mindmaster.common.excel_handle import ExcelHandler
from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler

case_data1 = [{'actual_result': None,
                 'case_id': 1,
                 'case_title': 'login_suss',
                 'expected_result': 'success',
                 'method': 'post',
                 'model_name': '登录',
                 'data': '{\'email\': "695418206@qq.com",\'from\': "web",\'product\': '
                            '"master-online",\'pw\': "f2d8ddfc169a0ee6f8b0ecd924b1d300"}',
                 'test_result': None,
                 'url': 'https://userapi.edrawsoft.cn/api/user/login'},
            {'actual_result': None,
                             'case_id': 2,
                             'case_title': 'login_fail',
                             'expected_result': 'fault',
                             'method': 'post',
                             'model_name': '登录',
                             'data': '{\'email\': "69541820@qq.com",\'from\': "web",\'product\': '
                                        '"master-online",\'pw\': "f2d8ddfc169a0ee6f8b0ecd924b1d300"}',
                             'test_result': None,
                             'url': 'https://userapi.edrawsoft.cn/api/user/login'}  ]
@ddt
class TestLogin(unittest.TestCase):

    # # 读取excel中的数据
    # excel = ExcelHandler('../data/openpyxl_mindmaster2.xlsx')
    # case_data = excel.read_excel('login')
    # pprint(case_data)
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()

    def tearDown(self):
        self.req.close_session()

    @data(*case_data1)
    # data方法只能以列表或元组形式接收待测数据，而由于您将待测数据封装在字典中，因此需要先将它转换成列表或元组形式。
    def test_login_success(self,items):
        print(items)
        res = self.req.visit(url=items['url'],
                             method=items['method'],
                             data=items['data'])
        print(res)


if __name__ == '__main__':
    unittest.main()