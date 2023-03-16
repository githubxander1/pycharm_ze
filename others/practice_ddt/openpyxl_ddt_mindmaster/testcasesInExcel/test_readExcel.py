import unittest
import requests

from ddt import ddt, data,unpack
from com_getExcelData import get_excel_data2


@ddt
class Demo(unittest.TestCase):
    @data(*get_excel_data2())
    @unpack
    def test_01(self, id, name, url, type, data, pre_result, resquests=None):
        # url='https://userapi.edrawsoft.cn/api/user/login'
        re=requests.post(url=url,data=data)
        result =pre_result in re.text
        print(result)

if __name__ == '__main__':
    unittest.main()