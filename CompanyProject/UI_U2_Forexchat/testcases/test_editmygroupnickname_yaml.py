import unittest
import time

import logging

import pytest

from CompanyProject.UI_U2_Forexchat.common.common import take_screenshot
from CompanyProject.UI_U2_Forexchat.data.load_testdata import load_yamldata
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Test_group_nickname():
    def setup_class(cls):
        # 在测试类中，setUpClass() 方法会在所有测试用例执行前自动调用一次
        Base1().startApp()
        time.sleep(6)
        Home().click_conversation()
        GroupWindow().click_groupSet()
        time.sleep(2)
        GroupSet().slide_down()


    def teardown_class(cls):
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    @pytest.mark.parametrize('nickname', load_yamldata()['groupNickName'])
    def test_nickname_set(self,nickname):
        GroupSet().nickname_set(nickname['text'])

        d.implicitly_wait(10)
        if GroupSet.disbandgroup.exists:
            time.sleep(2)
            if GroupSet().disbandgroup.exists:
                take_screenshot()
                print('截图成功')
            else:
                print('未截图')




if __name__ == "__main__":
    pytest.main()