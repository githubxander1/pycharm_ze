import sys
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from others.PO_mindmaster.basepage.baseBase import BasePage

sys.path.append('../basepage')
# from homeBase import HomePage

# 分别定义该页面需要用到的元素
class LoginPage(BasePage):
    url = 'https://mm.edrawsoft.cn/files'
    dr = webdriver.Edge()

    ifr=(By.XPATH, '//*[@id="edraw-authorization--wrapper"]/iframe')
    tabCount_loc=(By.XPATH,'//*[@id="tab-account"]')
    username_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[实例25_批量生成PPT版荣誉证书]/form/div[实例25_批量生成PPT版荣誉证书]/div/div/div/div[实例25_批量生成PPT版荣誉证书]/input')
    password_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[实例25_批量生成PPT版荣誉证书]/form/div[2]/div/div/input')
    loginBtn_loc=(By.XPATH,'/html/body/div[实例25_批量生成PPT版荣誉证书]/div[2]/div/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[2]/button')


    # 用户名为空
    userNull_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[实例25_批量生成PPT版荣誉证书]/form/div[实例25_批量生成PPT版荣誉证书]/div/div[2]')
    passwordNull_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[实例25_批量生成PPT版荣誉证书]/form/div[2]/div/div[2]')

    # account_or_password_error_loc=(By.CSS_SELECTOR,'#pane-account > div > div.el-row.is-justify-space-around.el-row--flex > form > div.el-form-item.is-error.is-required.is-no-asterisk > div > div.el-form-item__error')
    account_or_password_error_loc=(By.XPATH,'//*[@id="pane-account"]/div/div[实例25_批量生成PPT版荣誉证书]/form/div[2]/div/div[2]')

    # def __init__(self):
    #     super().__init__()
        # self.dr.get(self.url)

    # 打开网站，切换到登录表单
    def openLoginPage(self,username,password):
        self.dr = webdriver.Edge()
        self.url = 'https://mm.edrawsoft.cn/files'
        self.dr.get(self.url)
        sleep(2)
        # 切换到登录表单
        self.iframe = self.locator(self.ifr)
        self.dr.switch_to.frame(self.iframe)
        time.sleep(3)
        # 点击账密登录
        # d.find_element(By.XPATH,'//li[contains(string(),"{}")]'.format(number)).click()
        # self.dr.locator(By.XPATH, '{}'.format(self.tabCount_loc)).click()
        self.click(self.locator(self.tabCount_loc))
        self.send_keys(self.locator(self.username_loc),username)
        self.send_keys(self.locator(self.password_loc),password)
        self.click(self.locator(self.loginBtn_loc))
        time.sleep(3)
    # 点击账密登录
    def click_tabCount(self):
        self.click(self.locator(self.tabCount_loc))
    # 切换到登录弹窗
    def switch_to_iframe(self):
        iframe = self.locator(self.ifr)
        self.dr.switch_to.frame(iframe)
    # 输入用户名
    def input_username(self,username):
        self.send_keys(self.locator(self.username_loc),username)
    def input_password(self,password):
        self.send_keys(self.locator(self.password_loc),password)
    def click_loginbtn(self):
        self.click(self.locator(self.loginBtn_loc))

    # def click_account_or_password_error(self):
    #     self.locator(*self.account_or_password_error_loc).click()

    # 获取登录提示信息
    def get_assertText(self):
        return self.locator(*self.loginBtn_loc).text
    def get_userNullText(self):
        return self.locator(*self.userNull_loc).text
    def get_passwordNullText(self):
        return self.locator(*self.passwordNull_loc).text

    # 组装登录流程
    def login_mind_pro(self,username,password):
        self.open_url(self.url)
        time.sleep(2)
        self.switch_to_iframe()
        self.input_username(username)
        self.input_password(password)
        self.click_loginbtn()

# url='https://mm.edrawsoft.cn/files'
# dr=webdriver.Edge()
loginpage = LoginPage()
# loginpage.login_mind_pro('2695418206@qq.com', 'your_password')
loginpage.openLoginPage('2695418206@qq.com', 'your_password')