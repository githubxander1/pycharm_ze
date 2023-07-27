
# coding: utf-8
import time
import unittest
import HTMLTestRunner

from CompanyProject.UI_U2_Forexchat.base.basePage import Base1
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupAvatar import GroupAvatar
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup


class Test_editGroupAvatar(unittest.TestCase):
    name='编辑群头像'
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

    # def test_editGroupAvatar_set_sus(self):
    #     GroupAvatar().editGroupAvatar_set_sus()

    def test_editGroupAvatar_view(self):
        GroupAvatar().editGroupAvatar_view()



if __name__ == "__main__":
    # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(stream='test_reports', title='Test Report'))
    unittest.main()
    # Open the test report file
    with open('report_path', "w") as f:
        # Create an HTMLTestRunner instance
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Test Report', description='')
        # Run the tests and generate the test report
        runner.run(unittest.makeSuite(Test_editGroupAvatar))
