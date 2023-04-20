# 2page(页面对象)：封装对元素的操作，一个页面封装成一个对象
# coding: utf-8

# from op_ManageGroup import ManageGroup
from GroupMagema.op_ManageGroup import ManageGroup
from basePage import Base1, d


# 取消更新
# d(description="取消").click()
class GroupDescription(Base1):
    # 群介绍
    description = d.xpath('//*[contains(@content-desc,"群介绍")]')
    inputgroupdescription = d(className="android.widget.edittext")

    cancel = d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.imageview[1]')
    complete = d(description="完成")
    sure = d.xpath('//*[@content-desc="确定"]')


    # 取消编辑群介绍
    def editgroupdescription_cancel(descriptioninput):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupDescription().description.click()
        GroupDescription().inputgroupdescription.send_keys(descriptioninput)
        GroupDescription().cancel.click()
        GroupDescription().sure.click()

    # 编辑成功
    def editgroupdescription_set(editgropdescription_textinput):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupDescription().description.click()
        GroupDescription().inputgroupdescription.send_keys(editgropdescription_textinput)
        GroupDescription().complete.click()

    # 清空输入框
    def editgroupdescription_clear(self):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupDescription().description.click()
        GroupDescription().inputgroupdescription.clear_text()
        GroupDescription().complete.click()

#
if __name__ == '__main__':
    # editgroupdescription_cancel('群介绍：取消')
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    # editgroupdescription_set('群介绍：感受到丰田供热')
    # time.sleep(3)
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    # editgroupdescription_clear()
    # d.app_stop('com.bv.forexchat')
    editgropdescription_textinput = '这是群介绍'
    GroupDescription().editgroupdescription_set()
    # toasts = d.toast.get_message()
    # toasts2 = d.toast.show()
    # print(toasts)
