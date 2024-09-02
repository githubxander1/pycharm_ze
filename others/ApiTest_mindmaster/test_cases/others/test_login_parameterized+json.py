import json
import unittest
from pprint import pprint

import requests
from parameterized import parameterized

from ApiTest_mindmaster.common.excel_handle import ExcelHandler
from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler

def build_data():
    with open('../../data/loginData.json') as f:
        result=json.load(f)
        data=[]
        # pprint(result)
        for i in result:
            data.append((i.get('email'),i.get('pw'),i.get('from'),i.get('product')))
            # print(data)
    return data
print(build_data())

class TestLogin(unittest.TestCase):

    @parameterized.expand(build_data())
    def test_login_success(self, email, from_, product, pw):
        self.url = "https://userapi.edrawsoft.cn/api/user/login"
        res = requests.post(self.url, data={"email": email,"pw": pw, "from": from_, "product": product})
        print(res.json())

    @unittest.skip('没什么原因') #跳过
    def test_login_success1(self, email, from_, product, pw):
        self.url = "https://userapi.edrawsoft.cn/api/user/login"
        res = requests.post(self.url, data={"email": email, "pw": pw, "from": from_, "product": product})
        print(res.json())
if __name__ == '__main__':
    unittest.main()
