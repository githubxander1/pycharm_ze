
# coding: utf-8
import time
import uiautomator2 as u2

from op_ManageGroup import  d,manage_groups,editgroupprofile,name,inputgroupname,cancel,sure,complete
# from ele import d,manage_groups,editgroupprofile,name,inputgroupname,cancel,sure,complete

# d=u2.connect('127.0..1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新

if d(description="取消").exists:
    d(description="取消").click()
else:
    pass
# 取消更新
# def update():
#     if d(description="取消").exists:
#         d(description="取消").click()
#     else:
#         pass

# 取消编辑群名称
def editgroupname_cancel(nameinput):
    manage_groups()
    editgroupprofile.click()
    name.click()
    inputgroupname.send_keys(nameinput)
    cancel.click()
    sure.click()

# 编辑群名称成功
def editgroupname_set(nameinput):
    manage_groups()
    editgroupprofile.click()
    name.click()
    inputgroupname.send_keys(nameinput)
    complete.click()

# 清空输入框
def editgroupname_clear():
    manage_groups()
    editgroupprofile.click()
    name.click()
    inputgroupname.clear_text()
    complete.click()

#
if __name__ == '__main__':
    editgroupname_cancel('群主-269')
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    # editgroupname_set('群主-1314')


