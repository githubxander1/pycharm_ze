from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, d

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")
setting=d(resourceId="com.app.ct4:id/settings")

account_security=d(resourceId="com.app.ct4:id/accountSecurity")


email_set=d.xpath('//*[@resource-id="com.app.ct4:id/emailAddress"]/android.view.ViewGroup[1]/android.widget.TextView[2]')
twitter=d(resourceId="com.app.ct4:id/status", text="Untie")
google=d.xpath('//*[@resource-id="com.app.ct4:id/qq"]/android.view.ViewGroup[1]/android.widget.TextView[2]')

auto_login=d(resourceId="com.app.ct4:id/autoLogin")
privacy_protection=d(resourceId="com.app.ct4:id/privacyProtection")
cancel_account=d(resourceId="com.app.ct4:id/cancelAccount")

class TestEmail:
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
        pass
        # email_set.click()
        yield
        sleep(1)
        back.click()



    def test_untie(self):
        email_set.click()
        sleep(2)






if __name__ == '__main__':
    pytest.main(["-vs", '--reruns', '1', "--html=report.html", 'settings_login_password_test.py::TestEmail'])
