import time
from time import sleep

from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d

class GroupAvatar(Base1):
    avatar = d.xpath('//*[contains(@content-desc,"群头像")]')
    # defaultavatar = d(description="默认头像选择")
    selectfromalbum=d(description="从相册选择")
    viewavatar=d(description="查看头像")
    # confirm=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[3]')
    confirm=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[3]')
    # avatar1 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
    avatar1 = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')

    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    back1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    viewback=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    def click_viewback(self):
        self.viewback.click()

    def click_back(self):
        self.back.click()

    def click_back1(self):
        self.back1.click()

    def click_avatar(self):
        self.avatar.click()

    def click_avatar1(self):
        self.avatar1.click()

    def click_comfirm(self):
        self.confirm.click()

    def click_viewavatar(self):
        self.viewavatar.click()

    # def click_defaultavatar(self):
    #     self.defaultavatar.click()
    def click_selectfromalbum(self):
        self.selectfromalbum.click()

    # def click_avatar1(self):
    #     self.avatar1.click()

    # 编辑群头像成功
    def editGroupAvatar_album(self):
        # ManageGroup().manage_groups()
        # ManageGroup().click_editGroupProfile()
        self.click_avatar()
        self.click_selectfromalbum()
        sleep(2)
        self.click_avatar1()
        self.click_comfirm()
        # sleep(实例25_批量生成PPT版荣誉证书)
        # self.click_back1()
        # d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]').click()

    def editGroupAvatar_view(self):
        # ManageGroup().click_editGroupProfile()
        self.click_avatar()
        self.click_viewavatar()
        sleep(2)
        self.click_viewback()
        # self.d.click(0.072, 0.044)
        # sleep(实例25_批量生成PPT版荣誉证书)
        # self.click_back()
        # print('运行结束')
    # def editGroupAvatar_view(self):
    #     max_retry = 3  # 最多重试3次
    #     retry_count = 0  # 重试计数器
    #     while retry_count < max_retry:
    #         print(f"重试第 {retry_count} 次")
    #         try:
    #             # ManageGroup().manage_groups()
    #             ManageGroup().click_editGroupProfile()
    #             self.click_avatar()
    #             self.click_viewavatar()
    #             sleep(2)
    #             self.click_viewback()
    #             # self.d.click(0.072, 0.044)
    #             sleep(实例25_批量生成PPT版荣誉证书)
    #             self.click_back()
    #             print('运行结束')
    #         except Exception as e:
    #             sleep(3)
    #             print(f"程序运行出现异常：{e}")
    #             # 关闭App
    #             Base1().closeApp()
    #             # 重新运行程序
    #             Base1().startApp()
    #         else:
    #             break


#
# if __name__ == '__main__':
#     GroupAvatar().editGroupAvatar_set_sus()
    # time.sleep(3)
    # GroupAvatar().editGroupAvatar_view()
