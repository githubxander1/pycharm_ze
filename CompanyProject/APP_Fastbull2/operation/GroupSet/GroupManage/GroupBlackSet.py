import time

from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d

class GroupBlack(Base1):
    groupblacklist = d(description="群黑名单")
    # back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    back=d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
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

