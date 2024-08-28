import logging
import time

# from faker import Faker

from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.base.basePage import Base1,d
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class GroupAlbum(Base1):
    groupNotice=d(description="公告")
    groupFile=d(description="文件")
    groupAlbum=d(description="相册")

    def click_groupNotice(self):
        self.groupNotice.click()

    def click_groupFile(self):
        self.groupFile.click()

    def click_groupAlbum(self):
        self.groupAlbum.click()


    addbutton=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    uploadlocal=d(description="本地上传")
    importgroup=d(description="导入群聊")

    def click_addbutton(self):
        self.addbutton.click()
    def click_uploadlocal(self):
        self.uploadlocal.click()
    def click_importgroup(self):
        self.importgroup.click()
    def uploadgroupphoto(self):
        self.uploadphoto.click()

    localfile1 = d.xpath(
        '//*[@resource-id="com.android.documentsui:id/dir_list"]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')
    localphoto1 = d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    groupphoto1=d.xpath('//*[@content-desc="本月"]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')

    uploadphoto=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    def click_groupphoto1(self):
        self.groupphoto1.click()
    def click_localphoto1(self):
        self.localphoto1.click()

    usephoto = d.xpath('//*[contains(@content-desc,"使用(")]')
    upload=d(description="上传")

    def click_upload(self):
        self.upload.click()

    def click_usephoto(self):
        self.usephoto.click()

    importfroup_photo1=d.xpath('//*[@content-desc="本周"]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')

    def click_importfroup_photo1(self):
        self.importfroup_photo1.click()

    creatNewalbum=d(description="新建相册")
    # imputalbumname=d.xpath('//android.widget.FrameLayout[3]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.EditText[实例25_批量生成PPT版荣誉证书]')
    # inputalbumname=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.EditText[实例25_批量生成PPT版荣誉证书]')
    inputalbumname=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.EditText[实例25_批量生成PPT版荣誉证书]')
    # imputalbumdescription=d.xpath('//android.widget.FrameLayout[3]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.EditText[2]')
    # imputalbumdescription=d.xpath('//android.widget.FrameLayout[2]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.EditText[2]')
    # imputalbumdescription=d.xpath('//android.widget.FrameLayout[4]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.EditText[2]')
    inputalbumdescription=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.EditText[2]')
    inputalbumdescription2=d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.EditText[2]')
    create=d(description="新建")

    def click_create(self):
        self.create.click()

    def input_albumname(self,name):
        self.inputalbumname.set_text(name)

    def input_albumdescription(self,description):
        try:
            if self.inputalbumdescription.exists:
                self.inputalbumdescription.set_text(description)
            else:
                self.inputalbumdescription2.set_text(description)
        except Exception as e:
            logging.info(e)


    def click_createnewalbum(self):
        self.creatNewalbum.click()

    back=d.xpath('//android.widget.FrameLayout[3]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')

    def click_back(self):
        self.back.click()

    # def createnewalbum(self,name,description):
    #     max_retry = 3  # 最多重试3次
    #     retry_count = 0  # 重试计数器
    #     while retry_count < max_retry:
    #         print(f"重试第 {retry_count} 次")
    #         try:
    #             # Home().startApp()
    #             # time.sleep(5)
    #             # Home().click_conversation()
    #             # logging.info("进入对话列表")
    #             # GroupWindow().click_groupSet()
    #             # logging.info("点击群设置")
    #             # GroupSet().click_groupAlbum()
    #             # logging.info("进入群相册")
    #
    #             self.click_createnewalbum()
    #             logging.info("点击创建新相册")
    #             time.sleep(2)
    #             self.input_albumname(name)
    #             logging.info("输入相册名")
    #             time.sleep(3)
    #             self.input_albumdescription(description)
    #             logging.info("输入描述")
    #             self.click_create()
    #
    #             # # 等待toast出现并获取提示内容
    #             # toast_message = self.wait_for_toast()
    #             # print(toast_message)
    #
    #         except Exception as e:
    #             time.sleep(3)
    #             print(f"程序运行出现异常：{e}")
    #             # 关闭App
    #             Base1().closeApp()
    #             # 重新运行程序
    #             Base1().startApp()
    #         else:
    #             break
    #
    #     # 断言toast的提示内容
    #     # assert "Expected Toast Message" in toast
    def createnewalbum(self,name,description):
        self.click_createnewalbum()
        logging.info("点击创建新相册")
        time.sleep(2)
        self.input_albumname(name)
        logging.info("输入相册名")
        time.sleep(3)
        self.input_albumdescription(description)
        logging.info("输入描述")
        self.click_create()


    editalbum=d(description="编辑")
    edit_upload=d(description="上传")
    edit_settop=d.xpath('//android.widget.Switch')
    edit_delete=d(description="删除相册")
    edit_cancel=d(description="取消")
    edit_comfirm=d(description="确定")
    edit_save=d(description="保存")

    def click_editalbum(self):
        self.editalbum.click()

    def click_edit_upload(self):
        self.edit_upload.click()

    def click_edit_settop(self):
        self.edit_settop.click()

    def click_edit_delete(self):
        self.edit_delete.click()

    def click_edit_cancel(self):
        self.edit_cancel.click()

    def click_edit_comfirm(self):
        self.edit_comfirm.click()




    # 本地上传
    def upload_local(self):
        self.click_addbutton()
        self.click_uploadlocal()
        self.click_localphoto1()
        self.click_usephoto()
        self.click_upload()

    # 导入群聊
    def importfromGroup(self):
        self.click_addbutton()
        self.click_importgroup()
        self.click_groupphoto1()
        self.click_usephoto()
        self.click_upload()

if __name__ == '__main__':
    # GroupFile().uploadgroupfile()
    fake=Faker(['zh_CN','en_US'])
    name=fake.name()
    number=fake.random_number()
    description=fake.text()
    GroupAlbum().createnewalbum(str(number)+name,description)
    # GroupAlbum().upload_local()
    # GroupAlbum().importfromGroup()
    time.sleep(3)
    # Base1().closeApp()