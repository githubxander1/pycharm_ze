import unittest
# from common.requests_handler import RequestsHandler
from pprint import pprint
from parameterized import parameterized

from others.ApiTest_mindmaster.common.requests_handler import RequestsHandler
from ApiTest_mindmaster.middleware.helper import save_token

data={'prefix':'test_新建'}

class TestNewFold(unittest.TestCase):

    def setupClass(self):
        '''整个测试过程中只执行一次'''
        pass
    def teardownClass(self):
        pass

    def setUp(self):
        '''每个测试方法执行之前都会先调用的方法'''
        # 请求类实例化
        self.req = RequestsHandler()

    def tearDown(self):
        '''每个测试方法执行后都会调用的方法'''
        self.req.close_session()

    @parameterized.expand(data)
    def test_newfold_success(self):
        # save_token()
        # token=Context.token
        token = save_token()
        print(token)
        newfold_url = 'https://masterapi.edrawsoft.cn/api/oss/23928516/obj'
        # data = {
        #     "prefix": "新建1",
        #     # "id": 23928516
        # }
        headers = {'Authorization': token}

        res = self.req.visit('post', newfold_url, headers=headers, json=data)
        # pprint(res['data'])
        pprint(res)
        # self.assertEqual('success', res['status'])


if __name__ == '__main__':
    unittest.main()