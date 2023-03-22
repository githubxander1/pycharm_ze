import time
import uiautomator2 as u2

d=u2.connect('127.0.0.1:21513')


# 标记已读
def mark_read():
    # 先定位元素，再滑动
    hh = d.xpath('//android.widget.ScrollView/android.view.View[2]')
    # hh.swipe('left')
    hh.swipe('left')
    time.sleep(2)
    d.xpath('//android.widget.ScrollView/android.view.View[2]/android.widget.ImageView[1]').click()
    # d.xpath('//android.widget.ScrollView/android.view.View[3]/android.widget.ImageView[1]')
