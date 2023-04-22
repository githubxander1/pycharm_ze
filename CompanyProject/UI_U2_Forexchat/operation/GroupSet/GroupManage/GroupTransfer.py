from Company_project.UI_U2_Forexchat.operation.GroupSet import ManageGroup
from Company_project.UI_U2_Forexchat import Base1, d


class GroupTransfer(Base1):
    transferGroup = d(description="转让群")
    newAdmin=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/'
                     'android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/'
                     'android.widget.ImageView[1]')
    # d.find_element_by_xpath('//li[contains(string(),"{}")]'.format(number)).click()
    cancel=d(description="取消")
    sure=d(description="确定")

    # 转让群
    def group_transfer(self):
        ManageGroup().manage_groups()
        GroupTransfer().transferGroup.click()
        GroupTransfer().newAdmin.click()
        GroupTransfer().cancel.click()


#
if __name__ == '__main__':
    GroupTransfer().group_transfer()
