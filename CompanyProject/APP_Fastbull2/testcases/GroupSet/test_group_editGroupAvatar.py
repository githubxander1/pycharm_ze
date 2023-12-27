import os
import time
import unittest
import pytest
import allure

from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.common.common import Common
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupAvatar import GroupAvatar
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup

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
    @pytest.mark.skip()
    def test_editGroupAvatar_view(self):
        GroupAvatar().editGroupAvatar_view()
        file_basename=os.path.basename(__file__)
        sc_name='头像-预览'
        try:
            GroupAvatar().avatar.wait(10)
            Common().take_screenshot(file_basename,sc_name)
        except:
            print('元素不存在，未截图')
    def test_editGroupAvatar_album(self):
        GroupAvatar().editGroupAvatar_album()
        file_basename=os.path.basename(__file__)
        sc_name='头像—相册'
        if GroupAvatar().avatar.exists:
            Common().take_screenshot(file_basename,sc_name)
        # try:
        #     GroupAvatar().avatar.wait(10)
        #     common().take_screenshot(file_basename,sc_name)
        # except:
        #     print('元素不存在，未截图')
        print(d.toast.get_message())
        # assert d.toast.get_message()=='头像设置成功'



if __name__ == '__main__':
    pytest.main(['-vs', 'test_editGroupAvatar.py'])
    # Run the tests and generate the Allure report
    # pytest.main(['-s', '-v', '--alluredir', 'allure_reports'])
    #
    # Generate the Allure report
    # os.system(f"allure generate {'allure_reports'} -o {'allure_reports'}/html")
    # pytest.main(['-s', '--alluredir=../allure-results', 'test_editgroup_nickname.py'])
    # os.system('allure generate ../allure-results -o open ../allure-results/report/html --clean ')

