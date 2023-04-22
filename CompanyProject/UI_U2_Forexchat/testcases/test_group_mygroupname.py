
# coding: utf-8


from pg_groupSet import d,mynickname,nameinput,complete

from Company_project.UI_U2_Forexchat.operation.GroupSet import  manage_groups



d.implicitly_wait(10)


class test_mygroupname:
    name='群名称'

    def setup(self):
        d.app_start('com.sy.fxchat')

    def teardown(self):

        # 编辑群头像成功
    def test_nickname_sus(self,name):
        manage_groups()
        mynickname.click()
        nameinput.send_keys(name)
        complete.click()




