from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, d

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")

about=d(resourceId="com.app.ct4:id/aboutUs")
feedback=d(resourceId="com.app.ct4:id/feedback")
suggestions_edit=d(resourceId="com.app.ct4:id/suggestionsEdit")

add_image=d(resourceId="com.app.ct4:id/addIcon")
camera=d(resourceId="com.app.ct4:id/tvCamera")
select_picture1=d.xpath('//*[@resource-id="com.app.ct4:id/recycler"]/android.widget.RelativeLayout[2]/android.widget.TextView[实例25_批量生成PPT版荣誉证书]')
select_picture2=d.xpath('//*[@resource-id="com.app.ct4:id/recycler"]/android.widget.RelativeLayout[3]/android.widget.TextView[实例25_批量生成PPT版荣誉证书]')
select_picture3=d.xpath('//*[@resource-id="com.app.ct4:id/recycler"]/android.widget.RelativeLayout[4]/android.widget.TextView[实例25_批量生成PPT版荣誉证书]')
select_picture4=d.xpath('//*[@resource-id="com.app.ct4:id/recycler"]/android.widget.RelativeLayout[5]/android.widget.TextView[实例25_批量生成PPT版荣誉证书]')
select_confirm=d(resourceId="com.app.ct4:id/ps_tv_complete")
select_cancel=d(resourceId="com.app.ct4:id/ps_tv_cancel")
select_preview=d(resourceId="com.app.ct4:id/ps_tv_preview")
btn_ok=d(resourceId="com.app.ct4:id/btnOk")

contact_edit=d(resourceId="com.app.ct4:id/contactEdit")
submit=d(resourceId="com.app.ct4:id/confirm")

class TestFeedback:
    @pytest.fixture(scope='class',autouse=True)
    def setup_class(self):
        d.app_start("com.app.ct4")
        d.implicitly_wait(10)
        sleep(2)
        login_email()
        about.click()
        yield
        back.click()
        d.app_stop("com.app.ct4")
    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown(self):
        sleep(2)
        feedback.click()
        yield
        sleep(1)
        back.click()

    @pytest.mark.skip
    def test_feedback_sus(self):
        suggestions_edit.send_keys("测试反馈")
        add_image.click()
        select_picture1.click()
        select_picture2.click()
        select_picture3.click()
        select_confirm.click()
        contact_edit.send_keys("18888888888")
        submit.click()

        assert d.toast.get_message()=='提交成功'







if __name__ == '__main__':
    pytest.main(["-vs", '--reruns', '实例25_批量生成PPT版荣誉证书', "--html=report.html", 'feedback_test.py::TestFeedback'])
