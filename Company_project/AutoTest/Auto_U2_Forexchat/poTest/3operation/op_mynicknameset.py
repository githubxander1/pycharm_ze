
# coding: utf-8
import time
import uiautomator2 as u2


# from ele import d,mynickname,nameinput,complete

from pg_groupSet import  d,mynickname,nameinput,complete
from op_ManageGroup import manage_groups


# d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
# d(description="取消").click()


# 编辑群头像成功
def nickname_set(name):
    manage_groups()
    mynickname.click()
    nameinput.send_keys(name)
    complete.click()




#
if __name__ == '__main__':
    nickname_set('我的群昵称')

