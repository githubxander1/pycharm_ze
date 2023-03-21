import time

import uiautomator2 as u2

# 连接模拟器或手机
from Company_project.AutoTest.Auto_U2_Forexchat.base.base import session1, groupSet

d=u2.connect('127.0.0.1:21513')

d.app_start('com.sy.fxchat')

d(description="取消").click()

