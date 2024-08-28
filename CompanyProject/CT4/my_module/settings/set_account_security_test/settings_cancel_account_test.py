from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, d

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")
setting=d(resourceId="com.app.ct4:id/settings")

account_security=d(resourceId="com.app.ct4:id/accountSecurity")


cancel_account=d(resourceId="com.app.ct4:id/cancelAccount")
close=d(resourceId="com.app.ct4:id/ivClose")
agree_check_box=d(resourceId="com.app.ct4:id/agreeCheckBox")
apply_cancellation=d(resourceId="com.app.ct4:id/applyCancellation")


class TestCancellation:
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
        cancel_account.click()
        yield
        sleep(1)
        back.click()



    def test_apply_cancellation_sus(self):
        agree_check_box.click()
        apply_cancellation.click()
        assert d.toast.get_message()=='申请成功'







if __name__ == '__main__':
    pytest.main(["-vs", '--reruns', '实例25_批量生成PPT版荣誉证书', "--html=report.html", 'settings_cancel_account_test.py::TestCancellation'])
