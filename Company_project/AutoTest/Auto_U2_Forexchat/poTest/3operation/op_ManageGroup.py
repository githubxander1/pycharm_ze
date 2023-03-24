import time
import uiautomator2 as u2

from Company_project.AutoTest.Auto_U2_Forexchat.nomal import EditGroupProfile

d=u2.connect('127.0.0.1:21513')

from op_Home import session1
from op_Windows import groupSet

# 进入管理群
def manage_groups():
    # 进入会话
    session1()
    # 点击群设置
    groupSet()
    time.sleep(3)
    # 点击管理群
    d(scrollable=True).scroll.to(description="管理群")
    d(description="管理群").click()

# 点击编辑群资料
def EditGroupProfile_click(self):
    EditGroupProfile.click()

# 点击管理员
def group_admin_add():
    manage_groups()
    d.xpath('//*[contains(@content-desc,"管理员"]').click()

