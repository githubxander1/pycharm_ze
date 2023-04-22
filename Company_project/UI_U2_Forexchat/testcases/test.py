import uiautomator2 as u2
import time

d=u2.connect('127.0.0.1:21503')
d.implicitly_wait(10)

d.app_start('com.sy.fxchat')
time.sleep(10)
d.xpath('//android.widget.ScrollView/android.view.View[2]').click()
d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.ImageView[3]').click()
time.sleep(2)

d(scrollable=True).scroll.to(description='管理群')
time.sleep(3)
d.xpath('//*[contains(@content-desc,"管理群")]').click()
time.sleep(10)

d(description="编辑群资料").click()
d.xpath('//*[@content-desc="群头像"]').click()
time.sleep(3)
d.xpath('//*[@content-desc="默认头像选择"]').click()
time.sleep(5)
d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ImageView[4]').click()
# time.sleep(2)
d.implicitly_wait(5)
# toas=d.xpath('//*[@content-desc="头像设置成功"]')
d.toast.show('cg')
# print(t)