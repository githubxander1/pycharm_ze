import time

import allure
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

from CompanyProject.Fastbull.WEB_FB_PosterMaker.base import Base


class Login(Base):
    url='https://testfb.tostar.top/cn/login?next=/cn'

    loginMethodMail=(By.ID,'loginMethodMail')
    inputMailText=(By.ID,'inputMailText')
    inputMailPwd=(By.ID,'inputMailPwd')
    mailBtn=(By.ID,'mailBtn')
    def click_login(self):
        self.d.find_element(*self.mailBtn).click()
    def input_pwd(self,pwd):
        self.d.find_element(*self.inputMailPwd).send_keys(pwd)
    def input_email(self,email):
        self.d.find_element(*self.inputMailText).send_keys(email)
    def click_emali(self):
        self.d.find_element(*self.loginMethodMail).click()
    @allure.step('登录')
    def login(self,email,pwd):
        self.open_url(self.url)
        self.click_emali()
        self.input_email(email)
        self.input_pwd(pwd)
        self.click_login()
        time.sleep(3)
        # if self.d.current_url == 'https://testfb.tostar.top/cn':
        #     print('登录成功')
        # else:
        #     print('登录失败')

if __name__ == '__main__':
    d=webdriver.Edge()
    login=Login(d)
    login.login('7@qq.com', 'a1234567')
