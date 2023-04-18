from pprint import pprint

import uiautomator2 as u2

d=u2.connect('5ENDU18C21003487')
# # d=u2.connect_adb_wifi('92.168.2.49')
# d=u2.connect_wifi('192.168.2.49')
pprint(d.info)

