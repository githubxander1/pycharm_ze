# -*- coding:utf-8 -*-
from interface.user import user_info
from commen.headle_token import *
import unittest, os
current_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前路径
# 获取 token 的路径
token_path = os.path.join(current_path, "commen")
token_path = os.path.join(token_path, "token.sina.yaml")


class TestUserInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token = get_yaml(token_path)
        print("获取token")
        print(cls.token)

    def test_user_info_success(self):
        r = user_info("https://api.xdclass.net", self.token)
        print(r.text)


if __name__ == '__main__':
    unittest.main()

