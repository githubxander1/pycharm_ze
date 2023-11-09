from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, d

warning=d(resourceId="com.app.ct4:id/warning")

back=d(resourceId="com.app.ct4:id/tv_left")
right=d(resourceId="com.app.ct4:id/tv_right")


select_all=d(resourceId="com.app.ct4:id/cb_select_all")
delete=d(resourceId="com.app.ct4:id/btn_delete")
cancel=d(resourceId="com.app.ct4:id/btn_cancel")

add_warning=d(resourceId="com.app.ct4:id/btn_add")

add_stock=d(resourceId="com.app.ct4:id/tv_add_stock")
stock1=d.xpath('//*[@resource-id="com.app.ct4:id/rv_watchlist"]/android.view.ViewGroup[1]')

spinner_warn_type=d(resourceId="com.app.ct4:id/spinner_warn_type")
spinner_condition=d(resourceId="com.app.ct4:id/spinner_condition")
edit_price=d(resourceId="com.app.ct4:id/edit_price")
add_ew=d(resourceId="com.app.ct4:id/tv_add_ew")

push_system=d(resourceId="com.app.ct4:id/cb_system")
push_email=d(resourceId="com.app.ct4:id/cb_email")
edit_email=d(resourceId="com.app.ct4:id/edit_email")

push_message=d(resourceId="com.app.ct4:id/cb_sms")
country_code=d(resourceId="com.app.ct4:id/tv_countryCode")
edit_phone=d(resourceId="com.app.ct4:id/edit_phone")

remark=d(resourceId="com.app.ct4:id/edit_remark")


class TestAlert:
    @pytest.fixture(scope='class',autouse=True)
    def setup_class(self):
        d.app_start("com.app.ct4")
        d.implicitly_wait(10)
        sleep(2)
        login_email()
        warning.click()
        yield
        back.click()
        d.app_stop("com.app.ct4")
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        sleep(2)
        pass
        yield
        sleep(1)
        back.click()

    def test_add_warning_sus(self):
        add_warning.click()
        add_stock.click()
        stock1.click()

        push_system.click()
        push_email.click()
        edit_email.set_text('123456789@qq.com')

        push_message.click()
        country_code.click()
        edit_phone.send_keys('13111111111')
        remark.set_text('测试')
        add_warning.click()
        assert d.toast.get_message()=='添加成功'


if __name__ == '__main__':
    pytest.main(["-vs", '--reruns', '1', "--html=report.html", 'message_alerts_test.py::TestAlert'])
