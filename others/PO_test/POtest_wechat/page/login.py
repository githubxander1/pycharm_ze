from selenium.webdriver.common.by import By
from others.PO_test.POtest_wechat.page.base_page import BasePage
from others.PO_test.POtest_wechat.page.register import Register


class Login(BasePage):
    # 扫描二维码
    def scan_qrcode(self):
        pass
    # 进入注册页面
    def goto_registry(self):
        # self._driver.find_element(By.LINK_TEXT, "企业注册").click()
        self._driver.find_element(By.CSS_SELECTOR,'#tmp > div.index_head_info > a').click()
        return Register(self._driver)

# Login().goto_registry()
# time.sleep(5)