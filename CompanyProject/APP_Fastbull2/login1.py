import uiautomator2 as u2

d = u2.connect_adb_wifi('192.168.5.220:5555')#手机


d.app_start('com.bv.forexchat')
d.implicitly_wait(10)