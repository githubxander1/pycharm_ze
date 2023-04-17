import sys
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from others.PO_mindmaster.basepage.homeBase import HomePage

sys.path.append('../basepage')
# from homeBase import HomePage

# 分别定义该页面需要用到的元素
class LoginPage(HomePage):
    ifr=(By.XPATH, '//*[@id="edraw-authorization--wrapper"]/iframe')
    tabCount_loc=(By.XPATH,'//*[@id="tab-account"]')
    username_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[1]/form/div[1]/div/div/div/div[1]/input')
    password_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[1]/form/div[2]/div/div/input')
    loginBtn_loc=(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/button')
    # 用户名为空
    userNull_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[1]/form/div[1]/div/div[2]')
    passwordNull_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[1]/form/div[2]/div/div[2]')
    # 打开网站，切换到登录表单
    def openLoginPage(self,username,password):
        self.dr=webdriver.Edge()
        self.dr.get('https://mm.edrawsoft.cn/files')
        sleep(2)
        # 切换到登录表单
        self.iframe = self.dr.find_element(By.XPATH, '//*[@id="edraw-authorization--wrapper"]/iframe')
        self.dr.switch_to.frame(self.iframe)
        time.sleep(3)
        # 点击账密登录
        # d.find_element_by_xpath('//li[contains(string(),"{}")]'.format(number)).click()
        # self.dr.find_element(By.XPATH, '{}'.format(self.tabCount_loc)).click()
        self.dr.find_element(By.XPATH, '//*[@id="tab-account"]').click()
        self.dr.find_element(By.XPATH, '//*[@id="pane-account"]/div/div[1]/form/div[1]/div/div/div/div[1]/input').send_keys(
            username)
        self.dr.find_element(By.XPATH, '//*[@id="pane-account"]/div/div[1]/form/div[2]/div/div/input').send_keys(
            password)
        self.dr.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/button').click()
        time.sleep(3)
    # 点击账密登录
    def click_tabCount(self):
        self.find_element(*self.tabCount_loc).click()
    # 切换到登录弹窗
    def switch_to_iframe(self):
        iframe = self.find_element(*self.ifr)
        self.dr.switch_to.frame(iframe)
    # 输入用户名
    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    def input_password(self,password):
        self.find_element(*self.password_loc).send_Keys(password)
    def click_loginbtn(self):
        self.find_element(*self.loginBtn_loc).click()

    # 获取登录提示信息
    def get_assertText(self):
        return self.find_element(*self.loginBtn_loc).text
    def get_userNullText(self):
        return self.find_element(*self.userNull_loc).text
    def get_passwordNullText(self):
        return self.find_element(*self.passwordNull_loc).text

    # 组装登录流程
    def login_mind_pro(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_loginbtn()

