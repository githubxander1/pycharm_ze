import time

import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CompanyProject.Fastbull.UI_Fastbull.page.login_page import Login
from CompanyProject.Fastbull.WEB_FB_PosterMaker.base import Base


class Home(Base):
    cookie_accept_bt=(By.XPATH,'//*[@id="leftBox"]/div[1]/div[1]/div[4]/div/div[2]')
    def click_cookie_accept_bt(self):
        self.d.find_element(*self.cookie_accept_bt).click()
    share_close=(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/i')
    def click_share_close(self):
        self.d.find_element(*self.share_close).click()

    chat_iframe=(By.ID,'chat_iframe')
    def switch_to_chat_iframe(self):
        self.d.switch_to.frame(self.d.find_element(*self.chat_iframe))

    msgEditor=(By.XPATH,'//*[@id="app"]/div/main/div/div[3]/footer/div[1]/div[1]/div/div')
    def input_msg(self,msg):
        self.d.find_element(*self.msgEditor).send_keys(msg)

    # send_btn = (By.XPATH, '//*[@id="app"]/div/main/div/div[2]/footer/div[2]/svg')
    # send_btn = (By.XPATH, '/html/body/div[1]/div/main/div/div[3]/footer/div[2]/svg')
    send_btn = (By.XPATH, '//*[@id="app"]/div/main/div/div[2]/footer/div[2]/svg/use')
    def click_send(self):
        time.sleep(1)
        if self.d.find_element(*self.send_btn).is_displayed():
            if self.d.find_element(*self.send_btn).is_enabled():
                print('元素可见且可点击')
                self.d.find_element(*self.send_btn).click()
        else:
            print('元素不存在')

    # friend=(By.XPATH,'//*[@id="app"]/div/header/ul/li[3]')
    friend=(By.CSS_SELECTOR,'#app > div > header > ul > li:nth-child(3)')
    def click_friend(self):
        # WebDriverWait(self.d, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/header/ul/li[3]')))
        # if self.d.find_element(*self.friend).is_displayed():
        #     if self.d.find_element(*self.friend).is_enabled():
        #         print('元素可见且可点击')
        self.d.find_element(*self.friend).click()
        # else:
        #     print('元素不存在')
    friend1=(By.XPATH,'//*[@id="con_835224111725151365"]')
    def click_friend1(self):
        self.d.find_element(*self.friend1).click()
    def friend_chat(self,msg):
        self.click_cookie_accept_bt()
        # self.click_share_close()
        self.switch_to_chat_iframe()
        self.click_friend()
        self.click_friend1()
        self.input_msg(msg)
        self.click_send()


if __name__ == '__main__':
    d = webdriver.Chrome()
    login = Login(d)
    login.login_email('forex1@linshiyou.com', 'a1234567')
    # time.sleep(10)
    friendchat=Home(d)
    friendchat.friend_chat('test')

