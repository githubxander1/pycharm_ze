from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get('https://letcode.in/radio')

print('判断能否点击选中')
driver.find_element(By.ID,'yes').click()
print('点击yes')
# sleep(1)
driver.find_element(By.ID,'no').click()
print('点击no')


print('1判断按钮是否被选中')
# 定位所有radio button元素
# radio_buttons1 = driver.find_elements(By.XPATH,'//input[@type="radio"]')
# print(f'打印所有radio button元素：{radio_buttons}')

# 需要判断的radio button
one_radio = driver.find_element(By.ID,'one')
two_radio = driver.find_element(By.ID,'two')
one_radio.click()

if one_radio.is_selected():
    print(one_radio.get_attribute('name')+'按钮被选中')
    print('被选中的单选按钮文本是：'+one_radio.get_attribute('id'))
elif two_radio.is_selected():
    print('two按钮被选中')
    print('被选中的单选按钮文本是：'+two_radio.get_attribute('id'))
else:
    print('两个都没有被选中')


print('2判断哪个按钮被选中')
# 定位所有radio button元素
radio_buttons = driver.find_elements(By.XPATH,'//input[@type="radio"]')

# 选择需要的radio button
desired_radio = driver.find_element(By.ID,'notfoo')
# desired_radio.click()
# 遍历radio button元素
for desired_radio in radio_buttons:
    # 判断是否已经被选中
    if desired_radio.is_selected():
        # 取消选中
        print(desired_radio.get_attribute('id')+'按钮已被选中')
    else:
        print(desired_radio.get_attribute('id')+'按钮未被选中')

print('3判断按钮是否可点击')
disabled_button=driver.find_element(By.ID,'maybe')
if disabled_button.is_enabled():
    print('按钮可点击')
else:
    print('按钮不可点击')


print('4复选框状态判断')
checkbox = driver.find_element(By.XPATH,"/html/body/app-root/app-radio-check/section[1]/div/div/div[1]/div/div/div[6]/label[2]/input")
# checkbox = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-radio-check > section.section.has-background-white-ter > div > div > div.column.is-7-desktop.is-8-tablet > div > div > div:nth-child(6) > label.checkbox > input[type=checkbox]")
checkbox.click()
if checkbox.is_selected():
    print("复选框已被选中")
else:
    print("复选框未被选中")
