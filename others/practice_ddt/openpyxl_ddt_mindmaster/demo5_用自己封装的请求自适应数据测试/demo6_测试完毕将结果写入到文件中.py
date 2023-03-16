import unittest
from ddt import ddt, data, unpack
from com import get_excel_data3,send_request,write_result
# 步骤1:导入自写模块的函数


@ddt
class Demo(unittest.TestCase):
    @data(*get_excel_data3())
    @unpack
    def test_01_demo(self, id, name, url, type, data_type, data, pre_result, result):
        re = send_request(url=url, type=type, data_type=data_type, data=data)
        result = pre_result in re.text
        write_result(id=id, result=result)


if __name__ == "__main__":
    unittest.main()
