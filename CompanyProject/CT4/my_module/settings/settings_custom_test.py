from time import sleep

import uiautomator2 as u2
import pytest

from CompanyProject.CT4.my_module.common import login_email

d=u2.connect()

back=d(resourceId="com.app.ct4:id/tv_left")
save=d(resourceId="com.app.ct4:id/tv_right")

setting=d(resourceId="com.app.ct4:id/settings")

dark=d(resourceId="com.app.ct4:id/systemRadio1")
light=d(resourceId="com.app.ct4:id/systemRadio2")
system=d(resourceId="com.app.ct4:id/systemRadio3")

greenred=d(resourceId="com.app.ct4:id/colorRadio1")
redgreen=d(resourceId="com.app.ct4:id/colorRadio2")

customize=d(resourceId="com.app.ct4:id/colorRadio3")

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
        # 点击设置
        setting.click()
        yield
        sleep(1)
        back.click()







if __name__ == '__main__':
    pytest.main(["-s", "-v", '--reruns','2',"--html=report.html"])
