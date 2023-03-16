
from selenium.webdriver.common.by import By
from others.POtest_wechat.page.base_page import BasePage

class Login(BasePage):
    # 扫描二维码
    def scan_qrcode(self):
        pass
    # 进入注册页面
    def goto_registry(self):
        self._driver.find_element(By.LINK_TEXT, "企业注册").click()
        return Register(self._driver)