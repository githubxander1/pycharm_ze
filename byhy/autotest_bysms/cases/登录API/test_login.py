from byhy.test_api.lib.libapi import APIMgr

import unittest
import pytest

import libs


class Test_login(unittest.TestCase):
    name = '登录'

    # 初始化方法
    def setup(self):
        pass

    #清除方法
    def teardown(self):
        pass

    def test_login_sus(self):
        login= APIMgr().mgr_login('byhy', 88888888)
        print(login.json())
        # self.assertEqual(0,login.json()['ret'])
        assert 0==login.json()['ret']

    def test_login_userEm(self):
        login= APIMgr().mgr_login('', 88888888)
        print(login.json())
        # self.assertEqual(0,login.json()['ret'])
        assert 1 == login.json()['ret']

    def test_login_pwdEm(self):
        login= APIMgr().mgr_login('byhy', '')
        print(login.json())
        # self.assertEqual(0,login.json()['ret'])
        assert 1 == login.json()['ret']

if __name__=='__main__':
    # unittest.main()
    pytest.main()