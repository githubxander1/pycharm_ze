# from hyrobot.base import *

# import unittest
import pytest

import libs


class Test_login:
    name = '登录'

    # 初始化方法
    def setup(self):
        pass
        # apimgr.order_del_all()
        # apimgr.customer_del_all()
        # apimgr.medicine_del_all()

    #清除方法
    def teardown(self):
        pass

    def test_login_sus(self):
        from byhy.test_api.lib.webapi import APIMgr
        login= APIMgr().mgr_login('byhy', 88888888)
        # self.assertEqual(0,login.json()['ret'])
        assert 0==login.json()['ret']

if __name__=='__main__':
    # unittest.main()
    pytest.main()