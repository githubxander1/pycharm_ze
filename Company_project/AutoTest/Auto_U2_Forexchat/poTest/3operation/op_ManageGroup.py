import time
import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.nomal import EditGroupProfile

# try:
#     d=u2.connect('127.0.0.1:21513')
# except:
d=u2.connect('127.0.0.1:21513')
d.implicitly_wait(10)
# from ele import d,editgroupprofile
# from op_Home import session1
# from op_Windows import groupSet



from op_Home import Home
from op_GroupWindow import GroupWindow
from basePage import Base1

class ManageGroup(Base1):
    # 编辑群资料
    # class GroupProfile():
    editgroupprofile = d(description="编辑群资料")
    # editgroupprofile=d.xpath('//*[@content-desc="编辑群资料"]')

    # 群头像
    avatar = d.xpath('//*[contains(@content-desc,"群头像")]')
    defaultavatar = d(description="默认头像选择")
    avatar1 = d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ImageView[2]')
    # 群名称
    name = d.xpath('//*[contains(@content-desc,"群名称")]')
    inputgroupname = d(className="android.widget.edNittext")
    # 群介绍
    description = d.xpath('//*[contains(@content-desc,"群介绍")]')
    inputgroupdescription = d(className="android.widget.edittext")

    cancel = d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.imageview[1]')
    complete = d(description="完成")
    sure = d.xpath('//*[@content-desc="确定"]')

    # 设置管理员
    # adminset=d.xpath('//*[contains(@description,"设置管理员")]')
    adminset = d.xpath('//*[contains(@content-desc,"设置管理员")]')
    # adminset=d(descriptionContains='设置管理员')

    # adminadd=d.xpath('//*[contains(@content-desc,"添加管理员")]/')
    adminadd = d(description="添加管理员")
    # d.xpath('//*[@content-desc="添加管理员"]')
    groupMute = d(description="设置群内禁言")
    switch = d.xpath('//android.widget.Switch')

    addFriend = d(description="禁止群内成员互加好友")

    groupadditionMethod = d(description="加群方式")
    everyone = d(description="允许任何人加群")
    needVerify = d(description="需要发送验证消息")
    forbid = d(description="不允许任何人加群")

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
        # d(scrollable=True).scroll.horiz.to(description="管理群")
        # d(scrollable=True).scroll.to(description="管理群")
        time.sleep(3)
        d(description="管理群").click()


    # 点击编辑群资料
    def editgroupprofile_click(self):
        ManageGroup().editgroupprofile.click()

    # 点击管理员
    def group_admin_add(self):
        ManageGroup().manage_groups()
        d.xpath('//*[contains(@content-desc,"管理员"]').click()

