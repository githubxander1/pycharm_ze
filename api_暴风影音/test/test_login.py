#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:张红
import unittest
import requests
import time as t
# ttfrom page.login import login
# from page.login import headers
# from utils.operationJson import readJson
# from utils.operationJson import readYaml
from api_暴风影音.page.login import headers
from api_暴风影音.utils.operationJson import readYaml


class LoginTest(unittest.TestCase):


    def setUp(self) -> None:
        t.sleep(2)

    # 这个pass是后续没有任何操作
    def tearDown(self) -> None:
        pass

    # 测试首页
    def test_fengbao_index(self):
        r = requests.get(
            url=readYaml()['url']['nameport']+'/interface/index',
            headers=headers()
        )
        self.assertEqual(r.json()['count']['api'],0)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)