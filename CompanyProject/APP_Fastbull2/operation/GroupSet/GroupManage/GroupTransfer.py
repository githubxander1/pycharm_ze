import time

from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d


class GroupTransfer(Base1):
    transferGroup = d(description="转让群")
    # newAdmin=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/'
    #                  'android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/'
    #                  'android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    newAdmin=0.101, 0.256
    # d.find_element(By.XPATH,'//li[contains(string(),"{}")]'.format(number)).click()
    cancel=d(description="取消")
    sure=d(description="确定")

    def click_transferGroup(self):
        self.transferGroup.click()

    def click_newAdmin(self):
        self.d.click(0.101, 0.256)

    def click_cancel(self):
        self.cancel.click()

    def click_sure(self):
        self.sure.click()

    # 转让群
    def group_transfer(self):
        ManageGroup().manage_groups()
        self.click_transferGroup()
        self.click_newAdmin()
        time.sleep(2)
        # 取消
        self.click_cancel()


#
if __name__ == '__main__':
    GroupTransfer().group_transfer()
