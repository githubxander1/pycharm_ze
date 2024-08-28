from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, d

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")
setting=d(resourceId="com.app.ct4:id/settings")

account_security=d(resourceId="com.app.ct4:id/accountSecurity")

auto_login=d(resourceId="com.app.ct4:id/autoLogin")
auto_login_switch=d(resourceId="com.app.ct4:id/slideBtn")
no_authentication=d(resourceId="com.app.ct4:id/systemRadio1")
faceID=d(resourceId="com.app.ct4:id/systemRadio2")
gesture_password=d(resourceId="com.app.ct4:id/systemRadio3")

privacy_protection=d(resourceId="com.app.ct4:id/privacyProtection")
cancel_account=d(resourceId="com.app.ct4:id/cancelAccount")

class TestPhone:
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
        auto_login.click()
        yield
        sleep(1)
        back.click()



    def test_auto_login(self):
        auto_login_switch.click()

    def test_no_authentication(self):
        no_authentication.click()

    def test_faceID(self):
        faceID.click()

    def test_gesture_password(self):
        gesture_password.click()







if __name__ == '__main__':
    pytest.main(["-vs", '--reruns', '实例25_批量生成PPT版荣誉证书', "--html=report.html", 'settings_login_password_test.py::TestPhone'])
