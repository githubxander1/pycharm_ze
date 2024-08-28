from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, d

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")
setting=d(resourceId="com.app.ct4:id/settings")

account_security=d(resourceId="com.app.ct4:id/accountSecurity")

password_set=d.xpath('//*[@resource-id="com.app.ct4:id/loginPassword"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.widget.TextView[2]')
current_pwd=d(resourceId="com.app.ct4:id/oldPassword")
new_pwd=d(resourceId="com.app.ct4:id/newPassword")
confirm_pwd=d(resourceId="com.app.ct4:id/confirmPassword")

phone_set=d.xpath('//*[@resource-id="com.app.ct4:id/phoneNumber"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.widget.TextView[2]')
phone_input_password=d(text="Enter Password")

email_set=d.xpath('//*[@resource-id="com.app.ct4:id/emailAddress"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.widget.TextView[2]')
twitter=d(resourceId="com.app.ct4:id/status", text="Untie")
google=d.xpath('//*[@resource-id="com.app.ct4:id/qq"]/android.view.ViewGroup[实例25_批量生成PPT版荣誉证书]/android.widget.TextView[2]')

auto_login=d(resourceId="com.app.ct4:id/autoLogin")
privacy_protection=d(resourceId="com.app.ct4:id/privacyProtection")
cancel_account=d(resourceId="com.app.ct4:id/cancelAccount")

class TestPassword:
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
        password_set.click()
        yield
        sleep(1)
        back.click()



    def test_password_set_current_null(self):
        current_pwd.send_keys('')
        new_pwd.send_keys('')
        confirm_pwd.send_keys('')
        save.click()
        assert d.toast.get_message()=='密码不能为空'
    def test_password_set_new_null(self):
        current_pwd.send_keys('a1234567')
        new_pwd.send_keys('')
        confirm_pwd.send_keys('')
        save.click()
        assert d.toast.get_message()=='新密码不能为空'
    def test_password_set_confirm_null(self):
        current_pwd.send_keys('a1234567')
        new_pwd.send_keys('a1234567')
        confirm_pwd.send_keys('')
        save.click()
        assert d.toast.get_message()=='新密码不能为空'

    def test_password_set_current_error(self):
        current_pwd.send_keys('a1')
        new_pwd.send_keys('a1234567')
        confirm_pwd.send_keys('a1234567')
        save.click()
        assert d.toast.get_message() == '密码错误'
    def test_password_set_current_less8(self):
        current_pwd.send_keys('a1234567')
        new_pwd.send_keys('a123456')
        confirm_pwd.send_keys('a123456')
        save.click()
        assert d.toast.get_message() == '密码长度不足'
    def test_password_set_current_65(self):
        current_pwd.send_keys('a1234567')
        new_pwd.send_keys('a1'*65)
        confirm_pwd.send_keys('a1'*65)
        save.click()
        assert d.toast.get_message() == '密码错误'
    def test_password_set_new_notEqual_confirm(self):
        current_pwd.send_keys('a1234567')
        new_pwd.send_keys('a1')
        confirm_pwd.send_keys('a2')
        save.click()
        assert d.toast.get_message() == '两次密码不一致'


    def test_password_success(self):
        password_set.click()
        current_pwd.send_keys('a1234567')
        new_pwd.send_keys('a12345678')
        confirm_pwd.send_keys('a12345678')
        save.click()
        assert d.toast.get_message()=='修改成功'





if __name__ == '__main__':
    pytest.main(["-vs", '--reruns', '实例25_批量生成PPT版荣誉证书', "--html=report.html", 'settings_login_password_test.py::TestPassword'])
