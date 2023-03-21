# page(页面对象)：封装对元素的操作，一个页面封装成一个对象
# coding: utf-8
import time

import uiautomator2 as u2

# 连接模拟器或手机
from Company_project.AutoTest.Auto_U2_Forexchat.base.base import session1, groupSet

d=u2.connect('127.0.0.1:21513')
# 获取设备基本信息
# print(d.info)
d.implicitly_wait(10)
d.app_start('com.sy.fxchat')

# 取消更新
d(description="取消").click()

def manage_groups():
    # 进入会话
    session1()
    time.sleep(5)
    # 点击群设置
    groupSet()
    time.sleep(3)
    # 点击管理群
    d(scrollable=True).scroll.to(description="管理群")
    d(description="管理群").click()

    # 设置群内禁言
def group_Mute():
    manage_groups()
    d(description="设置群内禁言").click()
    d.xpath('//android.widget.Switch').click()

def group_MuteFriendsAdd():
    manage_groups()
    d(description="禁止群内成员互加好友").click()
    d.xpath('//android.widget.Switch').click()

def group_editGroupProfiles():
    manage_groups()
    d(description="编辑群资料").click()
    d.xpath('//*[contains(@content-desc,"群介绍")]').click()
    d(text="请输入群介绍").send_keys('群介绍：打扫房间独守空闺季拉开')
    # d.xpath('//*[contains(text(),"请输入群介绍")]').send_keys('dfsgsd')
    # d.xpath('//*[contains(@content-desc,"请输入群介绍")]').send_keys('dfsgsd')
    d.xpath('//*[contains(@content-desc,"编辑群介绍")]/android.widget.ImageView[1]').click()
    d.xpath('//*[@content-desc="确定"]').click()
    # d.xpath('//*[@content-desc="完成"]').click()

def group_admin_add():
    manage_groups()
    d.xpath('//*[contains(@content-desc,"管理员"]').click()

if __name__ == '__main__':
    group_editGroupProfiles()
    time.sleep(3)
    # d.app_stop('com.sy.fxchat')


