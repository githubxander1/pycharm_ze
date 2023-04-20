
# coding: utf-8
import time

# d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
from op_ManageGroup import  ManageGroup
from basePage import Base1, d
# 取消更新
# d(description="取消").click()

class GroupTransfer(Base1):
    transferGroup = d(description="转让群")

    # 转让群
    def group_transfer(self):
        ManageGroup().manage_groups()
        GroupTransfer().transferGroup.click()

    # # 编辑群头像成功
    # def nickname_set(name):
    #     manage_groups()
    #     mynickname.click()
    #     nameinput.send_keys(name)
    #     complete.click()
    #


#
if __name__ == '__main__':
    GroupTransfer().group_transfer()

