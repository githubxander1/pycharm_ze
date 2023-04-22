
# coding: utf-8
import time
import uiautomator2 as u2
import pytest

from CompanyProject.UI_U2_Forexchat.base.basePage import Base1
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupAvatar import GroupAvatar



class Test_editGroupAvatar(Base1):
    name='编辑群头像'

    def setup(self):
        pass
    def teardown(self):
        pass

        # 编辑群头像成功
    def test_editGroupAvatar_set_sus(self):
        GroupAvatar().editGroupAvatar_set()

        # toast=d.xpath('//*[@content-desc="头像设置成功"]')
        # print(toast)
    #   assert d.toast.get_message() == toast

if __name__ == '__main__':
     pytest.main(["-s","-v","--html=Outputs/reports/pytest.html",
                  "--alluredir=Outputs/allure"])   # allure文件生成的目录



