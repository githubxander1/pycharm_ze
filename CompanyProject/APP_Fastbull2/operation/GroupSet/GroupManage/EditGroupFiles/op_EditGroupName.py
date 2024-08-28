from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d

class GroupName(Base1):
    # 群名称
    name = d.xpath('//*[contains(@content-desc,"群名称")]')
    # inputgroupname = d(className="android.widget.edNittext")
    inputgroupname = d.xpath('//*[contains(@content-desc,"编辑群名称")]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]/android.widget.edNittext')

    cancel = d.xpath('//*[contains(@content-desc,"编辑群名称")]/android.widget.imageview[实例25_批量生成PPT版荣誉证书]')
    complete = d(description="完成")
    sure = d.xpath('//*[@content-desc="确定"]')

    # 取消编辑群名称
    def editgroupname_cancel(nameinput):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupName().name.click()
        GroupName().inputgroupname.clear_text()
        GroupName().inputgroupname.send_keys(nameinput)
        # GroupName().cancel.click()
        GroupName().sure.click()

    # 编辑群名称成功
    def editgroupname_set(nameinput):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupName().name.click()
        GroupName().inputgroupname.clear_text()
        GroupName().inputgroupname.send_keys(nameinput)
        GroupName().complete.click()

    # 清空输入框
    def editgroupname_clear(self):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupName().inputgroupname.clear_text()
        GroupName().name.click()
        GroupName().complete.click()


if __name__ == '__main__':
    GroupName().nameinput='群主-269'
    GroupName().editgroupname_set()


