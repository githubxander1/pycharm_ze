import uiautomator2 as u2

d = u2.connect('127.0.0.1:21503')
class Base1:
    def __init__(self):
        self.d = u2.connect('127.0.0.1:21503')
        # print(self.d.info['currentPackageName'])
        self.d.app_start('com.bv.forexchat')
        self.d.implicitly_wait(10)

    def startApp(self):
        self.d.app_start('com.bv.forexchat')

    def closeApp(self):
        self.d.app_stop('com.bv.forexchat')
