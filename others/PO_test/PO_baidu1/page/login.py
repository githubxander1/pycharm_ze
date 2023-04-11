from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from register import Register


class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    # 输入正确的账号和密码
    def login_success(self):
        self._driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('test123')
        self._driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('Aa123456')
        self._driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()

    # 输入错误的账号和密码
    def login_fail(self):
        self._driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('test123')
        self._driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('Aa123456')
        self._driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()

    # 跳转注册
    def goto_register(self):
        self._driver.find_element(By.ID, 'TANGRAM__PSP_11__regLink').click()
        windows = self._driver.window_handles
        self._driver.switch_to.window(windows[-1])
        return Register(self._driver)

    # 封装获取错误信息，用于后续断言实用
    def get_error_message(self):
        error_element = self._driver.find_element(By.ID, 'TANGRAM__PSP_11__error')
        error_value = error_element.text
        print(error_value)
        return error_value

