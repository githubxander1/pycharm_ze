import uiautomator2
# from ..common import login_email
from CompanyProject.CT4.common import login_email, close_app
import unittest

d = uiautomator2.connect()
d.app_start("com.app.ct4")
login_email()
d(resourceId="com.app.ct4:id/avatar").click()

class TestProfile(unittest):
    def setUp(self):
        pass
    def setDown(self):
        pass
    def test_back(self):
        d(resourceId="com.app.ct4:id/tv_left").click()
    def test_avatar(self):
        d(resourceId="com.app.ct4:id/selectAvatar").click()
    def test_nickname(self):
        d(resourceId="com.app.ct4:id/nickName").send_keys('ct2_1')


# close_app()