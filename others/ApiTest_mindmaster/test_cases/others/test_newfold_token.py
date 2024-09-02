import unittest
# from common.requests_handler import RequestsHandler
from pprint import pprint

from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler
from ApiTest_mindmaster.middleware.helper import save_token, Context


class LoginTest(unittest.TestCase):
    def setUp(self):
        # 请求类实例化
        self.req = RequestsHandler()

        # pass

    def tearDown(self):
        self.req.close_session()
    # pass

    def test_newfold_success(self):
        # save_token()
        # token=Context.token
        token=save_token()
        print(token)
        newfold_url = 'https://masterapi.edrawsoft.cn/api/oss/23928516/obj'
        data = {
            "prefix": "新建1",
            # "id": 23928516
        }
        headers = {'Authorization':token}

        res = self.req.visit('post', newfold_url,headers=headers,json=data)
        # pprint(res['data'])
        pprint(res)
        # self.assertEqual('success', res['status'])


if __name__ == '__main__':
    unittest.main()