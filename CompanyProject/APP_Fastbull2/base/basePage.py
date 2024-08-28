import time
from datetime import datetime

from time import sleep

import uiautomator2 as u2

# d = u2.connect_usb('22addc6f0403')
# d = u2.connect_wifi('192.168.31.117')
# d = u2.connect_adb_wifi('192.168.5.220:5555')
d = u2.connect()
print(d.info)
class Base1:

    head=d.xpath('//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.widget.FrameLayout[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    def click_head(self):
        self.head.click()
    tologin=d(resourceId="com.bv.fastbull:id/tv_mine_top_welcome")
    def click_tologin(self):
        self.tologin.click()
    phoneOremail=d.xpath('//*[@resource-id="com.bv.fastbull:id/ll_btn"]/android.widget.RelativeLayout[实例25_批量生成PPT版荣誉证书]')
    get_code=d(resourceId="com.bv.fastbull:id/tv_get_code")
    def click_get_code(self):
        self.get_code.click()
    phone=d(resourceId="com.bv.fastbull:id/et_mine_edit_phone_number")
    identifyCode=d(resourceId="com.bv.fastbull:id/et_code")
    login=d(resourceId="com.bv.fastbull:id/tv_sign")
    def click_login(self):
        self.login.click()

    chat=d.xpath('//*[@resource-id="com.bv.fastbull:id/mainTabBar"]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]/android.widget.ImageView[实例25_批量生成PPT版荣誉证书]')
    def __init__(self):
    #     # self.d = u2.connect_adb_wifi('192.168.31.19')
    #     # self.d = u2.connect_adb_wifi('192.168.31.19:5555')
    #     self.d = u2.connect_adb_wifi('192.168.5.220:5555')
        self.d = u2.connect()
        self.d.implicitly_wait(10)
    #     # self.d = u2.connect_adb_wifi('192.168.5.249:5555')
    #     # self.d = u2.connect_adb_wifi('192.168.31.19:5555')
    #     # self.d = u2.connect_adb_wifi('192.168.31.117:5555')
    #     # self.d = u2.connect_usb('22addc6f0403')
    #     # self.d = u2.connect('127.0.0.实例25_批量生成PPT版荣誉证书:21503')
    #     # print(self.d.info())
    #     self.d.app_start('com.bv.forexchat')
    #     self.d.implicitly_wait(10)

    def startApp(self):
        self.d.app_start('com.bv.fastbull')
        self.chat.click()


    def closeApp(self):
        self.d.app_stop('com.bv.fastbull')

    def login_phone(self):
        self.startApp()
        time.sleep(4)
        self.click_head()
        self.click_tologin()

        self.phoneOremail.click()
        self.phone.set_text('13111111114')
        self.click_get_code()
        sleep(2)
        # self.d.click(0.845, 0.927)
        # self.d.click(0.845, 0.927)
        self.identifyCode.set_text('1234')


    def take_screenshot(self,text):
        now=datetime.now().strftime('%Y%m%d-%H%M%S')
        filename=f'result_screenshots/group_nickname/{text}_{now}.png'
        d.screenshot(filename)





# base=Base1()
# base.login_phone()
# # screenshot_path = "./screenshot1.png"  # 截图保存的路径
# # d.screenshot(screenshot_path)# base.login_phone()
# base.startApp()