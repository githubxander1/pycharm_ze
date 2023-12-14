from time import sleep

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 配置Edge WebDriver
# edge_options.add_argument("disable-gpu")
d=webdriver.Edge()


d.get("http://axure.tostar.top:8000/CloudTrader/AISignal/#id=jhptou&p=%E4%BF%A1%E5%8F%B7%E5%88%97%E8%A1%A8_1")

sleep(3)
try:
    WebDriverWait(d,10).until(EC.alert_is_present())
    alert = d.switch_to.alert
    print(alert.text)
except:
    print('没有找到弹窗')
# 切换到Windows安全中心弹窗
# alert=Alert(d)

# # 输入用户名和密码
# alert.send_keys('xiaozehua')
# alert.send_keys(Keys.TAB)  # 使用TAB键切换到下一个输入框
# alert.send_keys('abc@2021')
# alert.dismiss()
# # 点击确定按钮
# alert.accept()
# alert.send_keys('\t')
