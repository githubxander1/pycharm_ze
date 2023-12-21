from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver

import requests
import time
import cv2


#下载图片
def download_img(url,filename):
    r = requests.get(url)
    with open( filename + '.png', 'wb') as f:
        # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入yanzheng.png中
        f.write(r.content)
        print(filename + '下载完成')

def get_image():
    #为什么这里要定义全局变量？因为driver在函数内，函数运行完毕就会关闭，
    #相应的网页也会被关闭，这就是网上很多问为什么网页会自动关闭的原因。
    global driver
    driver= webdriver.Chrome() #获取浏览器对象
    driver.get("https://mail.qq.com/") #加载百度首页
    #窗口最大化操作，如果窗口过小，会导致后续拖动滑块时出现视野丢失的问题
    driver.maximize_window()
    time.sleep(2) #睡眠两秒

    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div/div[1]/div[2]').click()

    time.sleep(1)

    driver.switch_to.frame('login_frame')
    # driver.find_element(By.XPATH,'//*[@id="switcher_plogin"]').click()

    #输入账号密码
    input=driver.find_element(By.XPATH,'//*[@id="u"]')#定位QQ账号框
    time.sleep(1)
    input.send_keys("2695418206@qq.com") #搜索框输入内容

    input=driver.find_element(By.XPATH,'//*[@id="p"]')#定位QQ密码框
    input.send_keys("txj9713@xl") #搜索框输入内容
    print('账号密码输入完成。')
    #这里停顿一下，不然不会显示滑动验证，应该是检测自动化工具的手段。（反爬）
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="login_button"]').click()

    #注意我们这里又需要跳到验证码的子框（又一个嵌套）
    time.sleep(1)
    driver.switch_to.frame('tcaptcha_iframe')
    #webdriver的定位方法和浏览器xpath不一样，不能直接定位到标签的属性.
    #需要首先定位到webelement，之后get到属性!!!!!!!
    bk = driver.find_element(By.XPATH,'//*[@id="slideBg"]').get_attribute('src')
    print(bk)
    #获取背景和滑块地址，下载到本地。
    key = driver.find_element(By.XPATH,'//*[@id="slideBlock"]').get_attribute('src')
    print(bk)

    download_img(bk,filename= 'bk')
    download_img(key,filename= 'key')

    #锁定滑块
    slider = driver.find_element(By.XPATH,'//*[@id="tcaptcha_drag_thumb"]')
    #获取应滑动距离
    dis = get_distance()
    print(dis)

    #滑块部分，没有问题，已完成。
    newact =  ActionChains(driver)
    newact.click_and_hold(slider).perform()

    newact.move_by_offset(xoffset=dis-20,yoffset=0).perform()
    time.sleep(0.5)
    newact.release().perform()

#处理得到滑块应移动的距离。
def get_distance():
    path = 'bk.png'
    img = cv2.imread(path)

    path = 'key.png'
    img2 = cv2.imread(path)

    imgContour = img.copy()
    print('img.shape:', img.shape)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgCanny = cv2.Canny(imgBlur, 400, 500)

    imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    imgBlur2 = cv2.GaussianBlur(imgGray2, (3, 3), 1)
    imgCanny2 = cv2.Canny(imgBlur2, 400, 500)

    cv2.imshow("O", imgCanny)

    # 匹配拼图
    result = cv2.matchTemplate(imgCanny, imgCanny2, cv2.TM_CCOEFF_NORMED)

    # 归一化
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print('min_loc:', min_loc)
    print('max_loc:', max_loc)

    # 匹配后结果画圈
    cv2.rectangle(imgContour, max_loc, (max_loc[0] + 135, max_loc[1] + 135), (0, 0, 255), 2)

    # 原图为680*390 在浏览器resize为280*161，这里我们只用到宽。所以需要进行同比例缩放。
    res = min_loc[0] / (680 / 280)

    cv2.imshow("Canny Image", imgContour)
    #这里不可以用0，因为图片窗口会一直显示，程序卡住无法return出距离给滑块功能使用。
    cv2.waitKey(100)
    print('应滑动距离获取成功。')
    return res

if __name__ == '__main__':
    get_image()