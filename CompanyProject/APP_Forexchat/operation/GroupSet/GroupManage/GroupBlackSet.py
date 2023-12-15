import time

from CompanyProject.APP_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Forexchat.base.basePage import Base1, d

class GroupBlack(Base1):
    groupblacklist = d(description="群黑名单")
    # back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    back=d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    def click_groupBlacklist(self):
        self.groupblacklist.click()

    def click_back(self):
        self.back.click()

    # 群黑名单
    def groupBlacklist(self):
        self.click_groupBlacklist()
        time.sleep(2)
        self.click_back()



#
if __name__ == '__main__':
    GroupBlack().groupBlacklist()

