from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 配置Edge WebDriver
# edge_options.add_argument("disable-gpu")
d=webdriver.Edge()


d.get("http://axure.tostar.top:8000/CloudTrader/AISignal/#id=jhptou&p=%E4%BF%A1%E5%8F%B7%E5%88%97%E8%A1%A8_1")

sleep(3)
# 切换到Windows安全中心弹窗
alert = d.switch_to.alert

# 输入用户名和密码
alert.send_keys('xiaozehua')
alert.send_keys(Keys.TAB)  # 使用TAB键切换到下一个输入框
alert.send_keys('abc@2021')

# 点击确定按钮
alert.accept()
# alert.send_keys('\t')
