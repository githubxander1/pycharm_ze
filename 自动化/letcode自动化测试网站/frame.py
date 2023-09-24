from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

from selenium import webdriver
from msedge.selenium_tools import EdgeOptions


# options = webdriver.EdgeOptions()
# options.use_chromium = True
# options.add_argument("disable-blink-features=AutomationControlled")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31"
# )
# d = webdriver.Edge(options=options)
d = webdriver.Edge()
d.get('https://letcode.in/frame')
d.implicitly_wait(10)

#获取当前iframe的tag name，确定有几个iframe，
# 你所在的元素和获取到页面的iframe之间的关系，来进行iframe的切换。

for child_frame in d.find_elements(By.TAG_NAME,"iframe"):
    child_frame_id = child_frame.get_attribute("src")
    print(child_frame_id)

def list_frame(self, locator):
    for child_frame in self.d.find_elements(*locator):
        child_frame_id = child_frame.get_attribute("src")
        print(child_frame_id)


# 切换到主frame
def switch_body(self, locator, doc=''):
    logger.info('{0},body_frame切换到'.format(doc, locator))
    try:
        self.d.switch_to.parent_frame()
    except:
        logger.info('{0},body_frame切换到失败！！！'.format(doc, locator))
        raise

# 切换到不同的frame
# def switch_iframe(self, locator, doc=''):
#     logger.info('{0},frame切换到'.format(doc, locator))
#     try:
#         to_frame = self.get_element(locator)
#         self.driver.switch_to.frame(to_frame)
#     except:
#         logger.info('{0},frame切换到失败！！！'.format(doc, locator))
#             raise

#根据实际需求进行切换
    # 切换到不同的frame
# def switch_iframe(self, locator='', doc='', relation="child"):
#     logger.info('{0},frame切换到'.format(doc, locator))
#     try:
#         if relation == "parent":
#             self.driver.switch_to.default_content()
#         else:
#             to_frame = self.get_element(locator)
#             self.driver.switch_to.frame(to_frame)
#     except:
#         logger.info('{0},frame切换到失败！！！'.format(doc, locator))
#         raise

first_iframe = d.find_element(By.ID, 'firstFr')
d.switch_to.frame(first_iframe)

d.find_element(By.NAME, 'fname').send_keys('firstname')
d.find_element(By.NAME, 'lname').send_keys('lastname')
print('第一个frame操作执行完毕')

sleep(2)
print('开始跳转到内部frame')
inner_frame = d.find_element(By.CSS_SELECTOR, 'body > app-root > app-frame-content > div > div > div > iframe')
print('定位到了frame')
d.switch_to.frame(inner_frame)
print('已跳转')


d.find_element(By.NAME, 'email').send_keys('firstname@gmail.com')
print('输入邮箱完毕')

d.switch_to.parent_frame()
print('切换到第一个frame')
d.find_element(By.NAME, 'fname').send_keys('firstname_second')
print('第二次输入firstname完毕')
