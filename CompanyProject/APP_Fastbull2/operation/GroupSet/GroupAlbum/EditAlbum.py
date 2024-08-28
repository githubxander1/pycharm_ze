import logging
import time
from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.base.basePage import Base1,d
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class EditGroupAlbum(Base1):
    edit=d(description="编辑")
    manage=d(description="管理")
    upload=d(description="上传")

    editalbumname=d.xpath('//android.widget.FrameLayout[3]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.widget.EditText[实例25_批量生成PPT版荣誉证书]')
    editalbumdescription=d.xpath('//android.widget.FrameLayout[3]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.widget.EditText[2]')
    editalbumcover=d(description="更换封面")
    settop=d.xpath('//android.widget.Switch')
    save=d(description="保存")
    deletealbum=d(description="删除相册")
    cancel=d(description="取消")
    confirm=d(description="确定")

    def click_cancel(self):
        self.cancel.click()

    def click_confirm(self):
        self.confirm.click()

    def click_deletealbum(self):
        self.deletealbum.click()

    def click_settop(self):
        self.settop.click()

    def click_save(self):
        self.save.click()

    def input_editalbumname(self,name):
        self.editalbumname.set_text(name)

    def input_editalbumdescription(self,description):
        self.editalbumdescription.set_text(description)

    def click_editalbumcover(self):
        self.editalbumcover.click()

    def click_edit(self):
        self.edit.click()

    def reviseAlubm(self,name,description):
        self.click_edit()
        self.input_editalbumname(name)
        self.input_editalbumdescription(description)
        if self.editalbumcover.exists:
            self.click_editalbumcover()
        time.sleep(2)
        self.d.click(0.207, 0.292)
        self.click_settop()
        self.click_save()

    def delAlbum(self):
        self.click_edit()
        self.click_deletealbum()
        self.click_cancel()
        time.sleep(2)
        self.click_deletealbum()
        self.click_confirm()


if __name__ == '__main__':
    # GroupFile().uploadgroupfile()
    # GroupAlbum().createnewalbum('description', 'de')
    # GroupAlbum().upload_local()

    EditGroupAlbum().d.click(0.701, 0.275)
    time.sleep(1)
    EditGroupAlbum().reviseAlubm('相册1', 'description')
    EditGroupAlbum().delAlbum()
    time.sleep(3)
    # Base1().closeApp()