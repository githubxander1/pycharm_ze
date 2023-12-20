import time

import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CompanyProject.Fastbull.UI_Fastbull.page.login_page import Login
from CompanyProject.Fastbull.WEB_FB_PosterMaker.base import Base


class Home(Base):
    msgEditor=(By.XPATH,'//*[@id="app"]/div/main/div/div[3]/footer/div[1]/div[1]/div/div')
    def input_msg(self,msg):
        self.d.find_element(*self.msgEditor).send_keys(msg)

    send_btn = (By.XPATH, '//*[@id="app"]/div/main/div/div[2]/footer/div[2]/svg')
    def click_send(self):
        self.d.find_element(*self.send_btn).click()

    # friend=(By.XPATH,'//*[@id="app"]/div/header/ul/li[3]')
    friend=(By.CSS_SELECTOR,'#app > div > header > ul > li:nth-child(3)')
    def click_friend(self):
        WebDriverWait(self.d, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/header/ul/li[3]')))
        if self.d.find_element(*self.friend).is_displayed():
            if self.d.find_element(*self.friend).is_enabled():
                print('元素可见且可点击')
                self.d.find_element(*self.friend).click()
        else:
            print('元素不存在')
        self.d.find_element(*self.friend).click()
    friend1=(By.XPATH,'//*[@id="con_835201618067063063"]')
    def click_friend1(self):
        self.d.find_element(*self.friend1).click()
    def friend_chat(self,msg):
        self.click_friend()
        self.click_friend1()
        self.input_msg(msg)
        self.click_send()


if __name__ == '__main__':
    d = webdriver.Edge()
    login = Login(d)
    login.login('7@qq.com', 'a1234567')
    time.sleep(50)
    friendchat=Home(d)
    friendchat.friend_chat('test')

