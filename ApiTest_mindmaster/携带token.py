# /api/user/23928516/subscription/mindmaster
import unittest
from middleware.helper import save_token
class TestRecharge(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_recharge(self):
        # save_token()
        # token = Context.token

        token = save_token()
        print(token)
        # params = token
        # res = requests.get(url='https://masterapi.edrawsoft.cn/api/oss/23928516?token='+token)
        # print(res.json())
if __name__ == '__main__':
    unittest.main()