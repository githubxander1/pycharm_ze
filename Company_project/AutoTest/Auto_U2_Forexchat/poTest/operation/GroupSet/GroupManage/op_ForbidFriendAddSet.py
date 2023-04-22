from Company_project.AutoTest.Auto_U2_Forexchat.poTest.operation.GroupSet.GroupManage.op_ManageGroup import ManageGroup
from Company_project.AutoTest.Auto_U2_Forexchat.poTest.base.basePage import Base1, d

class ForbidFriendAdd(Base1):
    addFriend = d(description="禁止群内成员互加好友")
    switch = d.xpath('//android.widget.Switch')

    # 修改群内加好友设置
    def friendAdd_set(self):
        ManageGroup().manage_groups()
        ForbidFriendAdd().addFriend.click()
        ForbidFriendAdd().switch.click()



#
if __name__ == '__main__':
    ForbidFriendAdd().friendAdd_set()

