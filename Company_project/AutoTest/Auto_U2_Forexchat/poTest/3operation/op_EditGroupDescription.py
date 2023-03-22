# 2page(页面对象)：封装对元素的操作，一个页面封装成一个对象
# coding: utf-8
import time
import uiautomator2 as u2


d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()


# 取消编辑群介绍
def group_editGroupProfiles(self,editGropDescription_textInput):
    manage_groups()
    self.EditGroupProfile_click()
    self.Description_click()
    self.InputGroupDescription(editGropDescription_textInput)
    self.Cancel_click()
    self.Sure_click()
#
# # 编辑群介绍
# def group_editGroupProfiles():
#     manage_groups()
#     d(description="编辑群资料").click()
#     d.xpath('//*[contains(@content-desc,"群介绍")]').click()
#     d(text="请输入群介绍").send_keys('群介绍：打扫房间独守空闺季拉开')
#     d.xpath('//*[@content-desc="完成"]').click()
#
# # 取消编辑群介绍
# def group_editGroupProfiles_cancel():
#     manage_groups()
#     d(description="编辑群资料").click()
#     d.xpath('//*[contains(@content-desc,"群介绍")]').click()
#     d(text="请输入群介绍").send_keys('群介绍：打扫房间独守空闺季拉开')
#     d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]').click()
#     d.xpath('//*[@content-desc="确定"]').click()

if __name__ == '__main__':
    EditDescription().group_editGroupProfiles('群介绍：感受到丰田供热')
    time.sleep(3)
    # d.app_stop('com.sy.fxchat')


