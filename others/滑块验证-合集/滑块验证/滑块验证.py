from selenium import webdriver
import requests
import time
import cv2
import numpy as np
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://dun.163.com/trial/sense')

# 点击进入滑块界面
driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]').click()
time.sleep(1)
# 点击完成验证
driver.find_element(By.XPATH,
    '/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/span').click()
time.sleep(3)

while True:
    # 获取两张图片
    url_s = driver.find_element(By.CLASS_NAME,'yidun_jigsaw').get_attribute('src')
    url_b = driver.find_element(By.CLASS_NAME,'yidun_bg-img').get_attribute('src')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
    }
    res_s = requests.get(url_s, headers=headers)
    data_s = res_s.content
    res_b = requests.get(url_b, headers=headers)
    data_b = res_b.content
    # 保存图片
    with open('../CompanyProject/test/pic_s.png', 'wb') as f:
        f.write(data_s)
    with open('../CompanyProject/test/pic_b.png', 'wb') as f:
        f.write(data_b)

    # 使用opencv读取两张图片
    simg = cv2.imread('pic_s.png')
    bimg = cv2.imread('pic_b.png')

    # 灰度处理，降低偏差
    s_img = cv2.cvtColor(simg, cv2.COLOR_BGR2GRAY)
    b_img = cv2.cvtColor(bimg, cv2.COLOR_BGR2GRAY)

    # 保存两张灰度处理的图片
    cv2.imwrite('hui_simg.png', s_img)
    cv2.imwrite('hui_bimg.png', b_img)

    # 处理滑块图片，保存有效部分
    s_img = s_img[s_img.any(1)]

    # opencv的匹配算法，匹配模块寻找两张图片的相似之处
    result = cv2.matchTemplate(b_img, s_img, cv2.TM_CCOEFF_NORMED)
    print('result', result)

    # 获取坐标
    # 获取最大索引
    index_max = np.argmax(result)
    # 获取到坐标
    y, x = np.unravel_index(index_max, result.shape)
    print("y:", y, "x:", x)

    # 定位到滑块
    ele = driver.find_element(By.XPATH,
        '/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]')

    # 实例化对象
    action = ActionChains(driver)
    # 拖动滑块
    time.sleep(1)
    action.drag_and_drop_by_offset(ele, xoffset=x, yoffset=0).perform()
    time.sleep(1)
    # 定位到验证成功
    time.sleep(1)
    text = driver.find_element(By.XPATH,
        '/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]/span[2]').text
    if text == "验证成功":
        break