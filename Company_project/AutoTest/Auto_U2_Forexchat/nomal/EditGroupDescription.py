
# coding: utf-8
import time
import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.nomal import EditGroupProfile, Description, Cancel, \
    InputGroupDescription, Sure, complete

d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()

# 点击进入会话聊天窗口
def session1():
    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]').click()
    # d.xpath('//android.widget.ScrollView/android.view.View[2]').click()

  # 进入群设置
def groupSet():
    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]').click()

# 进入管理群
def manage_groups():
    # 进入会话
    session1()
    # 点击群设置
    groupSet()
    time.sleep(3)
    # 点击管理群
    d(scrollable=True).scroll.to(description="管理群")
    d(description="管理群").click()
# 取消编辑群介绍
def editGroupProfiles_cancel(editGropDescription_textInput):
    manage_groups()
    EditGroupProfile.click()
    Description.click()
    InputGroupDescription.send_keys(editGropDescription_textInput)
    Cancel.click()
    Sure.click()

# 编辑成功
def editGroupProfiles_set(editGropDescription_textInput):
    manage_groups()
    EditGroupProfile.click()
    Description.click()
    InputGroupDescription.send_keys(editGropDescription_textInput)
    complete.click()

# 清空输入框
def editGroupProfiles_clear():
    manage_groups()
    EditGroupProfile.click()
    Description.click()
    InputGroupDescription.clear_text()
    complete.click()

#
if __name__ == '__main__':
    # editGroupProfiles_cancel('群介绍：取消')
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    # editGroupProfiles_set('群介绍：感受到丰田供热')
    # time.sleep(3)
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    editGroupProfiles_clear()
    toasts = d.toast.get_message()
    # toasts2 = d.toast.show()
    print(toasts)


