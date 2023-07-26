import unittest
import time

import logging
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')



class Test_groupDescription(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 在测试类中，setUpClass() 方法会在所有测试用例执行前自动调用一次
        Base1().startApp()
        time.sleep(3)
        Home().click_conversation()
        GroupWindow().click_groupSet()
        time.sleep(2)
        GroupSet().slide_down()

    @classmethod
    def tearDownClass(cls):
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    def test_nickname_set_sus(self):
        text = '群昵称-第一次'
        GroupSet().nickname_set(text)

    def test_nickname_set_sus2(self):
        text = '群昵称-第二次'
        GroupSet().nickname_set(text)

    def test_nickname_set_sus3(self):
        text = '群昵称-第三次'
        GroupSet().nickname_set(text)



if __name__ == "__main__":
    unittest.main()