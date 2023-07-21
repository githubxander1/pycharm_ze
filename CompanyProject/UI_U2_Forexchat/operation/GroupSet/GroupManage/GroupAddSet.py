from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d

class GroupAdd(Base1):
    groupAddMethod = d(description="加群方式")
    anyone = d(description="允许任何人加群")
    needVerify = d(description="需要发送验证消息")
    NoneAllowed= d(description="不允许任何人加群")

    def click_groupAddMethod(self):
        self.groupAddMethod.click()

    def click_anyone(self):
        self.anyone.click()

    def click_needVerify(self):
        self.needVerify.click()

    def click_forbid(self):
        self.NoneAllowed.click()

    # 加群方式
    def groupAdd_set(self):
        ManageGroup().manage_groups()
        ManageGroup().click_groupAddMethod()
        self.click_anyone()



#
if __name__ == '__main__':
    GroupAdd().groupAdd_set()

