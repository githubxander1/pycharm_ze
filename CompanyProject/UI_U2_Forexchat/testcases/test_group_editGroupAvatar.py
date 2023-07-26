
# coding: utf-8
import time
import unittest

from CompanyProject.UI_U2_Forexchat.base.basePage import Base1
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.EditGroupFiles.op_EditGroupAvatar import GroupAvatar
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class Test_editGroupAvatar(Base1):
    name='编辑群头像'
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

    def test_editGroupAvatar_set_sus(self):
        GroupAvatar().editGroupAvatar_set()

    def test_editGroupAvatar_set_sus1(self):
        GroupAvatar().editGroupAvatar_set()

    def test_editGroupAvatar_set_sus2(self):
        GroupAvatar().editGroupAvatar_set()


if __name__ == "__main__":
    unittest.main()
#     def setup(self):
#         pass
#     def teardown(self):
#         pass
#
#         # 编辑群头像成功
#     def test_editGroupAvatar_set_sus(self):
#         GroupAvatar().editGroupAvatar_set()
#
#         # toast=d.xpath('//*[@content-desc="头像设置成功"]')
#         # print(toast)
#     #   assert d.toast.get_message() == toast
#
# if __name__ == '__main__':
#      pytest.main(["-s","-v","--html=Outputs/reports/pytest.html",
#                   "--alluredir=Outputs/allure"])   # allure文件生成的目录



