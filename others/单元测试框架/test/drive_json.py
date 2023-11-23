from selenium import webdriver
import unittest
import time as t
from selenium.webdriver.common.by import By

from others.单元测试框架.utils.operatioJson import readJson


class sinaTest(unittest.TestCase):
    def setUp(self) -> None: #前提
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None: #清理
        self.driver.quit()

    def test_sina_null(self):
        '''sina邮箱验证：登录账户为空'''
        self.driver.find_element(By.ID,'freename').send_keys(readJson()['loginNull']['username'])
        self.driver.find_element(By.ID,'freepassword').send_keys(readJson()['loginNull']['password'])
        self.driver.find_element(By.CLASS_NAME,'loginBtn').click()
        divText=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]')
        self.assertEqual(divText.text,readJson()['loginNull']['result'])

    def test_sina_email_format(self):
        '''sina邮箱验证：登录邮箱格式不正确'''
        self.driver.find_element(By.ID,'freename').send_keys(readJson()['emailFormat']['username'])
        self.driver.find_element(By.ID,'freepassword').send_keys(readJson()['emailFormat']['password'])
        self.driver.find_element(By.CLASS_NAME,'loginBtn').click()
        divText=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]')
        self.assertEqual(divText.text,readJson()['emailFormat']['result'])

    def test_sina_username_error(self):
        '''sina邮箱验证：登录账户密码不匹配'''
        self.driver.find_element(By.ID,'freename').send_keys(readJson()['loginError']['username'])
        self.driver.find_element(By.ID,'freepassword').send_keys(readJson()['loginError']['password'])
        self.driver.find_element(By.CLASS_NAME,'loginBtn').click()
        t.sleep(3)
        divText=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]')
        self.assertEqual(divText.text,readJson()['loginError']['result'])

if __name__ == '__main__':
    unittest.main()