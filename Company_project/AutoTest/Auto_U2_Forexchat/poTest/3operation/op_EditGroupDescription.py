# 2page(页面对象)：封装对元素的操作，一个页面封装成一个对象
# coding: utf-8
import time
import uiautomator2 as u2
from op_ManageGroup import manage_groups
from ele import editgroupprofile,description,inputgroupdescription,cancel,sure,complete

d=u2.connect('127.0.0.1:21513')

d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()

# 取消编辑群介绍
def editgroupdescription_cancel(descriptioninput):
    manage_groups()
    editgroupprofile.click()
    description.click()
    inputgroupdescription.send_keys(descriptioninput)
    cancel.click()
    sure.click()

# 编辑成功
def editgroupdescription_set(editgropdescription_textinput):
    manage_groups()
    editgroupprofile.click()
    description.click()
    inputgroupdescription.send_keys(editgropdescription_textinput)
    complete.click()

# 清空输入框
def editgroupdescription_clear():
    manage_groups()
    editgroupprofile.click()
    description.click()
    inputgroupdescription.clear_text()
    complete.click()

#
if __name__ == '__main__':
    # editgroupdescription_cancel('群介绍：取消')
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    # editgroupdescription_set('群介绍：感受到丰田供热')
    # time.sleep(3)
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    editgroupdescription_clear()
    toasts = d.toast.get_message()
    # toasts2 = d.toast.show()
    print(toasts)
