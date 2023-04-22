from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d


class GroupMute(Base1):
    group_mute = d(description="设置群内禁言")
    switch = d.xpath('//android.widget.Switch')

    def mute_set(self):
        ManageGroup().manage_groups()
        GroupMute().group_mute.click()
        GroupMute().switch.click()




if __name__ == '__main__':
    GroupMute().mute_set()

