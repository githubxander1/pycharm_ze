import time
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class ManageGroup(Base1):
    editgroupprofile = d(description="编辑群资料")
    adminset = d.xpath('//*[contains(@content-desc,"设置管理员")]')
    groupMute = d(description="设置群内禁言")
    addFriend = d(description="禁止群内成员互加好友")
    groupadditionMethod = d(description="加群方式")
    groupBlacklist = d(description="群黑名单")
    transferGroup = d(description="转让群")

    # 进入管理群
    def manage_groups(self):
        # 进入会话
        Home().click_conversation()
        # 点击群设置
        GroupWindow().group_set.click()
        # 点击管理群
        # 垂直向前滚动到指定位置（横向同理）
        d(scrollable=True).scroll.forward.to(description="管理群")
        time.sleep(3)
        d(description="管理群").click()

    # 点击编辑群资料
    def editgroupprofile_click(self):
        ManageGroup().editgroupprofile.click()

    # 点击管理员
    def group_admin_add(self):
        ManageGroup().manage_groups()
        d.xpath('//*[contains(@content-desc,"管理员"]').click()
