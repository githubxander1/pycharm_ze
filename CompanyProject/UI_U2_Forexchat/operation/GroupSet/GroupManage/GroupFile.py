import time

from CompanyProject.UI_U2_Forexchat.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.UI_U2_Forexchat.base.basePage import Base1, d
from CompanyProject.UI_U2_Forexchat.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.UI_U2_Forexchat.operation.op_Home import Home


class GroupFile(Base1):
    groupNotice=d(description="公告")
    groupFile=d(description="文件")
    groupAlbum=d(description="相册")

    addbutton=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    def click_addbutton(self):
        self.addbutton.click()
    addfile=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    def click_addfile(self):
        self.addfile.click()
    filelist=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]')
    def click_filelist(self):
        self.filelist.click()
    filemanage=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]')
    def click_filemanage(self):
        self.filemanage.click()
    filesearch=d.xpath('//android.widget.EditText')
    cancelsearch=d(description="取消")
    def click_filesearch(self,text):
        self.filesearch.set_text(text)
        self.d.press('enter')

    def click_cancelsearch(self):
        self.cancelsearch.click()

    addnewfolder=d(description="新建文件夹")
    inputtext=d.xpath('//android.widget.EditText')
    canceladdnewfolder=d.xpath('//*[contains(@content-desc,"新建文件夹")]/android.widget.ImageView[1]')

    file_forward=d(description="转发")
    file_move=d(description="移动")
    file_rename=d(description="重命名")
    file_collect=d(description="收藏")
    file_view=d(description="查看")
    file_del=d(description="删除")

    def click_file_forward(self):
        self.file_forward.click()

    def click_file_move(self):
        self.file_move.click()

    def click_file_rename(self):
        self.file_rename.click()

    def click_file_collect(self):
        self.file_collect.click()

    def click_file_view(self):
        self.file_view.click()

    def click_file_del(self):
        self.file_del.click()

    folder_rename=d(description="重命名")
    folder_del=d(description="删除")

    def click_folder_rename(self):
        self.folder_rename.click()

    def click_folder_del(self):
        self.folder_del.click()

    def click_cancel(self):
        self.canceladdnewfolder.click()

    def click_addnewfolder(self):
        self.addnewfolder.click()

    def click_inputtext(self):
        self.inputtext.click()

    uploadfile=d(description="上传文件")
    def click_uploadfile(self):
        self.uploadfile.click()

    chat=d.xpath('//*[contains(@content-desc,"聊天")]')
    collection=d.xpath('//*[contains(@content-desc,"收藏")]')
    local=d.xpath('//*[contains(@content-desc,"本地")]')
    selectlocalfile=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]')
    upload=d.xpath('//*[contains(@content-desc,"上传(")]')
    localfile1=d.xpath('//*[@resource-id="com.android.documentsui:id/dir_list"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[2]')
    localphoto1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    def click_localphoto1(self):
        self.localphoto1.click()
    usephoto=d.xpath('//*[contains(@content-desc,"使用(")]')
    def click_usephoto(self):
        self.usephoto.click()

    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
    def click_back(self):
        self.back.click()
    def click_selectlocal(self):
        self.selectlocalfile.click()

    def click_chat(self):
        self.chat.click()

    def click_collection(self):
        self.collection.click()

    def click_local(self):
        self.local.click()

    def click_upload(self):
        self.upload.click()

    def click_local1(self):
        self.localfile1.click()

    uploadphoto = d(description="上传照片")
    def click_uploadphoto(self):
        self.uploadphoto.click()

    def uploadgroupfile(self):
        Home().click_conversation()
        GroupWindow().click_groupSet()
        GroupSet().click_groupFile()
        self.click_addbutton()
        self.click_uploadfile()
        self.click_local()
        time.sleep(1)
        # 点击选择本地文件
        self.d.click(0.492, 0.628)
        # 点击文件1
        time.sleep(1)
        self.d.click(0.252, 0.207)
        self.click_upload()

    def uploadgroupphoto(self):
        Home().click_conversation()
        GroupWindow().click_groupSet()
        GroupSet().click_groupFile()
        self.click_addbutton()
        self.click_uploadphoto()
        # self.click_local()
        time.sleep(1)
        # 点击选择本地图片
        self.click_localphoto1()
        # 点击文件1
        time.sleep(1)
        self.click_usephoto()



    usePop=d.xpath('//android.widget.ScrollView/android.widget.Switch[1]')
    setTop=d.xpath('//android.widget.ScrollView/android.widget.Switch[2]')


    forNewComers=d.xpath('//android.widget.ScrollView/android.widget.Switch[3]')
    # cancel=d(description="取消")
    confirm=d(description="确定")


    def click_confirm(self):
        self.confirm.click()



    def click_usePop(self):
        self.usePop.click()

    def click_groupNotice(self):
        self.groupNotice.click()

    def click_groupFile(self):
        self.groupFile.click()

    def click_groupAlbum(self):
        self.groupAlbum.click()








if __name__ == '__main__':
    # GroupFile().uploadgroupfile()
    GroupFile().uploadgroupphoto()
    time.sleep(3)
    Base1().closeApp()