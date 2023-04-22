import time

from Company_project.UI_U2_Forexchat.operation.GroupSet import ManageGroup
from Company_project.UI_U2_Forexchat import Base1, d


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
