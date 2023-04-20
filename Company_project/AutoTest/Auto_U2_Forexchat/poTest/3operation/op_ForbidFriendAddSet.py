
# coding: utf-8
import time
from op_ManageGroup import  ManageGroup
from basePage import Base1, d
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.bv.forexchat')

# 取消更新
# d(description="取消").click()

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

