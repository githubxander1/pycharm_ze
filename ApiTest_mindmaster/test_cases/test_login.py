import unittest
# from common.requests_handler import RequestsHandler
from pprint import pprint

from ApiTest_mindmaster.common.requests_handler import RequestsHandler


class LoginTest(unittest.TestCase):
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()
    # pass

    def tearDown(self):
        self.req.close_session()
    # pass

    def test_login_success(self):
        login_url = 'https://userapi.edrawsoft.cn/api/user/login'
        payload={
              'email': "2695418206@qq.com",
              'from': "web",
              'product': "master-online",
              'pw': "f2d8ddfc169a0ee6f8b0ecd924b1d300"
              }

        res = self.req.visit('post', login_url, json=payload)
        pprint(res['data'])
        self.assertEqual('success', res['status'])


if __name__ == '__main__':
    unittest.main()