from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:

    def __init__(self, driver: WebDriver):
        self._driver = driver
	# 注册功能封装
    def register(self):
        self._driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys('test123')
        self._driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys('13120991801')
        self._driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys('Aa123456')
        self._driver.find_element(By.ID, 'TANGRAM__PSP_4__verifyCode').send_keys('1234')
        self._driver.find_element(By.ID, 'TANGRAM__PSP_4__isAgree').click()
        self._driver.find_element(By.ID, 'TANGRAM__PSP_4__submit').click()
