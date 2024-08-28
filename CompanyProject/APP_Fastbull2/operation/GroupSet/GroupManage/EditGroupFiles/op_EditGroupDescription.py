# 2page(页面对象)：封装对元素的操作，一个页面封装成一个对象
# coding: utf-8
# import sys
# sys.path.append("..") #相对路径或绝对路径
import time

from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d

# 取消更新
# d(description="取消").click()
class GroupDescription(Base1):
    # 群介绍
    description = d.xpath('//*[contains(@content-desc,"群介绍")]')
    inputgroupdescription = d.xpath('//android.widget.EditText')

    def input_groupdescription(self,text):
        self.inputgroupdescription.clear_text()
        self.inputgroupdescription.set_text(text)

    # 完成
    # complete = d.xpath('//*[@content-desc="完成"]')

    cancel = d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.imageview[实例25_批量生成PPT版荣誉证书]')
    complete = d(description="完成")

    def click_complete(self):
        self.complete.click()

    # sure = d.xpath('//*[@content-desc="确定"]')


    # 取消编辑群介绍
    def editgroupdescription_cancel(text):
        # ManageGroup().manage_groups()
        ManageGroup().click_editGroupProfile()
        GroupDescription().description.click()
        GroupDescription().input_groupdescription(text)
        # GroupDescription().cancel.click()
        GroupDescription().click_complete()

    # 编辑成功
    def editgroupdescription_set(text):
        # ManageGroup().manage_groups()
        ManageGroup().click_editGroupProfile()
        GroupDescription().description.click()
        GroupDescription().inputgroupdescription.set_text(text)
        GroupDescription().complete.click()

    # 清空输入框
    def editgroupdescription_clear(self):
        # ManageGroup().manage_groups()
        ManageGroup().click_editGroupProfile()
        GroupDescription().description.click()
        GroupDescription().inputgroupdescription.clear_text()
        GroupDescription().complete.click()


if __name__ == '__main__':
    text = '这是群介绍'
    GroupDescription().editgroupdescription_set(text)

