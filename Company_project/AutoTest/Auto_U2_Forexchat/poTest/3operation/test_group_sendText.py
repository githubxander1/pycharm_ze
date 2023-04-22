
# coding: utf-8
import time
import uiautomator2 as u2



from op_ManageGroup import  manage_groups

from op_GroupWindow import send_text

d.implicitly_wait(10)
from basePage import BasePage

class test_sendText(BasePage):
    name='发送文本'

    def setup(self):
        self.d = u2.connect('127.0.0.1:21503')
        self.d.app_start('com.sy.fxchat')

    def teardown(self):
        pass

        # 编辑群头像成功
    def test_sendText_sus(self):
        send_text('fdsfd')




