import os
import time
import unittest
import pytest
import allure

from CompanyProject.UI_U2_Forexchat.base.basePage import Base1
from CompanyProject.UI_U2_Forexchat.common.common import take_screenshot
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupAvatar import GroupAvatar
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup

class Test_editGroupAvatar(unittest.TestCase):
    name = '编辑群头像'

    @classmethod
    def setUpClass(cls):
        Base1().startApp()
        ManageGroup().manage_groups()
        ManageGroup().click_editGroupProfile()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.story('编辑群头像-设置成功')
    # def test_editGroupAvatar_set_sus(self):
    #     GroupAvatar().editGroupAvatar_set_sus()

    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.story('编辑群头像-查看')
    def test_editGroupAvatar_view(self):
        GroupAvatar().editGroupAvatar_view()
        take_screenshot()


if __name__ == '__main__':
    pytest.main()
    # Run the tests and generate the Allure report
    # pytest.main(['-s', '-v', '--alluredir', 'allure_reports'])
    #
    # Generate the Allure report
    # os.system(f"allure generate {'allure_reports'} -o {'allure_reports'}/html")
    # pytest.main(['-s', '--alluredir=../allure-results', 'test_editgroup_nickname.py'])
    # os.system('allure generate ../allure-results -o open ../allure-results/report/html --clean ')

