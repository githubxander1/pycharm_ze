from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email, d

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")
language=d(resourceId="com.app.ct4:id/language")

english=d.xpath('//*[@resource-id="com.app.ct4:id/rv_languages"]/android.view.ViewGroup[1]/android.widget.ImageView[1]')
chinese=d.xpath('//*[@resource-id="com.app.ct4:id/rv_languages"]/android.view.ViewGroup[2]/android.widget.ImageView[1]')
taiwan=d.xpath('//*[@resource-id="com.app.ct4:id/rv_languages"]/android.view.ViewGroup[3]/android.widget.ImageView[1]')


class TestLanguage:
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
        # 点击头像
        language.click()
        yield
        sleep(1)
        back.click()

    def test_english(self):
        # 英文
        english.click()
        save.click()
        assert language.get_test()=='language'
    def test_chinese(self):
        # 英文
        chinese.click()
        save.click()
        assert language.get_test()=='语言'
    def test_twiwan(self):
        taiwan.click()
        save.click()
        assert language.get_test()=='語言'

    def test_unmodified(self):
        taiwan.click()
        save.click()
        back.click()
        language.click()
        taiwan.click()
        assert language.get_test()=='語言'

if __name__ == '__main__':
    pytest.main(["-s", "-v", '--reruns','2',"--html=report.html"])
