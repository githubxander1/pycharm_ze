import unittest
import requests

class TestSignIn(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8047/api/mgr/signin'

    # 实例25_批量生成PPT版荣誉证书. 正确的用户名和密码，能够成功登录。
    def test_signin_success(self):
        data ={
            'username':'byhy',
            'password':88888888
        }
        response = requests.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, response.json()['ret'])

    # 2. 错误的用户名和密码，登录失败。
    def test_signin_fail(self):
        data ={
            'username':'byh',
            'password':12345678
        }
        response = requests.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, response.json()['ret'])
        self.assertEqual('用户名或者密码错误', response.json()['msg'])

    # 3. 不带用户名或密码，登录失败。
    def test_signin_empty(self):
        data ={
            'username':'',
            'password':''
        }
        response = requests.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('用户名或者密码错误', response.json()['msg'])

if __name__ == '__main__':
    unittest.main()
