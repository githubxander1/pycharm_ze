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
        Home().click_conversation()
        GroupWindow().click_groupSet()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    def test_1aditgrouintroduction_sus1(self):
        text = '群介绍-第一次'
        GroupSet().editgroupintroduction(text)

    def test_2aditgrouintroduction_sensitive(self):
        text = '群介绍-第二次'
        # 点击群介绍
        GroupSet().editgroupintroduction(text)

    def test_3aditgrouintroduction_sensitive(self):
        text = '第三次'
        GroupSet().editgroupintroduction(text)



if __name__ == "__main__":
    unittest.main()