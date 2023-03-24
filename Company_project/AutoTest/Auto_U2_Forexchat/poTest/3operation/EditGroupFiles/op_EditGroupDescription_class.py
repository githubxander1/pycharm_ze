# 2page(页面对象)：封装对元素的操作，一个页面封装成一个对象
# coding: utf-8
import time
import uiautomator2 as u2
# from ele import EditGroupProfile,Description,InputGroupDescription,Cancel,Sure,complete
# from op_ManageGroup import manage_groups
from op_ManageGroup_class  import ManageGroup

manageGroup=ManageGroup()
d=u2.connect('127.0.0.1:21513')

d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()

# 取消编辑群介绍
def editGroupDescription_cancel(DescriptionInput):
    manageGroup.manage_groups()
    EditGroupProfile.click()
    Description.click()
    InputGroupDescription.send_keys(DescriptionInput)
    Cancel.click()
    Sure.click()

# 编辑成功
def editGroupDescription_set(editGropDescription_textInput):
    manage_groups()
    EditGroupProfile.click()
    Description.click()
    InputGroupDescription.send_keys(editGropDescription_textInput)
    complete.click()

# 清空输入框
def editGroupDescription_clear():
    manage_groups()
    EditGroupProfile.click()
    Description.click()
    InputGroupDescription.clear_text()
    complete.click()

#
if __name__ == '__main__':
    # editGroupDescription_cancel('群介绍：取消')
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    # editGroupDescription_set('群介绍：感受到丰田供热')
    # time.sleep(3)
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    editGroupDescription_clear()
    toasts = d.toast.get_message()
    # toasts2 = d.toast.show()
    print(toasts)
