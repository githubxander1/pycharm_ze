
# coding: utf-8
import time

from Company_project.UI_U2_Forexchat.operation.GroupSet import ManageGroup
from Company_project.UI_U2_Forexchat import Base1, d


class Admin(Base1):
    adminset = d.xpath('//*[contains(@content-desc,"设置管理员")]')

    # 添加管理员
    def admin_add(self):
        ManageGroup().manage_groups()
        Admin().adminset.click()
        time.sleep(3)
        # adminadd.click()
        d.xpath('//*[contains(@content-desc="添加管理员")]').click()
        # d.click(0.857, 0.379)
        time.sleep(1)
        # d(description="确认").click()

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
    # Admin().admin_add()
    Admin().admin_remove()
# 添加管理员定位错误