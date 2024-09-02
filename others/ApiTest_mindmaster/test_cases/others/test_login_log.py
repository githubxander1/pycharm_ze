import unittest
# from common.requests_handler import RequestsHandler
# from common.excel_handler import ExcelHandler
import ddt
import json
# from common.logger_handler import logger
from ApiTest_mindmaster.common.excel_handle import ExcelHandler
from ApiTest_mindmaster.common.logger_handler import logger
from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler


@ddt.ddt
class TestLogin(unittest.TestCase):
    # 读取excel中的数据
    excel = ExcelHandler('../../data/openpyxl_mindmaster2.xlsx')
    case_data = excel.read_excel('login')
    print(case_data)
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()
    def tearDown(self):
        # 关闭session管理器
        self.req.close_session()
    @ddt.data(*case_data)
    def test_login_success(self,items):
        logger.info('*'*88)
        logger.info('当前是第{}条用例：{}'.format(items['case_id'],items['case_title']))
        logger.info('当前用例的测试数据：{}'.format(items))
        # 请求接口
        res = self.req.visit(method=items['method'],url=items['url'],json=json.loads(items['payload']),
                             headers=json.loads(items['headers']))
        try:
            # 断言：预期结果与实际结果对比
            self.assertEqual(res['code'], items['expected_result'])
            logger.info(res)
            result = 'Pass'
        except AssertionError as e:
            logger.error('用例执行失败：{}'.format(e))
            result = 'Fail'
            raise e
        finally:
            # 将响应的状态码，写到excel的第9列，即写入返回的状态码
            TestLogin.excel.write_excel("../data/cases.xlsx", 'login', items['case_id'] + 1, 9, res['code'])
            # 如果断言成功，则在第10行(测试结果)写入Pass,否则，写入Fail
            TestLogin.excel.write_excel("../data/cases.xlsx", 'login', items['case_id'] + 1, 10, result)
if __name__ == '__main__':
    unittest.main()