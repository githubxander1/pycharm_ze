
# coding: utf-8
import time
import uiautomator2 as u2



from op_ManageGroup import ManageGroup
# from op_ManageGroup import  manage_groups


# d=u2.connect('127.0.0.1:21513')
# d=u2.connect_wifi('192.168.31.119')
# d=u2.connect('5ENDU18C21003487')
# 获取设备基本信息
# print(d.info)
# d.implicitly_wait(10)
# d.app_start('com.bv.forexchat')
from basePage import Base1, d


# 取消更新
# d(description="取消").click()
class GroupAvatar(Base1):

    avatar = d.xpath('//*[contains(@content-desc,"群头像")]')
    defaultavatar = d(description="默认头像选择")
    avatar1 = d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ImageView[2]')
    # 编辑群头像成功
    def editGroupAvatar_set(self):
        ManageGroup().manage_groups()
        ManageGroup().editgroupprofile.click()
        GroupAvatar().avatar.click()
        GroupAvatar().defaultavatar.click()
        time.sleep(5)
        GroupAvatar().avatar1.click()
        # d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ImageView[2]').click()



#
if __name__ == '__main__':
    GroupAvatar().editGroupAvatar_set()

