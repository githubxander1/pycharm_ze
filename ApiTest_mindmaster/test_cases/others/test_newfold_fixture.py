import unittest
# from common.requests_handler import RequestsHandler
from pprint import pprint

from ApiTest_mindmaster.common.requests_handler import RequestsHandler


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

    def test_newfold_success(self):
        login_url = 'https://userapi.edrawsoft.cn/api/user/login'
        payload = {
            'email': "2695418206@qq.com",
            'from': "web",
            'product': "master-online",
            'pw': "f2d8ddfc169a0ee6f8b0ecd924b1d300"
        }

        res = self.req.visit('post', login_url, json=payload)

        # 获取保存token
        token = res['data']['token']
        token = 'Bearer' + ' ' + token
        print(token)
        # token放到请求头中
        headers = {
            'Authorization': token
        }

        newfold_url = 'https://masterapi.edrawsoft.cn/api/oss/23928516/obj'
        data = {
            "prefix": "新建",
            # "id": 23928516
        }

        res = self.req.visit('post', newfold_url, headers=headers,json=data)
        # pprint(res['data'])
        pprint(res)
        self.assertEqual('success', res['status'])


if __name__ == '__main__':
    unittest.main()