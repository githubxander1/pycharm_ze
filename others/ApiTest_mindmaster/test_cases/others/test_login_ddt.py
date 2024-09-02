import json
import unittest
from pprint import pprint

from ddt import ddt,data
from ApiTest_mindmaster.common.excel_handle import ExcelHandler
from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler

@ddt
class TestLogin(unittest.TestCase):
    # 读取excel中的数据
    excel = ExcelHandler('../../data/openpyxl_mindmaster2.xlsx')
    case_data = excel.read_excel('login')
    # 将字符串中的反斜杠替换为空
    # payload_str = case_data['data'].replace('\\', '')
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()

    def tearDown(self):
        self.req.close_session()

    @data(*case_data)
    def test_login(self, items):
        # pprint(items)
        res = self.req.visit(url=items['url'],
                             method=items['method'],
                             data=items['data'])

        try:
            # 断言：预期结果与实际结果对比:第一个是预期，第二个是实际
            self.assertEqual(items['expected_result'], res['status'])
            self.result = 'Pass'
        except AssertionError as e:
            self.result = 'Fail'
            raise e
        finally:
            # 将响应的状态码，写到excel的第9列，即写入返回的状态
            TestLogin.excel.write_excel('../data/openpyxl_mindmaster2.xlsx', 'login',items['case_id'] + 1, 8, res['status'])
            # 如果断言成功，则在第10行(测试结果)写入Pass,否则，写入Fail
            TestLogin.excel.write_excel('../data/openpyxl_mindmaster2.xlsx', 'login',items['case_id'] + 1, 9, self.result)


if __name__ == '__main__':
    unittest.main(__file__)

# 实例25_批量生成PPT版荣誉证书.excel里面字符串要用双引号
# 2.ddt(*data):* 表示对 case_data1 进行序列解包，将其作为独立的参数进行传递。也就是说，如果 case_data1 是一个列表或元组，这两种写法的效果一样。但是，如果 case_data1 是一个字典，则不能使用 @data(case_data1,) 这种写法。
        # 如果强制使用，会出现以下错误：TypeError: 'dict' object is not iterable
        # ddt(data,)表示将 case_data1 作为一个单独的元素放入元组中，并将该元组作为参数传递给装饰器,
        # 因此，在传递一个字典对象时，应该使用 @data(case_data1,) 的方式，而不是 @data(*case_data1)
# 3.字符串和json格式转换“
        # res_dict = json.dumps(res)  # 将字典字符串转换成json字符串
        # res_dict = json.loads(res)  # 将 JSON 字符串转换成字典