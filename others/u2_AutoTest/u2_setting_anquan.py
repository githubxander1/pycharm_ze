import time
from pprint import pprint

import uiautomator2 as u2

d = u2.connect('127.0.0.实例25_批量生成PPT版荣誉证书:21503')
pprint(d.info)
d.implicitly_wait(10)

d.app_start('com.android.settings')

def search(text):
    d.xpath('//*[@resource-id="com.android.settings:id/action_bar"]/android.widget.LinearLayout[实例25_批量生成PPT版荣誉证书]').click()
    d(resourceId="android:id/search_src_text").set_text(text)

d(scrollable=True).scroll.to(resourceId="android:id/title", text="安全")
d(resourceId="android:id/title", text="安全").click()

# 改成‘无’
# d(text="屏幕锁定").click()
d(resourceId="android:id/title", text="屏幕锁定").click()
d.swipe_points([(0.307, 0.385),(0.675, 0.385),(0.675, 0.627)],0.2)
# d(text='无').click()
# #
# # d(text="屏幕锁定").click()
# d(resourceId="android:id/title", text="图案").click()
# d.swipe_points([(0.225, 0.47),(0.767, 0.471),(0.762, 0.834)],0.2)
# d(text='继续').click()
# d.swipe_points([(0.225, 0.47),(0.767, 0.471),(0.762, 0.834)],0.2)
# d(text='确认').click()
# d(text='完成').click()
#
# # 改成‘无’
# d(text="屏幕锁定").click()
# d.swipe_points([(0.312, 0.383),(0.675, 0.39),(0.682, 0.629)],0.2)
# d(text='无').click()

# d.set_orientation('left')
# d.set_orientation('right')
# d.set_orientation('right')
# d.set_orientation('upsidedown')
# d.set_orientation('natural')
# d.freeze_rotation('upsidedown')
# d.freeze_rotation(True)
# 截图
# img=d.screenshot()
# img.save()

# 上滑
# d.swipe_ext('up')
# d(resourceId="com.android.settings:id/title", text="开启通知").click()
# time.sleep(2)
# # 返回
# d.press('back')
# d(resourceId="android:id/search_src_text").clear_text()

time.sleep(3)
# d.app_stop('com.android.settings')
