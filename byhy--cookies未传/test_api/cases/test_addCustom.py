import unittest

# from byhy--cookies未传.test_api.lib import webapi
from byhy.test_api.lib.webapi import APIMgr

url='http://127.0.0.1'
class addCustomser(unittest.TestCase):
    def setUp(self) :
        # self.logininfo = api1.libApi.loginApi('byhy--cookies未传', '88888888')
        # self.logininfo = webapi.APIMgr.mgr_login('byhy--cookies未传', '88888888')
        APIMgr().mar_login('byhy--cookies未传', '88888888')

    def tearDown(self) -> None:
        pass
    # @classmethod
    def test_customeradd_sus(self):
        # re = api1.libApi().customer_add('小米', 15318544154, '宝安区新安街道')
        # re = webapi.APIMgr.customer_add('小米', 15318544154, '宝安区新安街道')
        # self.login=requests.post(url + '/api/mgr/signin',
        #                    data={
        #                        'username': 'byhy--cookies未传',
        #                        'password': 88888888
        #                    })
        self.logininfo = api1.libApi().loginApi('byhy--cookies未传', 88888888)
        s=self.response.Session()
        self.add=s.post(url+"/api/mgr/customers",
                          json={
                                "action":"add_customer",
                                "data":{
                                    "name":'新增测试1',
                                    "phonenumber":15318544154,
                                    "address":'测试地址1'
                                }
                            })
        self.assertEqual(0, self.add.json())


if __name__ == '__main__':
    unittest.main()
