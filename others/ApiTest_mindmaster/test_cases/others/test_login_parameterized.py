import unittest
from pprint import pprint

import requests
from parameterized import parameterized

from ApiTest_mindmaster.common.excel_handle import ExcelHandler
from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler

data=[
    {"email": "695418206@qq.com",
      "from": "web",
      "product": "master-online",
      "pw": "f2d8ddfc169a0ee6f8b0ecd924b1d300"},
    {"email": "695418206@qq.com",
      "from": "web",
      "product": "master-online",
      "pw": "f2d8ddfc169a0ee6f8b0ecd924b1d300"}]

class TestLogin(unittest.TestCase):

    @parameterized.expand(data)
    def test_login_success(self, email, from_, product, pw):
        self.url = "https://userapi.edrawsoft.cn/api/user/login"
        res = requests.post(self.url, data={"email": email, "from": from_, "product": product, "pw": pw})
        print(res.status_code)
if __name__ == '__main__':
    unittest.main()
