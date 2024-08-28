from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d

class GroupAdd(Base1):
    groupAddMethod = d(description="加群方式")
    anyone = d(description="允许任何人加群")
    needVerify = d(description="需要发送验证消息")
    NoneAllowed= d(description="不允许任何人加群")
    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')

    def click_back(self):
        self.back.click()


    def click_groupAddMethod(self):
        self.groupAddMethod.click()

    def click_anyone(self):
        self.anyone.click()

    def click_needVerify(self):
        self.needVerify.click()

    def click_forbid(self):
        self.NoneAllowed.click()

    # 加群方式-允许任何人
    def groupAdd_anyone(self):
        # ManageGroup().manage_groups()
        ManageGroup().click_groupAddMethod()
        self.click_anyone()
        self.click_back()

    # 加群方式-需要发送验证消息
    def groupAdd_needVerify(self):
        # ManageGroup().manage_groups()
        ManageGroup().click_groupAddMethod()
        self.click_needVerify()
        self.click_back()

    # 加群方式-不允许任何人加群
    def groupAdd_forbid(self):
        # ManageGroup().manage_groups()
        ManageGroup().click_groupAddMethod()
        self.click_forbid()
        self.click_back()




#
if __name__ == '__main__':
    # GroupAdd().groupAdd_anyone()
    # GroupAdd().groupAdd_needVerify()
    GroupAdd().groupAdd_forbid()

