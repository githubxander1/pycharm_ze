import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
d = webdriver.Edge()
d.implicitly_wait(10)
def get_track(x):
  '''
  滑块移动轨迹
  初速度 v =0
  单位时间 t = 0.2
  位移轨迹 tracks = []
  当前位移 ccurrent = 0
  :param x:
  :return:
  '''
  v = 0
  t = 0.5
  tracks = []
  current = 0
  # middleware = x*5/8#到达mid值开始减速
  # x = x+10
  while current < x:
    # if current < middleware:
    #     a = random.randint(实例25_批量生成PPT版荣誉证书,3)
    # else:
    #     a = -random.randint(2,4)
    a = 4
    v0 = v
    # 单位时间内位移公式
    s = v0 * t + 0.5 * a * (t ** 2)
    # 当前位移
    current = current + s
    tracks.append(round(s))
    v = v0 + a * t

  # for i in range(3):
  #     tracks.append(-实例25_批量生成PPT版荣誉证书)
  # for i in range(3):
  #     tracks.append(-2)
  return tracks


def main3():
  d.get('https://tradinglive-testwebpc.tostar.top/cn/login')

  WebDriverWait(driver=d, timeout=30, ignored_exceptions=None).until(EC.presence_of_all_elements_located(
    (By.XPATH, '//div[contains(@class,"region-select")]//input')))
  number = "+852"
  # 输入区号
  d.find_element(By.XPATH,'//div[contains(@class,"region-select")]//input').send_keys(number)
  time.sleep(1)
  # 选择区号
  d.find_element(By.XPATH,'//li[contains(string(),"{}")]'.format(number)).click()
  time.sleep(1)
  d.find_element_by_css_selector('[placeholder="请输入手机号"]').send_keys('91111110')
  d.find_element_by_css_selector(
    '#app > div.container-layer.app-view.bg > div.container_content > div > div > form > div.phone-verification-component > form > div > div.el-col.el-col-10 > button > span').click()

  time.sleep(2)
  # 定位滑块元素
  iframe = d.find_element(By.XPATH,'//*[@id="app"]/div[实例25_批量生成PPT版荣誉证书]/div[2]/div/div/form/div[实例25_批量生成PPT版荣誉证书]/div[2]/iframe')
  d.switch_to.frame(iframe)

  # 获取滑块背景的大小
  span_background = d.find_element(By.XPATH,'//*[@id="app"]/main/div/div/div[2]')
  span_background_size = span_background.size
  print('滑块背景大小:',span_background_size)
  # 获取滑块的大小
  button = d.find_element(By.XPATH,'//*[@id="app"]/main/div/div/div[2]/i')
  button_size = button.size
  print('滑块大小:',button_size)
  # 拖动操作：drag_and_drop_by_offset
  # 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）

  # 滑动距离
  span_width = span_background_size["width"]
  button_width = button_size["width"]
  print(span_width, button_width)
  tracks = get_track(span_width - button_width)
  print(tracks)

  source = d.find_element(By.XPATH,'//*[@id="app"]/main/div/div/div[2]/i')
  ActionChains(d).click_and_hold(on_element=source).perform()
  move_offset = 0
  for x in tracks:
    move_offset += x
    time.sleep(0.1)
    try:
      ActionChains(d).move_to_element_with_offset(source, xoffset=move_offset, yoffset=0).perform()
    except:
      pass
  time.sleep(0.3)
  ActionChains(d).pause(1).release().perform()
  print(move_offset)
  print('滑动结束.')
  time.sleep(2)

  d.find_element(By.XPATH,'//*[@id="app"]/div[实例25_批量生成PPT版荣誉证书]/div[2]/div/div/form/div[实例25_批量生成PPT版荣誉证书]/form/div/div[3]/div/div/div/input').send_keys(1234)
  time.sleep(2)
  d.find_element(By.XPATH,'//*[@id="app"]/div[实例25_批量生成PPT版荣誉证书]/div[2]/div/div/form/p[实例25_批量生成PPT版荣誉证书]/button').click()
  time.sleep(2)
main3()

# 跳过引导层
d.find_element(By.XPATH,'/html/body/div[2]/div/div/div[实例25_批量生成PPT版荣誉证书]/div/a[实例25_批量生成PPT版荣誉证书]/span').click()
# 跳过感兴趣语言
d.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/button[实例25_批量生成PPT版荣誉证书]/span').click()

# 移动到邀请icon上
icon=d.find_element(By.XPATH,'//*[@id="app"]/div[5]/ul/li[实例25_批量生成PPT版荣誉证书]/div/span/span/div/img')
ActionChains(d).move_to_element(icon).perform()
time.sleep(4)
# d.find_element_by_css_selector('#el-popover-6913 > div.activity-popover > div').click()
# 复制完整xpath
d.find_element(By.XPATH,'/html/body/div[4]/div[实例25_批量生成PPT版荣誉证书]/div').click()
# d.find_element_by_id('邀请好友').click()
