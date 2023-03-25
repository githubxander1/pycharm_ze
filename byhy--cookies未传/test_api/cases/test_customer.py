from byhy.test_api.lib.webapi import APIMgr
# coding:utf-8


# import unittest
import pytest

import libs


class Test_customer:
    name = '客户'

    # 初始化方法
    def setup(self):
        APIMgr().mgr_login('byhy--cookies未传', 88888888)
        # APIMgr().customer_del_all()

    # 清除方法
    def teardown(self):
        pass

    def test_customerAdd_sus(self):
        customer_add = APIMgr().customer_add('测试',
                                             '13345679934',
                                             "武汉市桥西医院北路")
        print(customer_add)
        assert customer_add.json()['ret'] == 0

if __name__=='__main__':
    # unittest.main()
    pytest.main()