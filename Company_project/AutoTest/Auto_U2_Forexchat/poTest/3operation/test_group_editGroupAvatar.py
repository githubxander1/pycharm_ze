
# coding: utf-8
import time
import uiautomator2 as u2
import pytest
import allure_pytest



from op_ManageGroup import manage_groups, editgroupprofile, avatar, defaultavatar, avatar1

from op_groupWindow import send_text

# from basePage import BasePage

d = u2.connect('127.0.0.1:21503') # ctrl+shift+1
d.app_start('com.sy.fxchat')
d.implicitly_wait(10) #ctr+1  F11切换
# ctrl+shift+F11

class Test_editGroupAvatar:
    name='编辑群头像'

    def setup(self):
        pass
    def teardown(self):
        pass

        # 编辑群头像成功
    def test_editGroupAvatar_set_sus(self):
        manage_groups()
        editgroupprofile.click()
        avatar.click()
        defaultavatar.click()
        time.sleep(5)
        avatar1.click()

        toast=d.xpath('//*[@content-desc="头像设置成功"]')
        print(toast)
    #   assert d.toast.get_message() == toast

if __name__ == '__main__':
     pytest.main(["-s","-v","--html=Outputs/reports/pytest.html",
                  "--alluredir=Outputs/allure"])   # allure文件生成的目录



