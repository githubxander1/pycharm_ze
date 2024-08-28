from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, d

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")
setting=d(resourceId="com.app.ct4:id/settings")

account_security=d(resourceId="com.app.ct4:id/accountSecurity")

privacy_protection=d(resourceId="com.app.ct4:id/privacyProtection")
asset_protection=d.xpath('//*[@resource-id="com.app.ct4:id/blurPageSwitch"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
turnOn_faceID_recognition=d.xpath('//*[@resource-id="com.app.ct4:id/faceRecognitionSwitch"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
turnOn_gesture_password=d.xpath('//*[@resource-id="com.app.ct4:id/gestureRecognitionSwitch"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
background_hold_time=d(resourceId="com.app.ct4:id/backgroundHoldTime")

modify_gesture_password=d(resourceId="com.app.ct4:id/modifyGesturePassword")
close=d(resourceId="com.app.ct4:id/ivClose")
every_time_open=d(resourceId="com.app.ct4:id/radio1")
five_minutes=d(resourceId="com.app.ct4:id/radio2")
ten_minutes=d(resourceId="com.app.ct4:id/radio3")
twenty_minutes=d(resourceId="com.app.ct4:id/radio4")
thirty_minutes=d(resourceId="com.app.ct4:id/radio5")

cancel_account=d(resourceId="com.app.ct4:id/cancelAccount")

class TestAssertPrivacy:
    @pytest.fixture(scope='class',autouse=True)
    def setup_class(self):
        d.app_start("com.app.ct4")
        d.implicitly_wait(10)
        sleep(2)
        login_email()
        setting.click()
        account_security.click()
        yield
        back.click()
        d.app_stop("com.app.ct4")
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        sleep(2)
        privacy_protection.click()
        yield
        sleep(1)
        back.click()

    def test_asset_privacy(self):
        asset_protection.click()

    def test_turnOn_faceID_recognition(self):
        turnOn_faceID_recognition.click()
    def test_turnOn_gesture_password(self):
        turnOn_gesture_password.click()
    def test_background_hold_time_every(self):
        d(scrollable=True).scroll.toEnd()
        background_hold_time.click()
        every_time_open.click()
        close.click()
    def test_background_hold_time_five_minutes(self):
        d(scrollable=True).scroll.toEnd()
        background_hold_time.click()
        five_minutes.click()
        close.click()
    def test_background_hold_time_ten_minutes(self):
        d(scrollable=True).scroll.toEnd()
        background_hold_time.click()
        ten_minutes.click()
        close.click()
    def test_background_hold_time_twenty_minutes(self):
        d(scrollable=True).scroll.toEnd()
        background_hold_time.click()
        twenty_minutes.click()
        close.click()
    def test_background_hold_time_thirty_minutes(self):
        d(scrollable=True).scroll.toEnd()
        background_hold_time.click()
        thirty_minutes.click()
        close.click()

    def test_modify_gesture_password(self):
        d(scrollable=True).scroll.toEnd()
        modify_gesture_password.click()
        # five_minutes.click()
        close.click()









if __name__ == '__main__':
    pytest.main(["-vs", '--reruns', '实例25_批量生成PPT版荣誉证书', "--html=report.html", 'settings_login_password_test.py::TestAssertPrivacy'])
