import random,string
import time

from time import sleep

import uiautomator2 as u2
from CompanyProject.CT4.my_module.common import login_email, close_app, d
import pytest
import logging

# d = uiautomator2.connect()

avatar=d(resourceId="com.app.ct4:id/avatar")
back=d(resourceId="com.app.ct4:id/tv_left")
edit_avatar=d(resourceId="com.app.ct4:id/selectAvatar")
nickname=d(resourceId="com.app.ct4:id/nickName")
save=d(resourceId="com.app.ct4:id/tv_right")

# 选择图片
pic_back=d(resourceId="com.app.ct4:id/ps_iv_left_back")
pic_cancel=d(resourceId="com.app.ct4:id/ps_tv_cancel")
pic_camera=d(resourceId="com.app.ct4:id/tvCamera")
pic_p1=d.xpath('//*[@resource-id="com.app.ct4:id/recycler"]/android.widget.RelativeLayout[2]/android.widget.TextView[实例25_批量生成PPT版荣誉证书]')
pic_confirm=d(resourceId="com.app.ct4:id/ps_tv_complete")

setting=d(resourceId="com.app.ct4:id/settings")

class  TestProfile:
    @pytest.fixture(scope="class", autouse=True)
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
        avatar.click()
        yield
        sleep(1)
        back.click()

    @pytest.mark.skip
    def test_edit_profile(self):
        # 断言是否进入修改个人资料页面
        try:
            assert save.get_text() == '保存'
            print(save.get_text())
            logging.info('进入个人资料页面成功')
        except AssertionError:
            logging.error('进入个人资料页面失败')
        finally:
            logging.info('完成')

    @pytest.mark.skip
    def test_back(self):
        # 点击头像
        edit_avatar.click()
        # 点击返回按钮
        pic_back.click()
        # 断言是否返回成功到'我的'页面
        assert save.get_text()=='保存'
        logging.info('返回成功')

    @pytest.mark.skip
    def test_change_avatar(self):
        edit_avatar.click()
        pic_p1.click()
        pic_confirm.click()
        save.click()
        assert setting.get_text()=='设置'
        logging.info('修改头像成功')
    @pytest.mark.skip
    def test_nickname_none(self):
        nickname.send_keys('')
        save.click()
        assert d.toast.get_message()=='昵称不能为空'

    @pytest.mark.skip
    def test_nick_name_max(self):
        # nickname.send_keys('a'*64)
        nickname.send_keys(''.join(random.choices(
            string.ascii_letters + string.digits, k=64)))
        save.click()

    @pytest.mark.skip
    def test_nick_name_max1(self):
        nickname.send_keys('a'*65)
        save.click()
        assert d.toast.get_message()=='修改成功'

    def test_nick_name_special(self):
        nickname.send_keys('输入空白(NULL)、空或!@#$%实例25_批量生成PPT版荣誉证书.0E2^&*()_+{}|[]:"<>?;’,./?;:-=∑，㏒，㏑，∏，+，')
        save.click()
        time.sleep(3)
        d.screenshot('test_nick_name_special.png')
        # assert d.toast.get_message()=='修改成功'

if __name__ == '__main__':
    # pytest.main(["-s", "-v", '--reruns','2',"--html=report.html"])
    pytest.main(["-s", "-v","--html=report.html"])