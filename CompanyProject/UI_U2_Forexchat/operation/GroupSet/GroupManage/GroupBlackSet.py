from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d

class GroupBlack(Base1):
    groupBlacklist = d(description="群黑名单")
    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')

    def click_groupBlacklist(self):
        self.groupBlacklist.click()

    def click_back(self):
        self.back.click()

    # 编辑群头像成功
    def friendAdd_set(self):
        ManageGroup().manage_groups()
        self.click_groupBlacklist()



#
if __name__ == '__main__':
    GroupBlack().friendAdd_set()

