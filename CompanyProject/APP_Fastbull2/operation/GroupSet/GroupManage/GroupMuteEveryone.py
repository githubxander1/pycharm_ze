from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d


class GroupMute(Base1):
    group_mute = d(description="设置群内禁言")
    switch = d.xpath('//android.widget.Switch')


    def click_group_mute(self):
        self.group_mute.click()

    def click_switch(self):
        self.switch.click()

    def mute_set(self):
        ManageGroup().manage_groups()
        self.click_group_mute()
        self.click_switch()





if __name__ == '__main__':
    GroupMute().mute_set()

