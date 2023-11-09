import uiautomator2 as u2

# d = u2.connect_usb('22addc6f0403')
# d = u2.connect_wifi('192.168.31.117')
d = u2.connect_adb_wifi('192.168.5.220:5555')
class Base1:
    def __init__(self):
    #     # self.d = u2.connect_adb_wifi('192.168.31.19')
    #     # self.d = u2.connect_adb_wifi('192.168.31.19:5555')
        self.d = u2.connect_adb_wifi('192.168.5.220:5555')
    #     # self.d = u2.connect_adb_wifi('192.168.5.249:5555')
    #     # self.d = u2.connect_adb_wifi('192.168.31.19:5555')
    #     # self.d = u2.connect_adb_wifi('192.168.31.117:5555')
    #     # self.d = u2.connect_usb('22addc6f0403')
    #     # self.d = u2.connect('127.0.0.1:21503')
    #     # print(self.d.info())
        self.d.app_start('com.bv.forexchat')
    #     self.d.implicitly_wait(10)

    # def startApp(self):
    #     self.d.app_start('com.bv.forexchat')
    #
    # def closeApp(self):
    #     self.d.app_stop('com.bv.forexchat')


# base=Base1()
# base.startApp()