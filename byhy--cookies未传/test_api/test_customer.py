import unittest
from byhy.test_api.lib import webapi
import requests

class Test_customer(unittest.TestCase):
    name = '添加客户 - API-0151'
    # def __int__(self):

    def setUp(self) -> None:
        self.api=webapi.APIMgr()
        self.api.mgr_login('byhy--cookies未传',88888888)
        apimgr.mgr_login()
        apimgr.order_del_all()
        apimgr.customer_del_all()
        apimgr.medicine_del_all()

    # def __int__(self):
        self.s=requests.Session()

    def tearDown(self) -> None:
        apimgr.customer_del(self.addedCustomerId)

    def test_addCustomer(self):
        add_customer=webapi.APIMgr()
        add_customer.customer_add('28','2','dataInExcel')


if __name__=='__main__':
    unittest.main()