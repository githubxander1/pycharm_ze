import time

import pytest

from CompanyProject.APP_Fastbull2.base.basePage import Base1
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupAvatar import GroupAvatar
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupName import GroupName
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ForbidFriendAdd import ForbidFriendAdd
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup


class Test_editGroupName(Base1):
    name='编辑群名称'

    def setUpClass(cls):
        Base1().startApp()
        ManageGroup().manage_groups()
        # ManageGroup().click_editGroupProfile()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

        # 编辑群头像成功
    def test_editgroupname_set(self):
        nameinput = '群主-269'
        ForbidFriendAdd().friendAdd_set()
    #   assert d.toast.get_message() == toast

if __name__ == '__main__':
     pytest.main(["-s","-v",'test_group_editGroupName.py',
                  "--alluredir=Outputs/allure"])   # allure文件生成的目录
