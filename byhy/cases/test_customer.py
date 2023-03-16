import unittest
from byhy.test_api.lib import webapi
import requests

class Test_customer(unittest.TestCase):

    # def __int__(self):

    def setUp(self) -> None:
        self.api=webapi.APIMgr()
        self.api.mgr_login('byhy',88888888)

    # def __int__(self):
        self.s=requests.Session()

    def tearDown(self) -> None:
        pass
    def test_addCustomer(self):
        add_customer=webapi.APIMgr()
        add_customer.customer_add('28','2','dataInExcel')


if __name__=='__main__':
    unittest.main()