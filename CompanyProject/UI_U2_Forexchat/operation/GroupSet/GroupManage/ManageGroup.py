import time
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class ManageGroup(Base1):
    editGroupGrofile = d(description="编辑群资料")
    adminSet = d.xpath('//*[contains(@content-desc,"设置管理员")]')
    groupMute = d(description="设置群内禁言")
    addFriend = d(description="禁止群内成员互加好友")
    groupAddMethod = d(description="加群方式")
    groupBlacklist = d(description="群黑名单")
    transferGroup = d(description="转让群")

    # 点击编辑群资料
    def click_editGroupProfile(self):
        self.editGroupGrofile.click()

    def click_adminset(self):
        self.adminSet.click()

    def click_groupMute(self):
        self.groupMute.click()

    def click_addFriend(self):
        self.addFriend.click()

    def click_groupAddMethod(self):
        self.groupAddMethod.click()

    def click_groupBlacklist(self):
        self.groupBlacklist.click()

    def click_transferGroup(self):
        self.transferGroup.click()

    # 进入管理群
    def manage_groups(self):
        time.sleep(5)
        # 进入会话
        Home().click_conversation()
        # 点击群设置
        GroupWindow().click_groupSet()
        # 点击管理群
        # 垂直向前滚动到指定位置（横向同理）
        while not d(description="管理群").exists():
            d(scrollable=True).scroll.forward()
            time.sleep(1)
        d(description="管理群").click()




