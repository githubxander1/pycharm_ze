
# coding: utf-8
import time
import uiautomator2 as u2


# from ele import d,groupadditionMethod,everyone

from op_ManageGroup import  ManageGroup


# d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
from op_ManageGroup import  ManageGroup
from basePage import Base1, d

class GroupAdd(Base1):
    groupadditionMethod = d(description="加群方式")
    everyone = d(description="允许任何人加群")
    needVerify = d(description="需要发送验证消息")
    forbid = d(description="不允许任何人加群")
    # 加群方式
    def groupAdd_set(self):
        ManageGroup().manage_groups()
        ManageGroup().groupadditionMethod.click()
        GroupAdd().everyone.click()



#
if __name__ == '__main__':
    GroupAdd().groupAdd_set()

