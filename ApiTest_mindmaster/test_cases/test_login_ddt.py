import json
import unittest
# from common.requests_handler import RequestsHandler
from pprint import pprint

from ddt import ddt,data

from ApiTest_mindmaster.common.excel_handle import ExcelHandler
from ApiTest_mindmaster.common.requests_handler import RequestsHandler

@ddt
class TestLogin(unittest.TestCase):
    # 读取excel中的数据
    excel = ExcelHandler('../data/openpyxl_mindmaster2.xlsx')
    case_data = excel.read_excel('login')
    # 将字符串中的反斜杠替换为空
    # payload_str = case_data['data'].replace('\\', '')
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()

    def tearDown(self):
        self.req.close_session()

    @data(*case_data)
    def test_login_success(self, items):
        # items=items
        # pprint(items)
        res = self.req.visit(url=items['url'],
                             method=items['method'],
                             # data=items[json.loads('data')])
                             data=items['data'])
        print(res)
        print(res['status'])
        # 验证接口返回值
        # res_dict = json.loads(res)  # 将 JSON 字符串转换成字典
        # self.assertIsInstance(res_dict, dict)  # 判断 res 是否为字典
        # self.assertIn('status', res_dict)  # 判断 res 是否包含 'status' 键
        #
        # # 确认预期结果是否与实际结果一致
        self.assertEqual(str(res['status']), items['expected_result'])

        # try:
        #     # 断言：预期结果与实际结果对比
        #     self.assertEqual(res['status'],items['expected_result'])
        #     result = 'Pass'
        # except AssertionError as e:
        #     result = 'Fail'
        #     raise e
        # finally:
        #     # 将响应的状态码，写到excel的第9列，即写入返回的状态码
        #     TestLogin.excel.write_excel("../data/openpyxl_mindmaster2.xlsx", 'login',items['case_id'] + 1, 9, res['status'])
        #     # 如果断言成功，则在第10行(测试结果)写入Pass,否则，写入Fail
        #     TestLogin.excel.write_excel("../data/openpyxl_mindmaster2.xlsx", 'login',items['case_id'] + 1, 10, result)
        # pprint(res['data'])
        # self.assertEqual('success', res['status'])


if __name__ == '__main__':
    unittest.main()