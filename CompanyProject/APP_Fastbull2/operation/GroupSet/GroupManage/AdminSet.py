
# coding: utf-8
import time

from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d


class Admin(Base1):
    adminset = d.xpath('//*[contains(@content-desc,"设置管理员")]')
    adminadd = d.xpath('//*[contains(@content-desc,"添加管理员")]')
    admin1=(0.083, 0.265)
    confirm=d.xpath('//*[contains(@content-desc,"确定")]')

    # 点击设置管理员
    def click_adminset(self):
        self.adminset.click()

    def click_adminAdd(self):
        self.adminadd.click()

    def click_admin1(self):
        self.d.click(0.083, 0.265)

    def click_comfirm(self):
        self.confirm.click()


    # 添加管理员
    def admin_add(self):
        ManageGroup().manage_groups()
        Admin().click_adminset()
        time.sleep(3)
        self.click_adminAdd()
        time.sleep(1)
        self.click_admin1()
        self.click_comfirm()

    # 移除管理员
    def admin_remove(self):
        ManageGroup().manage_groups()
        Admin().adminset.click()
        time.sleep(3)
        d.click(0.857, 0.379)
        time.sleep(1)
        d(description="确认").click()
        # time.sleep(5)
        # 获取toast,当没有找到toast消息时，返回default内容
        # assert '管理员身份已移除' in d.toast.get_message(timout=15, default='no toast')
        # # 清空toast缓存
        # d.toast.reset()




#
if __name__ == '__main__':
    Admin().admin_add()
    # Admin().admin_remove()
# 添加管理员定位错误