# coding=utf-8
import re
import requests
import time
from io import BytesIO

import cv2
import numpy as np
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CrackSlider():
    # 通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并破解滑动验证码

    def __init__(self):
        super(CrackSlider, self).__init__()
        self.opts = webdriver.EdgeOptions()
        self.opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.opts)
        # chrome_path = r"C:\Users\11248\AppData\Local\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Edge()

        self.url = 'https://dun.163.com/trial/jigsaw'
        # self.url = 'https://dun.163.com/trial/sense'
        # self.url = 'https://tradinglive-testwebpc.tostar.top/cn/login'
        self.wait = WebDriverWait(self.driver, 10)
        # self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]').click()
        # driver.find_element(By.XPATH,'(By.XPATH,"/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/span")').click()
        # anquan = self.wait.until(EC.presence_of_element_located((By.XPATH,
        #                                                     "/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/span")))
        # anquan.click()

        # 切换到安全验证弹窗的iframe
        slider_iframe = self.driver.find_element(By.XPATH,'/html/body/iframe[1]')
        self.driver.switch_to.frame(slider_iframe)

    def get_pic(self):
        # self.driver.get(self.url)
        # time.sleep(5)
        target_link = self.driver.find_element(By.CLASS_NAME, "yidun_bg-img").get_attribute('src')
        template_link = self.driver.find_element(By.CLASS_NAME, "yidun_jigsaw").get_attribute('src')

        target_img = Image.open(BytesIO(requests.get(target_link).content))
        template_img = Image.open(BytesIO(requests.get(template_link).content))
        target_img.save('target.jpg')
        template_img.save('template.png')

    def crack_slider(self, distance):
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'yidun_slider')))
        ActionChains(self.driver).click_and_hold(slider).perform()
        ActionChains(self.driver).move_by_offset(xoffset=distance, yoffset=0).perform()
        time.sleep(2)
        ActionChains(self.driver).release().perform()
        return 0


def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    r_channel, g_channel, b_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道

    img_new = cv2.merge((r_channel, g_channel, b_channel, alpha_channel))  # 融合通道
    return img_new


def handel_img(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)  # 转灰度图
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # 高斯模糊
    imgCanny = cv2.Canny(imgBlur, 60, 60)  # Canny算子边缘检测
    return imgCanny


def match(img_jpg_path, img_png_path):
    # 读取图像
    img_jpg = cv2.imread(img_jpg_path, cv2.IMREAD_UNCHANGED)
    img_png = cv2.imread(img_png_path, cv2.IMREAD_UNCHANGED)
    # 判断jpg图像是否已经为4通道
    if img_jpg.shape[2] == 3:
        img_jpg = add_alpha_channel(img_jpg)
    img = handel_img(img_jpg)
    small_img = handel_img(img_png)
    res_TM_CCOEFF_NORMED = cv2.matchTemplate(img, small_img, 3)
    value = cv2.minMaxLoc(res_TM_CCOEFF_NORMED)
    value = value[3][0]  # 获取到移动距离
    return value


# 1. 打开chromedriver，试试下载图片
cs = CrackSlider()
cs.get_pic()
# 2. 对比图片，计算距离
img_jpg_path = 'target.jpg'  # 读者可自行修改文件路径
img_png_path = 'template.png'  # 读者可自行修改文件路径
distance = match(img_jpg_path, img_png_path)
distance = distance / 480 * 345 + 12
# 3. 移动
cs.crack_slider(distance)

