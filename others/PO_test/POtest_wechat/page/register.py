from selenium.webdriver.common.by import By
from others.PO_test.POtest_wechat.page.base_page import BasePage


class Register(BasePage):
    # 填写注册信息，此处只填写了部分信息，并没有填写完全
    def register(self, corpname):
        # 进行表格填写
        self._driver.find_element(By.ID, "corp_name").send_keys(corpname)
        self._driver.find_element(By.ID, "submit_btn").click()
        # 填写完毕，停留在注册页，可继续调用Register内的方法 

    #填写错误时，返回错误信息
    def get_error_message(self):
        # 收集错误信息并返回
        result=[]
        for element in self._driver.find_elements(By.CSS_SELECTOR, ".js_error_msg"):
            result.append(element.text)

        return result