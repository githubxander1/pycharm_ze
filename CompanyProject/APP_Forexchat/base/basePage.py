from datetime import datetime

from time import sleep

import uiautomator2 as u2

# d = u2.connect_usb('22addc6f0403')
# d = u2.connect_wifi('192.168.31.117')
# d = u2.connect_adb_wifi('192.168.5.220:5555')
d = u2.connect()
class Base1:
    phoneOremail=d(description="​邮​箱​/​F​X​I​D​/​手​机​号​")
    phone=d.xpath('//android.widget.EditText')
    identifyCode=d.xpath('//android.widget.EditText')
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
        self.d.app_start('com.bv.forexchat')

    def closeApp(self):
        self.d.app_stop('com.bv.forexchat')

    def login_phone(self):
        self.phoneOremail.click()
        self.phone.set_text('13111111114')
        sleep(2)
        self.d.click(0.845, 0.927)
        self.d.click(0.845, 0.927)
        self.identifyCode.set_text('1234')

    def take_screenshot(self,text):
        now=datetime.now().strftime('%Y%m%d-%H%M%S')
        filename=f'result_screenshots/group_nickname/{text}_{now}.png'
        d.screenshot(filename)





# base=Base1()
# screenshot_path = "./screenshot1.png"  # 截图保存的路径
# d.screenshot(screenshot_path)# base.login_phone()
# base.startApp()