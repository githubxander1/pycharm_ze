import json
import unittest
# from common.requests_handler import RequestsHandler
from pprint import pprint

import ddt

from ApiTest_mindmaster.common.excel_handle import ExcelHandler
from ApiTest_mindmaster.common.requests_handler import RequestsHandler


class TestLogin(unittest.TestCase):
    # 读取excel中的数据
    excel = ExcelHandler('../data/openpyxl_mindmaster2.xlsx')
    case_data = excel.read_excel('login')
    pprint(case_data)

    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()

    def tearDown(self):
        self.req.close_session()

    @ddt.data(*case_data)
    def test_login_success(self, items):
        # login_url = 'https://userapi.edrawsoft.cn/api/user/login'
        # payload={
        #       'email': "2695418206@qq.com",
        #       'from': "web",
        #       'product': "master-online",
        #       'pw': "f2d8ddfc169a0ee6f8b0ecd924b1d300"
        #       }

        res = self.req.visit(method=items['method'],url=items['url'],json=json.loads(items['payload']),
                             headers=json.loads(items['headers']))
        try:
            # 断言：预期结果与实际结果对比
            self.assertEqual(res['code'], items['expected_result'])
            result = 'Pass'
        except AssertionError as e:
            result = 'Fail'
            raise e
        finally:
            # 将响应的状态码，写到excel的第9列，即写入返回的状态码
            TestLogin.excel.write_excel("../data/openpyxl_mindmaster2.xlsx", 'login', items['case_id'] + 1, 9, res['code'])
            # 如果断言成功，则在第10行(测试结果)写入Pass,否则，写入Fail
            TestLogin.excel.write_excel("../data/openpyxl_mindmaster2.xlsx", 'login', items['case_id'] + 1, 10, result)
        pprint(res['data'])
        self.assertEqual('success', res['status'])


if __name__ == '__main__':
    unittest.main()