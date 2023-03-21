# page(页面对象)：封装对元素的操作，一个页面封装成一个对象
# coding: utf-8
import time
import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.base import EditProfile
from Company_project.AutoTest.Auto_U2_Forexchat.base.operate import manage_groups
from Company_project.AutoTest.Auto_U2_Forexchat.page import EditGroupProfile, Description, Cancel, Sure, \
    InputGroupDescription

# from Company_project.AutoTest.Auto_U2_Forexchat.base.EditProfile
# from Company_project.AutoTest.Auto_U2_Forexchat.base import EditGroupProfile, Description, Input, Cancel, Sure
EditProfile()

d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()

class EditDescription:

    # 点击编辑群资料
    def EditGroupProfile_click(self):
        EditGroupProfile.click()

    # 点击群介绍
    def Description_click(self):
        Description.click()

    # 输入群介绍文案
    def InputGroupDescription(self,editGropDescription_textInput):
        InputGroupDescription.send_keys(editGropDescription_textInput)

    def Cancel_click(self):
        Cancel.click()

    def Sure_click(self):
        Sure.click()

    def group_editGroupProfiles(self,editGropDescription_textInput):
        manage_groups()
        self.EditGroupProfile_click()
        self.Description_click()
        self.InputGroupDescription(editGropDescription_textInput)
        self.Cancel_click()
        self.Sure_click()



if __name__ == '__main__':
    EditDescription().group_editGroupProfiles('群介绍：感受到丰田供热')
    time.sleep(3)
    # d.app_stop('com.sy.fxchat')


