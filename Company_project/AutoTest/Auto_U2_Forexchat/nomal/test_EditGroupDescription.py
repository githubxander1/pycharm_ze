import pytest
import time
import uiautomator2 as u2
d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
from Company_project.AutoTest.Auto_U2_Forexchat.nomal.EditGroupDescription import editGroupProfiles_set, \
    editGroupProfiles_clear


class Test_edit:
    def setup(self):
        editGroupProfiles_clear()

    def teardown(self):
        d.app_stop('com.sy.fxchat')

    def test_editDescription_sus(self):
        d.app_stop('com.sy.fxchat')
        time.sleep(3)

        editGroupProfiles_set('群介绍：感受到丰田供热')

        toasts=d.toast.get_message()
        print(toasts)
        assert toasts == '编辑成功'



if __name__ == '__main__':
    pytest.main()



