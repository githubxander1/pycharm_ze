import unittest
import time

import logging
from CompanyProject.APP_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Forexchat.base.basePage import Base1
from CompanyProject.APP_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Forexchat.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Test_groupDescription(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base1().startApp()
        time.sleep(3)
        Home().click_conversation()
        GroupWindow().click_groupSet()
        time.sleep(2)
        Base1().d.click(0.917, 0.717)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    def test_saveQR(self):
        GroupSet().click_save()

    def test_shareQR(self):
        GroupSet().click_share()
        GroupWindow().forward_tofriendandgroup()
        GroupWindow().click_back()
        GroupWindow().click_back()
        GroupWindow().click_back()



if __name__ == "__main__":
    unittest.main()