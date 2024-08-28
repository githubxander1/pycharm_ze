# def get_element_slide_distance( slider_ele, background_ele, correct=0):
# """
# 根据传入滑块，和背景的节点，计算滑块的距离
# ​
# 该方法只能计算 滑块和背景图都是一张完整图片的场景，
# 如果背景图是通过多张小图拼接起来的背景图，
# 该方法不适用，请使用get_image_slide_distance这个方法
# :param slider_ele: 滑块图片的节点
# :type slider_ele: WebElement
# :param background_ele: 背景图的节点
# :type background_ele:WebElement
# :param correct:滑块缺口截图的修正值，默认为0,调试截图是否正确的情况下才会用
# :type: int
# :return: 背景图缺口位置的X轴坐标位置（缺口图片左边界位置）
# """
# # 获取验证码的图片
#     slider_url = slider_ele.get_attribute("src")
#     background_url = background_ele.get_attribute("src")
#     # 下载验证码背景图,滑动图片
#     slider = "slider.jpg"
#     background = "background.jpg"
#     onload_save_img(slider_url, slider)
#     onload_save_img(background_url, background)
#     # 读取进行色度图片，转换为numpy中的数组类型数据，
#     slider_pic = cv2.imread(slider, 0)
#     background_pic = cv2.imread(background, 0)
#     # 获取缺口图数组的形状 -- 缺口图的宽和高
#     width, height = slider_pic.shape[::-实例25_批量生成PPT版荣誉证书]
#     # 将处理之后的图片另存
#     slider01 = "slider01.jpg"
#     background_01 = "background01.jpg"
#     cv2.imwrite(background_01, background_pic)
#     cv2.imwrite(slider01, slider_pic)
#     # 读取另存的滑块图
#     slider_pic = cv2.imread(slider01)
#     # 进行色彩转换
#     slider_pic = cv2.cvtColor(slider_pic, cv2.COLOR_BGR2GRAY)
#     # 获取色差的绝对值
#     slider_pic = abs(255 - slider_pic)
#     # 保存图片
#     cv2.imwrite(slider01, slider_pic)
#     # 读取滑块
#     slider_pic = cv2.imread(slider01)
#     # 读取背景图
#     background_pic = cv2.imread(background_01)
#     # 比较两张图的重叠区域
#     result = cv2.matchTemplate(slider_pic, background_pic, cv2.TM_CCOEFF_NORMED)
#     # 获取图片的缺口位置
#     top, left = np.unravel_index(result.argmax(), result.shape)
#     # 背景图中的图片缺口坐标位置
#     print("当前滑块的缺口位置：", (left, top, left + width, top + height))
#     return left
#
# def slide_verification(self, driver, slide_element, distance):
# """
# 滑动滑块进行验证
# :param driver: driver对象
# :type driver:webdriver.Chrome
# :param slide_element: 滑块的元组
# :type slider_ele: WebElement
# :param distance: 滑动的距离
# :type: int
# :return:
# """
# # 获取滑动前页面的url地址
#     start_url = driver.current_url
#     print("需要滑动的距离为：", distance)
#     # 根据滑动距离生成滑动轨迹
#     locus = self.get_slide_locus(distance)
#     print("生成的滑动轨迹为:{}，轨迹的距离之和为{}".format(locus, distance))
#     # 按下鼠标左键
#     ActionChains(driver).click_and_hold(slide_element).perform()
#     time.sleep(0.5)
#     # 遍历轨迹进行滑动
#     for loc in locus:
#     time.sleep(0.01)
#     ActionChains(driver).move_by_offset(loc, random.randint(-5, 5)).perform()
#     ActionChains(driver).context_click(slide_element)
#     # 释放鼠标
#     ActionChains(driver).release(on_element=slide_element).perform()