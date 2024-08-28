from selenium import webdriver
import unittest
import time as t
from selenium.webdriver.common.by import By

from others.单元测试框架.utils.operatioExcel import readExcel


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
        self.driver.find_element(By.ID,'freename').send_keys(readExcel()[0][0])
        self.driver.find_element(By.ID,'freepassword').send_keys(readExcel()[0][1])
        self.driver.find_element(By.CLASS_NAME,'loginBtn').click()
        t.sleep(3)
        divText=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[4]/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/span[实例25_批量生成PPT版荣誉证书]')
        self.assertEqual(divText.text,readExcel()[0][2])

    def test_sina_email_format(self):
        '''sina邮箱验证：登录邮箱格式不正确'''
        self.driver.find_element(By.ID,'freename').send_keys(readExcel()[1][0])
        self.driver.find_element(By.ID,'freepassword').send_keys(readExcel()[1][1])
        self.driver.find_element(By.CLASS_NAME,'loginBtn').click()
        t.sleep(3)
        divText=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[4]/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/span[实例25_批量生成PPT版荣誉证书]')
        self.assertEqual(divText.text,readExcel()[1][2])

    def test_sina_username_error(self):
        '''sina邮箱验证：登录账户密码不匹配'''
        self.driver.find_element(By.ID,'freename').send_keys(readExcel()[2][0])
        self.driver.find_element(By.ID,'freepassword').send_keys(readExcel()[2][1])
        self.driver.find_element(By.CLASS_NAME,'loginBtn').click()
        t.sleep(3)
        divText=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[4]/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/span[实例25_批量生成PPT版荣誉证书]')
        self.assertEqual(divText.text,readExcel()[2][2])

if __name__ == '__main__':
    unittest.main()