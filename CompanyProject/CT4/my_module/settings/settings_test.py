from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, btn_login, d

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")
cancel=d(resourceId="com.app.ct4:id/bt_cancel")
confirm=d(resourceId="com.app.ct4:id/bt_sure")

setting=d(resourceId="com.app.ct4:id/settings")

dark=d(resourceId="com.app.ct4:id/systemRadio1")
light=d(resourceId="com.app.ct4:id/systemRadio2")
system=d(resourceId="com.app.ct4:id/systemRadio3")

greenred=d(resourceId="com.app.ct4:id/colorRadio1")
redgreen=d(resourceId="com.app.ct4:id/colorRadio2")

customize=d(resourceId="com.app.ct4:id/colorRadio3")

custommode=d(resourceId="com.app.ct4:id/chartCustomMode")
chartsetting=d(resourceId="com.app.ct4:id/chartSetting")

timezone=d(resourceId="com.app.ct4:id/timeZone")
utc2=d.xpath('//*[@resource-id="com.app.ct4:id/recyclerView"]/android.view.ViewGroup[2]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.widget.CheckBox[实例25_批量生成PPT版荣誉证书]')
utc12=d.xpath('//*[@resource-id="com.app.ct4:id/recyclerView"]/android.view.ViewGroup[15]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.widget.CheckBox[实例25_批量生成PPT版荣誉证书]')

messagepush=d(resourceId="com.app.ct4:id/messagePush")
master_switch=d.xpath('//*[@resource-id="com.app.ct4:id/systemNotification"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
system_information=d.xpath('//*[@resource-id="com.app.ct4:id/systemInformation"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
newsletter=d.xpath('//*[@resource-id="com.app.ct4:id/newsletter"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
calendar=d.xpath('//*[@resource-id="com.app.ct4:id/pushCalendar"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
account_information=d.xpath('//*[@resource-id="com.app.ct4:id/pushAccountInfo"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')
early_warning_reminder=d.xpath('//*[@resource-id="com.app.ct4:id/pushWarning"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.view.View[实例25_批量生成PPT版荣誉证书]')

cache=d(text="Clear cache")

signout=d(resourceId="com.app.ct4:id/signOut")



class TestSetting:
    @pytest.fixture(scope='class',autouse=True)
    def setup_class(self):
        # 打开应用
        d.app_start("com.app.ct4")
        d.implicitly_wait(10)
        sleep(2)
        login_email()
        yield
        back.click()
        # 退出应用
        d.app_stop("com.app.ct4")

    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        sleep(2)
        # 点击设置
        setting.click()
        yield
        sleep(1)
        back.click()

    @pytest.mark.skip #暂时不做
    def test_dark(self):
        dark.click()
    def test_light(self):
        light.click()
    def test_system(self):
        system.click()
    #颜色模式
    def test_greenred(self):
        greenred.click()
    def test_redgreen(self):
        redgreen.click()
        #需完善
    def test_customize(self):
        customize.click()

    def test_custommode(self):
        custommode.click()
    def test_chartsetting(self):
        chartsetting.click()
    def test_timezone_2(self):
        d(scrollable=True).scroll.toEnd()
        timezone.click()
        d(scrollable=True).scroll.toEnd()
        utc2.click()
        save.click()
    def test_timezone_12(self):
        d(scrollable=True).scroll.toEnd()
        timezone.click()
        d(scrollable=True).scroll.toEnd()
        utc12.click()
        save.click()

    def test_messagepush(self):
        d(scrollable=True).scroll.toEnd()
        messagepush.click()
        back.click()
    def test_messagepush_master_switch(self):
        d(scrollable=True).scroll.toEnd()
        messagepush.click()
        master_switch.click()
        back.click()
    @pytest.mark.skip
    def test_messagepush_master_switch_off(self):
        d(scrollable=True).scroll.toEnd()
        messagepush.click()
        master_switch.click()
        back.click()

    def test_messagepush_system_information(self):
        d(scrollable=True).scroll.toEnd()
        messagepush.click()
        system_information.click()
        back.click()
    def test_messagepush_newsletter(self):
        d(scrollable=True).scroll.toEnd()
        messagepush.click()
        newsletter.click()
        back.click()
    def test_messagepush_calendar(self):
        d(scrollable=True).scroll.toEnd()
        messagepush.click()
        calendar.click()
        back.click()
    def test_messagepush_account_information(self):
        d(scrollable=True).scroll.toEnd()
        messagepush.click()
        account_information.click()
        back.click()
    def test_messagepush_early_warning_reminder(self):
        d(scrollable=True).scroll.toEnd()
        messagepush.click()
        early_warning_reminder.click()
        back.click()

    def test_cache(self):
        d(scrollable=True).scroll.toEnd()
        cache.click()

    def test_signout_cancel(self):
        d(scrollable=True).scroll.toEnd()
        signout.click()
        cancel.click()

    @pytest.mark.skip
    def test_signout_confirm(self):
        d(scrollable=True).scroll.toEnd()
        signout.click()
        confirm.click()
        assert btn_login.exists()




if __name__ == '__main__':
    pytest.main(["-vs",'--reruns','实例25_批量生成PPT版荣誉证书',"--html=report.html",'settings_test.py::TestSetting'])
    # pytest.main(["-vs",'--reruns','实例25_批量生成PPT版荣誉证书',"--html=report.html",'settings_test.py::TestLanguage::test_messagepush_master_switch'])
    # pytest.main(["-vs",'--reruns','实例25_批量生成PPT版荣誉证书',"--html=report.html"])
    # pytest.main(["-vs",'-k','test_messagepush_calendar','--reruns','实例25_批量生成PPT版荣誉证书',"--html=report.html"])
