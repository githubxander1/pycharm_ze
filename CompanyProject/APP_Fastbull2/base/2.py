import uiautomator2 as u2

d = u2.connect_adb_wifi('192.168.5.220:5555')
# d = u2.connect_adb_wifi('192.168.31.28:5555')
# d = u2.connect_adb_wifi('192.168.5.179:5555')
# d = u2.connect('1c0bde47')
# d = u2.connect('5ENDU18C21003487')

class Home():
    contact = d.xpath(
        '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]')
if __name__ == '__main__':

    d.app_start('com.bv.forexchat')
    # print(d.info)
    home=Home()
    home.contact.click()