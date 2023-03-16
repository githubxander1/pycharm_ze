import requests
import unittest
import openpyxl

from byhy.test_api.lib import webapi

class login(unittest.TestCase):
    def setup(self):
        pass

    def teardowm(self):
        pass

    def test_login_sus(self):
        self.logininfo = webapi.APIMgr().mgr_login('byhy', 88888888)
        print(self.logininfo)
        self.assertEqual(self.logininfo.json()['ret'],0)

    # def test_login_wrongUser(self):
    #     self.logininfo = api1.libApi().loginApi('yhy', 88888888)
    #     # print(self.logininfo.json())
    #     # self.assertEqual(self.logininfo.text()['ret'], 1)
    #
    # def test_login_wrongPass(self):
    #     self.logininfo = api1.libApi().loginApi('byhy', 8888888)
    #     # print(self.logininfo.json())
    #     # self.assertEqual(self.logininfo.text()['ret'], 1)
    #

if __name__ == 'main':
    unittest.main()
