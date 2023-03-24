
# coding: utf-8
import time
import uiautomator2 as u2


from ele import editgroupprofile,name,inputgroupname,cancel,sure,complete,avatar,defaultavatar,avatar1

from op_ManageGroup import  manage_groups


d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()


# 编辑群头像成功
def editGroupAvatar_set():
    manage_groups()
    editgroupprofile.click()
    avatar.click()
    defaultavatar.click()
    avatar1.click()



#
if __name__ == '__main__':
    editGroupAvatar_set()

