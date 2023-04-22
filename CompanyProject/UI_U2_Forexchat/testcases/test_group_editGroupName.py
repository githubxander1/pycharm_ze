import pytest

from CompanyProject.UI_U2_Forexchat.base.basePage import Base1
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupAvatar import GroupAvatar
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupName import GroupName
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ForbidFriendAdd import ForbidFriendAdd


class Test_editGroupAvatar(Base1):
    name='编辑群名称'

    def setup(self):
        pass
    def teardown(self):
        pass

        # 编辑群头像成功
    def test_editgroupname_set(self):
        nameinput = '群主-269'
        ForbidFriendAdd().friendAdd_set()
    #   assert d.toast.get_message() == toast

if __name__ == '__main__':
     pytest.main(["-s","-v",
                  "--alluredir=Outputs/allure"])   # allure文件生成的目录
