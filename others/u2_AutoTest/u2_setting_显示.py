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
d(resourceId="android:id/title", text="语言和输入法").click()
d(text='指针速度').click()
d.drag(0.139, 0.512,0.765, 0.514)
d(text='取消').click()


