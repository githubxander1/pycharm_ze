import unittest
import time

import logging
from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.base.basePage import Base1
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.GroupBlackSet import GroupBlack
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.GroupMuteEveryone import GroupMute
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ForbidFriendAdd import ForbidFriendAdd
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.GroupAddSet import  GroupAdd
# from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.GroupManage import GroupManage

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')



class Test_manageGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 在测试类中，setUpClass() 方法会在所有测试用例执行前自动调用一次
        Base1().startApp()
        time.sleep(4)
        Home().click_conversation()
        GroupWindow().click_groupSet()
        GroupSet().click_managegroup()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        # Base1().closeApp()

    def setUp(self):
        # 等待3秒
        time.sleep(3)

    def tearDown(self):
        pass

    # 加好友
    def test_addfriendset_1(self):
        ForbidFriendAdd().friendAdd_set()
        logging.info("设置加好友方式成功1")

    def test_addfriendset_2(self):
        ForbidFriendAdd().friendAdd_set()
        logging.info("设置加好友方式成功2")

    # 加群方式
    def test_groupaddset_anyone(self):
        GroupAdd().groupAdd_anyone()
        logging.info("加群方式-任何人")
    def test_groupaddset_needVerify(self):
        GroupAdd().groupAdd_needVerify()
        logging.info("加群方式-需要验证")
    def test_groupaddset_forbid(self):
        GroupAdd().groupAdd_forbid()
        logging.info("加群方式-禁止加群")


    # 群内禁言
    def test_groupmute_1(self):
        GroupMute().mute_set()
        logging.info("群内禁言成功1")
    def test_groupmute_2(self):
        GroupMute().mute_set()
        logging.info("群内禁言成功2")


    # 群黑名单
    def test_groupblack_1(self):
        GroupBlack().groupBlacklist()
        logging.info("群黑名单成功1")

    # 管理员
    def test_groupadmin_add(self):
        ManageGroup().addAdmin()
        logging.info("管理员添加成功")
    def test_groupadmin_del(self):
        ManageGroup().delAdmin()
        logging.info("管理员删除成功")


if __name__ == "__main__":
    unittest.main()