import time

import allure
import cv2
import requests
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver

from CompanyProject.Fastbull.WEB_FB_PosterMaker.base import Base


class Login(Base):
    # url='https://testfb.tostar.top/cn/login?next=/cn'
    url='https://beta.fastbull.com/cn/'

    inputPhoneText=(By.ID,'inputPhoneText')
    spand=(By.XPATH,'//*[@id="app"]/div/header/div/i[2]')

    def input_phone(self,phone):
        self.d.find_element(*self.inputPhoneText).send_keys(phone)

    codeBtn=(By.ID,'codeBtn')
    def click_code(self):
        self.d.find_element(*self.codeBtn).click()

    inputCodeText=(By.ID,'inputCodeText')
    def input_code(self,code):
        self.d.find_element(*self.inputCodeText).send_keys(code)

    security_verify_iframe=(By.XPATH,'/html/body/iframe')
    def switch_to_iframe(self):
        self.d.switch.to_frame(self.security_verify_iframe)

   # while True:
        # 获取验证码图片
        img_bj=self.d.find_element(By.XPATH,'//*[@id="app"]/main/div/div/div[2]')
        img_hk=self.d.find_element(By.XPATH,'//*[@id="app"]/main/div/div/div[2]/i')
        # 获取原图下载地址
        src_bj=img_bj.get_attribute('src')
        src_hk=img_hk.get_attribute('src')

        # 通过reques下载图片的二进制码
        content=requests.get(src_bj).content
        f=open('bj.png','wb')
        f.write(content)
        f.close()

        content=requests.get(src_hk).content
        f=open('hk.png','wb')
        f.write(content)
        f.close()

        def get_dis():
            # 解析x距离
            # 读取背景图片的rgb码
            bj_rgb=cv2.imread('bj.png')
            # 灰度处理
            bj_gray=cv2.cvtColor(bj_rgb,cv2.COLOR_RGB2GRAY)
            # 读取滑块的rgb码
            hk_rgb=cv2.imread('hk.png')
            # # 灰度处理
            # hk_gray=cv2.cvtColor(hk_rgb,cv2.COLOR_RGB2GRAY)
            # 匹配滑块在背景图的位置
            res=cv2.matchTemplate(bj_gray,hk_rgb,cv2.TM_CCOEFF_NORMED)
            # 获取位置
            lo=cv2.minMaxLoc(res)
            print(lo[2][0])
            return lo[2][0]
            # 计算缩放
            x=int(x * 178/267)

            # 开始拖动滑块
            action = ActionChains(d)
            action.click_and_hold(img_hk).perform()
            action.move_by_offset(xoffset=x, yoffset=0)  # 拖动的距离可能需要根据实际滑块长度调整
            action.release(img_hk).perform()
            # action.perform()

            slider = WebDriverWait(d, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/main/div/div/div[2]/i'))
            )
            # 获取滑块的初始位置
            initial_slider_location = slider.location

            # 获取滑块的父元素
            slider_parent = slider.find_element(By.XPATH,"..")
            # 等待验证成功的元素出现（这里假设验证成功后会显示一个隐藏的元素）
            try:
                WebDriverWait(d, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='verification-success']"))
                )
                print("滑块验证成功")
            except TimeoutException:
                print("滑块验证失败")

    phoneBtn=(By.ID,'phoneBtn')
    def click_phoneBtn(self):
        self.d.find_element(*self.phoneBtn).click()


    loginMethodMail=(By.ID,'loginMethodMail')
    inputMailText=(By.ID,'inputMailText')
    inputMailPwd=(By.ID,'inputMailPwd')
    mailBtn=(By.ID,'mailBtn')
    def click_mailBtn(self):
        self.d.find_element(*self.mailBtn).click()
    def input_pwd(self,pwd):
        self.d.find_element(*self.inputMailPwd).send_keys(pwd)
    def input_email(self,email):
        self.d.find_element(*self.inputMailText).send_keys(email)
    def click_emali(self):
        self.d.find_element(*self.loginMethodMail).click()
    @allure.step('登录')
    def login_phone(self,phone,code):
        self.open_url(self.url)
        self.input_phone(phone)
        self.click_code()
        self.switch_to_iframe()

        self.input_code(code)

        self.click_phoneBtn()
        time.sleep(3)
        # if self.d.current_url == 'https://testfb.tostar.top/cn':
        #     print('登录成功')
        # else:
        #     print('登录失败')
    def login_email(self,email,pwd):
        self.open_url(self.url)
        self.click_emali()
        self.input_email(email)
        self.input_pwd(pwd)
        self.click_mailBtn()
        time.sleep(3)
        # if self.d.current_url == 'https://testfb.tostar.top/cn':
        #     print('登录成功')
        # else:
        #     print('登录失败')

if __name__ == '__main__':
    d=webdriver.Edge()
    login=Login(d)
    # login.login_email('7@qq.com', 'a1234567')
    login.login_phone('13111111111', '1234')
