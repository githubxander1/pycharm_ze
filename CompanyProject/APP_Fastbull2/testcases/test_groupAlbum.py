import time
import pytest
import logging

from CompanyProject.APP_Fastbull2.common.logger import create_logger
from CompanyProject.APP_Fastbull2.operation.ChatWindows.GroupWindow import GroupWindow
from CompanyProject.APP_Fastbull2.base.basePage import Base1, d
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupAlbum.GroupAlbum import GroupAlbum
from CompanyProject.APP_Fastbull2.operation.GroupSet.GroupSet import GroupSet
from CompanyProject.APP_Fastbull2.operation.op_Home import Home

# 设置日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Test_groupAlbum():
    def __init__(self):
        self.logger = create_logger(__name__)
    @pytest.fixture(autouse=True)
    def setup(self):
        Base1().startApp()
        self.logger.info("App启动")
        logging.info("App启动成功")
        time.sleep(5)
        Home().click_conversation()
        logging.info("进入对话列表")
        GroupWindow().click_groupSet()
        logging.info("进入群组设置")
        GroupSet().click_groupAlbum()
        logging.info("进入群相册")
        yield
        time.sleep(3)
        Base1().closeApp()
        logging.info("App关闭成功")

    # def test_create_new_album(setup):
    #     GroupAlbum().createnewalbum('name3', 'de')
    #     logging.info("创建新相册成功")
        # assert groupAlbum.creatNewalbum.exists
    def test_create_new_album_namewithsensitive(setup):
        self.logger.info("创建新相册成功")
        GroupAlbum().createnewalbum('name3', 'de')
        logging.info("含敏感词")
        # 等待toast出现并获取提示内容
        toast = d.toast.get_message(wait=True)
        print(toast)

        # 断言toast的提示内容
        assert "Expected Toast Message" in toast


if __name__ == "__main__":
    pytest.main([__file__,"--capture=tee-sys"])