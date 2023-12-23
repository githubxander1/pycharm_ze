from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d

class ForbidFriendAdd(Base1):
    forbidAddFriend = d(description="禁止群内成员互加好友")
    switch = d.xpath('//android.widget.Switch')

    def click_forbidAddFriend(self):
        self.forbidAddFriend.click()

    def click_switch(self):
        self.switch.click()

    # 修改群内加好友设置
    def friendAdd_set(self):
        # ManageGroup().manage_groups()
        self.click_forbidAddFriend()
        self.click_switch()



#
if __name__ == '__main__':
    ForbidFriendAdd().friendAdd_set()

