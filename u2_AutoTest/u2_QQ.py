import time
from pprint import pprint

import uiautomator2 as u2

d=u2.connect('127.0.0.1:21503')
# d=u2.connect('192.168.43.15')
pprint(d.info)

d.implicitly_wait(5)
# d.app_start('com.android.settings')

# d(resourceId="android:id/input").click()
d(resourceId="android:id/title", text="我的设备").click()


# d.app_stop_all()
# 最近应用
# d.press('recent')
# d.swipe_ext('left')
# d(description="设置,未加锁").swipe('left',steps=20)
# d(resourceId="com.android.systemui:id/clearAnimView").click()
# d.app_stop('com.android.settings')