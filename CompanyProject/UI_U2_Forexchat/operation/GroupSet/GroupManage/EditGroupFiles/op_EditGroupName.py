from Company_project.UI_U2_Forexchat.operation.GroupSet import ManageGroup
from Company_project.UI_U2_Forexchat import Base1, d

class GroupName(Base1):
    # 群名称
    name = d.xpath('//*[contains(@content-desc,"群名称")]')
    inputgroupname = d(className="android.widget.edNittext")

    cancel = d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.imageview[1]')
    complete = d(description="完成")
    sure = d.xpath('//*[@content-desc="确定"]')

    # 取消编辑群名称
    def editgroupname_cancel(nameinput):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupName().name.click()
        GroupName().inputgroupname.send_keys(nameinput)
        GroupName().cancel.click()
        GroupName().sure.click()

    # 编辑群名称成功
    def editgroupname_set(nameinput):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupName().name.click()
        GroupName().inputgroupname.send_keys(nameinput)
        GroupName().complete.click()

    # 清空输入框
    def editgroupname_clear(self):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        ManageGroup().name.click()
        ManageGroup().inputgroupname.clear_text()
        ManageGroup().complete.click()

#
if __name__ == '__main__':
    nameinput='群主-269'
    GroupName().editgroupname_cancel(nameinput)
    # d.app_stop('com.sy.fxchat')
    # time.sleep(3)
    # editgroupname_set('群主-1314')


