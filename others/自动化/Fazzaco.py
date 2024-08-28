# from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# import re
import random
import string
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def wait_elevisible_click(n_driver,locator, by=By.XPATH, wait=30, requence=0.5,t_sleep=0):
    ele = WebDriverWait(n_driver, wait, requence).until(EC.visibility_of_element_located((by, locator)))
    time.sleep(t_sleep)
    ele.click()


def wait_elevisible_return( n_driver,locator, by=By.XPATH, wait=30, requence=0.5):
    # 等待元素出现就去点击
    ele = WebDriverWait(n_driver, wait, requence).until(EC.visibility_of_element_located((by, locator)))
    return ele


def input_ele(n_driver, locator,inputstr ,by=By.XPATH, wait=30, requence=0.5):
    ele = WebDriverWait(n_driver, wait, requence).until(EC.visibility_of_element_located((by, locator)))
    time.sleep(0.25)
    ele.send_keys(inputstr)


def click_and_wait(n_driver, locator1 ,locator2,by=By.XPATH, wait=30, requence=0.5,t_sleep=0):
    count=3
    time.sleep(t_sleep)
    while count:
        WebDriverWait(n_driver, wait, requence).until(EC.visibility_of_element_located((by, locator1))).click()
        try:
            wait_elevisible_return(n_driver,locator2, wait=5)
            break
        except:
            count-=1
    if count==0:
        raise Exception("元素未出现")


def BSchat(driver,username,password):
    login = '//div[@class="unlogin Log-In"]'
    inputphone = '//input[@class="phoneNumber"]'  # 手机号
    phoneCode = '//input[@class="password"]'  # 手机验证码
    buttonnext = '//button[@class="justLogin"]'  # 下一步
    passwordLogin = '//p[@class="passwordLogin"]'
    quhao = '//div[@class="loginByPassword"]//li[@class="getPhone"]/div[1]'
    quhaoC = '//li[@class="bar-item bar-C"]'
    chinaquhao = '//li[@data-name="China"]'

    chatbox = '//textarea[@id="chatbox-message"]'
    chatsend = '//i[@class="iconfont icon-F_web_icon_chat_send icon-can-send-msg"]'
    chatsend1 = '//i[@class="iconfont icon-F_web_icon_chat_send"]'
    likesend = '//i[@class="iconfont icon-F_web_icon_like_solid"]'


    time.sleep(1)
    click_and_wait(driver,login,passwordLogin, t_sleep=3)
    # wait_elevisible_click(driver, login, t_sleep=3)
    wait_elevisible_click(driver, passwordLogin, t_sleep=3)
    wait_elevisible_click(driver, quhao)
    wait_elevisible_click(driver, quhaoC)
    wait_elevisible_click(driver, chinaquhao)
    input_ele(driver, inputphone, username )
    input_ele(driver, phoneCode, password)
    wait_elevisible_click(driver, buttonnext)
    # wait_elevisible_return(driver, islogin)
    tag=1
    while 1:
        putstr='男嘉宾'+username[-4:]+': %s'%tag
        # putstr = ''.join(random.sample(string.ascii_letters + string.digits, 30))
        input_ele(driver, chatbox, putstr)
        try:
            wait_elevisible_click(driver, chatsend, wait=3)
        except:
            wait_elevisible_click(driver, chatsend1, wait=3)
        time.sleep(0.5)
        wait_elevisible_click(driver, likesend)
        time.sleep(0.5)
        tag+=1



def chatStart(username,password):
    base_dir = os.getcwd()
    executable_path = base_dir + r"\chromedriver.exe"
    # from selenium.webdriver.chrome.options import Options
    with open('live.txt', 'r') as f:
        live = f.read()
    test_url = 'https://www.fazzaco.com/webinars/%s'%live
    from selenium.webdriver import Chrome, ChromeOptions

    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"

    opt = ChromeOptions()  # 创建Chrome参数对象
    # opt.headless = True  # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
    driver = Chrome(executable_path=executable_path,options=opt)  # 创建Chrome无界面对象
    driver.get(test_url)
    driver.maximize_window()
    BSchat(driver,username,password)



