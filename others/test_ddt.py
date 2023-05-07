import unittest
import ddt


# 装饰类
@ddt.ddt
class DdtDemo(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 装饰方法
    @ddt.data(("15312344578", "12345678"), ("15387654321", "12345678"))
    @ddt.unpack
    def test_ddt(self, username, password):
        print(username, password)


if __name__ == '__main__':
    unittest.main(verbosity=2)