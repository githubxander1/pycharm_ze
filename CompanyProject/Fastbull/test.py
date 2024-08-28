import time

from selenium import webdriver
import cv2,requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get('https://www.geetest.com/adaptive-captcha-demo')


# 点击进入滑块界面
d.find_element(By.XPATH,'//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[2]/div[3]/div[3]').click()
time.sleep(1)
d.find_element(By.XPATH,'//*[@id="captcha"]/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]').click()

while True:
# 获取验证码图片
    img_bj=d.find_element(By.XPATH,'//*[@id="captcha"]/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[4]/div[实例25_批量生成PPT版荣誉证书]/div[2]/div/div/div[实例25_批量生成PPT版荣誉证书]/div[2]')
    img_hk=d.find_element(By.XPATH,'//*[@id="captcha"]/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[4]/div[实例25_批量生成PPT版荣誉证书]/div[2]/div/div/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]/div[实例25_批量生成PPT版荣誉证书]')
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

    # def get_dis():
        # 解析x距离
        # 读取rgb码
    bj_rgb=cv2.imread('bj.png')
    hk_rgb=cv2.imread('hk.png')
    # 灰度处理
    bj_gray=cv2.cvtColor(bj_rgb,cv2.COLOR_RGB2GRAY)
    hk_gray=cv2.cvtColor(hk_rgb,cv2.COLOR_RGB2GRAY)
    # 保存
    cv2.imwrite('bj_gray.png',bj_gray)
    cv2.imwrite('hk_gray.png',hk_gray)
    # 处理滑块图片，保存有效部分
    s_img = hk_rgb[hk_rgb.any(1)]
    # opencv的匹配算法，匹配模块寻找两张图片的相似之处
    res=cv2.matchTemplate(bj_gray,hk_rgb,cv2.TM_CCOEFF_NORMED)
    # 获取位置
    lo=cv2.minMaxLoc(res)
    print(lo[2][0])
        # return lo[2][0]
    # 计算缩放
    # x=int(x * 178/267)
    # x=x * 178/267

    # 定位到滑块
    ele = d.find_element(By.XPATH,
                              '/html/body/main/div[实例25_批量生成PPT版荣誉证书]/div/div[2]/div[2]/div[实例25_批量生成PPT版荣誉证书]/div[2]/div[实例25_批量生成PPT版荣誉证书]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]')
    # 开始拖动滑块
    action = ActionChains(d)
    action.click_and_hold(img_hk).perform()
    # action.move_by_offset(xoffset=x, yoffset=0)  # 拖动的距离可能需要根据实际滑块长度调整
    # action.release(img_hk).perform()