import unittest
from ddt import ddt,data,unpack
import requests
from com import get_excel_data3,send_request

@ddt
class Demo(unittest.TestCase):
    @data(*get_excel_data3())
    @unpack
    def test_01_demo(self,id,name,url,type,data_type,data,pre_result,result):
        # 不用之前的re = requests.post(url=url,data=data)，用自己封装的请求调用
        re = send_request(url=url,type=type,data_type=data_type,data=data)
        result = pre_result in re.text
        print(result)   # 打印结果：True True True True False True
if __name__=="__main__":
    unittest.main()
