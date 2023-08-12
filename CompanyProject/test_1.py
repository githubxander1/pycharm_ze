import unittest
import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options


class TestLogin(unittest.TestCase):
    def setUp(self):
        options = Options()
        # options.add_argument("--headless")
        options.add_experimental_option("headless", True)
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://testfb.tostar.top/cn")

    def tearDown(self):
        self.driver.quit()

    def test_login_success_toast(self):
        avatar = self.driver.find_element(By.ID, 'login_btn-main')
        ActionChains(self.driver).move_to_element(avatar).perform()

        self.driver.find_element(By.ID, 'login_btn').click()
        self.driver.find_element(By.ID, 'loginMethodMail').click()
        self.driver.find_element(By.ID, 'inputMailText').send_keys('7@qq.com')
        self.driver.find_element(By.ID, 'inputMailPwd').send_keys('a1234567')
        self.driver.find_element(By.ID, 'mailBtn').click()

        toast = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.toast-main > div > span")))
        toast_text = toast.text

        self.assertIn("登录成功", toast_text)


if __name__ == "__main__":
    # unittest.main()
    unittest.main(testRunner=unittest.TextTestRunner(stream=open("test_report.txt", "w")))
