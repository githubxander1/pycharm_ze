import time

from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupManage.ManageGroup import ManageGroup
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home
from CompanyProject.APP_Fastbull2.operation.common import Global


class GroupFile(Base1):
    groupNotice=d(description="公告")
    groupFile=d(description="文件")
    groupAlbum=d(description="相册")

    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    clear=d.xpath('//android.widget.FrameLayout[3]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')
    def click_clear(self):
        self.clear.click()
    def click_back(self):
        self.back.click()

    addbutton=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    def click_addbutton(self):
        self.addbutton.click()
    addfile=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    def click_addfile(self):
        self.addfile.click()

    filelist=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')

    # 上传下载中
    def click_filelist(self):
        self.filelist.click()

    # 管理文件
    filemanage=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[3]')
    filemanage_download=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    filemanage_share=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')
    filemanage_collect=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[3]')
    filemanage_delete=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[4]')
    def click_filemanage(self):
        self.filemanage.click()

    def click_filemanage_download(self):
        self.filemanage_download.click()


    def click_filemanage_share(self):
        self.filemanage_share.click()


    def click_filemanage_collect(self):
        self.filemanage_collect.click()


    def click_filemanage_delete(self):
        self.filemanage_delete.click()





    # 搜索
    filesearch=d.xpath('//android.widget.EditText')
    cancel=d(description="取消")
    confirm=d(description="确定")

    def click_confirm(self):
        self.confirm.click()
    def click_cancel(self):
        self.cancel.click()
    inputtext=d.xpath('//android.widget.EditText')
    def click_search(self,text):
        self.filesearch.set_text(text)
        self.d.press('enter')
    def click_inputtext(self):
        self.inputtext.click()

    # 按钮
    addnewfolder=d(description="新建文件夹")
    uploadfile=d(description="上传文件")
    uploadphoto = d(description="上传照片")
    canceladdnewfolder=d.xpath('//*[contains(@content-desc,"新建文件夹")]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    def click_addnewfolder(self):
        self.addnewfolder.click()
    def click_uploadfile(self):
        self.uploadfile.click()
    def click_uploadphoto(self):
        self.uploadphoto.click()

    # 文件操作
    file_forward=d(description="转发")

    file_move=d(description="移动")
    file_movehear=d(description="移动到这里")

    file_rename=d(description="重命名")
    file_renameedit=d.xpath('//android.widget.EditText')
    file_renamecancel=d.xpath('//*[contains(@content-desc,"重命名")]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    file_renamecomfirm=d(description="完成")
    file_collect=d(description="收藏")
    file_download=d(description="下载")

    file_view=d(description="查看")
    file_view_download=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')
    file_view_save=d(description="保存")
    file_view_edit=d(description="编辑")
    def click_file_view_save(self):
        self.file_view_save.click()

    def click_file_view_edit(self):
        self.file_view_edit.click()



    file_del=d(description="删除")

    def click_file_view_download(self):
        self.file_view_download.click()
    def click_file_download(self):
        self.file_download.click()
    def click_file_renamecomfirm(self):
        self.file_renamecomfirm.click()
    def click_file_renamecancel(self):
        self.file_renamecancel.click()

    def click_file_renameedit(self,text):
        self.file_renameedit.set_text(text)

    def click_file_forward(self):
        self.file_forward.click()

    def click_file_move(self):
        self.file_move.click()

    def click_file_movehear(self):
        self.file_movehear.click()

    def click_file_rename(self):
        self.file_rename.click()

    def click_file_collect(self):
        self.file_collect.click()

    def click_file_view(self):
        self.file_view.click()

    def click_file_del(self):
        self.file_del.click()

    # 文件夹操作
    folder_rename=d(description="重命名")
    folder_del=d(description="删除")

    def click_folder_rename(self):
        self.folder_rename.click()

    def click_folder_del(self):
        self.folder_del.click()

    def click_canceladdnewfolder(self):
        self.canceladdnewfolder.click()

    # 上传文件
    chat=d.xpath('//*[contains(@content-desc,"聊天")]')
    collection=d.xpath('//*[contains(@content-desc,"收藏")]')
    local=d.xpath('//*[contains(@content-desc,"本地")]')
    selectlocalfile=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]')
    upload=d.xpath('//*[contains(@content-desc,"上传(")]')
    localfile1=d.xpath('//*[@resource-id="com.android.documentsui:id/dir_list"]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[2]')
    localphoto1=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[2]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    def click_localphoto1(self):
        self.localphoto1.click()
    usephoto=d.xpath('//*[contains(@content-desc,"使用(")]')
    def click_usephoto(self):
        self.usephoto.click()

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


    # 上传文件
    def uploadgroupfile(self):
        self.click_addbutton()
        self.click_uploadfile()
        self.click_local()
        time.sleep(1)
        # 点击选择本地文件
        self.d.click(0.492, 0.628)
        # 点击文件1
        time.sleep(1)
        self.d.click(0.252, 0.207)
        time.sleep(1)
        self.click_upload()

    # 上传图片
    def uploadgroupphoto(self):
        self.click_addbutton()
        self.click_uploadphoto()
        # self.click_local()
        time.sleep(1)
        # 点击选择本地图片
        self.click_localphoto1()
        # 点击文件1
        time.sleep(1)
        self.click_usephoto()

    # 搜索文件
    def searchfile_filename(self,filename):
        self.click_search(filename)

    def searchfile_uploader(self,uploader):
        self.click_search(uploader)

    def searchfile_cancel(self):
        self.filesearch.click()
        self.click_cancel()

    # 文件-转发
    def file_Forward(self):
        self.d.click(0.912, 0.274)
        self.click_file_forward()
        Global().forward_tofriendandgroup()

    # 文件-移动
    def file_Move(self):
        self.d.click(0.912, 0.274)
        self.click_file_move()
        # 目标位置
        time.sleep(1)
        self.d.click(0.356, 0.632)
        self.click_file_movehear()

    # 文件-重命名
    def file_Rename(self,text):
        self.d.click(0.912, 0.274)
        self.click_file_rename()
        self.click_file_renameedit(text)
        self.click_file_renamecomfirm()

    # 文件-收藏
    def file_Collect(self):
        self.d.click(0.912, 0.274)
        self.click_file_collect()

    # 文件-下载
    def file_Download(self):
        self.d.click(0.912, 0.274)
        self.click_file_download()

    # 文件-查看
    def file_View(self):
        self.d.click(0.912, 0.274)
        self.click_file_view()

    # 文件-删除
    def file_Delete(self):
        self.d.click(0.912, 0.274)
        self.click_file_del()
        Global().click_confirm()

    # 管理-下载
    def filemanage_Download(self):
        self.click_filemanage()
        self.d.click(0.082, 0.298)
        self.click_filemanage_download()

    # 管理-分享
    def filemanage_Share(self):
        self.click_filemanage()
        self.d.click(0.082, 0.298)
        self.click_filemanage_share()
        Global().forward_tofriendandgroup()

    # 管理-收藏
    def filemanage_Collect(self):
        self.click_filemanage()
        self.d.click(0.082, 0.298)
        self.click_filemanage_collect()

    # 管理-删除
    def filemanage_Delete(self):
        self.click_filemanage()
        self.d.click(0.082, 0.298)
        self.click_filemanage_delete()
        Global().click_confirm()

if __name__ == '__main__':
    # GroupFile().uploadgroupfile()
    # time.sleep(3)
    # GroupFile().uploadgroupphoto()
    # time.sleep(3)
    # GroupFile().searchfile_filename('实例25_批量生成PPT版荣誉证书')
    # time.sleep(3)
    # GroupFile().searchfile_uploader('1312-真')
    # GroupFile().searchfile_cancel()
    # 文件
    # GroupFile().file_Forward()
    # GroupFile().file_Move()
    # GroupFile().file_Rename('重命名')
    # GroupFile().file_Collect()
    # GroupFile().file_Download()
    # GroupFile().file_View()
    # GroupFile().file_Delete()
    # 管理
    # GroupFile().filemanage_Download()
    # GroupFile().filemanage_Share()
    GroupFile().filemanage_Collect()
    # GroupFile().filemanage_Delete()


    # Base1().closeApp()
