
# coding: utf-8
import time
import uiautomator2 as u2


# from ele import d,groupMute,switch

from op_ManageGroup import  ManageGroup
from basePage import Base1, d
# d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()


# 编辑群头像成功
def mute_set():
    manage_groups()
    groupMute.click()
    switch.click()



#
if __name__ == '__main__':
    mute_set()

