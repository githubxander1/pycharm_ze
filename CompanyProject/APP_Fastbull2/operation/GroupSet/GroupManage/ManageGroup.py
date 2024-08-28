# import pytesseract as pytesseract
from PIL import Image
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # 替换成你的Tesseract OCR引擎的路径

# import cv2
import time
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.operation.op_Home import Home


class ManageGroup(Base1):
    editGroupGrofile = d(description="编辑群资料")
    # 管理员
    adminSet = d.xpath('//*[contains(@content-desc,"设置管理员")]')
    addadmin=d(description="添加管理员")
    # cancel = d.xpath('//*[contains(@content-desc,"取消")]')
    cancel = d(description="取消")
    confirm1 = d(description="确认")
    confirm = d.xpath('//*[contains(@content-desc,"确定(")]')
    # confirm = d(description="确定")
    back=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')

    def click_back(self):
        self.back.click()

    # # 群内禁言
    # groupMute = d(description="设置群内禁言")
    switch=d.xpath('//android.widget.Switch')
    def click_switch(self):
        self.switch.click()


    def click_addadmin(self):
        self.addadmin.click()

    def click_cancel(self):
        self.cancel.click()

    def click_confirm(self):
        if  self.confirm.exists:
            self.confirm.click()
        else:
            self.confirm1.click()

    def click_adminset(self):
        self.adminSet.click()

    def click_cancel1(self):
        self.cancel.click()

    def addAdmin(self):
        self.click_adminset()
        self.click_addadmin()
        time.sleep(1)
        self.d.click(0.083, 0.263)
        time.sleep(1)
        self.click_confirm()
        self.click_back()

    # def capture_toast_text(self):
    #     # 点击按钮，触发toast提示
    #     # d(text=button_text).click()
    #     # text = pytesseract.image_to_string(img, lang='eng', config=tessdata_dir_config)
    #
    #     # 等待toast提示出现
    #     time.sleep(实例25_批量生成PPT版荣誉证书)  # 等待toast提示出现的时间
    #     # d.implicit_wait(10)
    #
    #     # 获取toast提示中的文案
    #     # 截图
    #     screenshot_path = "./screenshot1.png"  # 截图保存的路径
    #     d.screenshot(screenshot_path)  # 截取当前屏幕并保存为图片
    #     # # 使用OCR识别toast提示中的文案
    #     # image = Image.open(screenshot_path)  # 打开截图图片
    #     # text = pytesseract.image_to_string(image)  # 使用OCR识别图片中的文案
    #
    #     # 使用OpenCV读取截图
    #     img = cv2.imread(screenshot_path)
    #     # 使用OpenCV识别图片中的文字
    #     # 灰度处理
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     # 二值化
    #     # 使用Tesseract OCR进行文字识别
    #     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 替换为你的tesseract安装路径
    #     tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'  # 替换为你的tessdata目录所在路径
    #     text = pytesseract.image_to_string(img,lang='chi_sim', config=tessdata_dir_config)
    #     # 输出识别结果
    #     print("识别结果：", text)
    #     # 返回识别结果
    #     return text

    def delAdmin(self):
        self.click_adminset()
        time.sleep(1)
        self.d.click(0.852, 0.358)
        self.click_cancel()
        time.sleep(1)
        self.d.click(0.852, 0.358)
        self.click_confirm()
        self.click_back()

    groupmute = d(description="设置群内禁言")
    addfriend = d(description="禁止群内成员互加好友")
    groupaddMethod = d(description="加群方式")
    groupBlacklist = d(description="群黑名单")
    transferGroup = d(description="转让群")

    # 点击编辑群资料
    def click_editGroupProfile(self):
        self.editGroupGrofile.click()

    def click_groupMute(self):
        self.groupmute.click()

    def click_addFriend(self):
        self.addfriend.click()

    def click_groupAddMethod(self):
        self.groupaddMethod.click()

    def click_groupBlacklist(self):
        self.groupBlacklist.click()

    def click_transferGroup(self):
        self.transferGroup.click()

    # 进入管理群
    def manage_groups(self):
        time.sleep(5)
        # 进入会话
        Home().click_conversation()
        # 点击群设置
        GroupWindow().click_groupSet()
        # 点击管理群
        # 垂直向前滚动到指定位置（横向同理）
        while not d(description="管理群").exists():
            d(scrollable=True).scroll.forward()
            time.sleep(1)
        d(description="管理群").click()

    def click_managegroup(self):
        # time.sleep(5)
        # # 进入会话
        # Home().click_conversation()
        # # 点击群设置
        # GroupWindow().click_groupSet()
        # 点击管理群
        # 垂直向前滚动到指定位置（横向同理）
        while not d(description="管理群").exists():
            d(scrollable=True).scroll.forward()
            time.sleep(1)
        d(description="管理群").click()





if  __name__ == "__main__":
    # ManageGroup().addAdmin()
    ManageGroup().delAdmin()

