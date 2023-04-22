
# coding: utf-8
import time
import uiautomator2 as u2


# from ele import d,groupBlacklist

from op_ManageGroup import  d,manage_groups,groupBlacklist


# d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
from op_ManageGroup import  ManageGroup
from basePage import Base1, d
# 取消更新
# d(description="取消").click()

class GroupBlack(Base1):
    groupBlacklist = d(description="群黑名单")

    # 编辑群头像成功
    def friendAdd_set(self):
        ManageGroup().manage_groups()
        GroupBlack().groupBlacklist.click()



#
if __name__ == '__main__':
    GroupBlack().friendAdd_set()

