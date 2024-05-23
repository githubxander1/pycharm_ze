from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

d=webdriver.Edge()
d.get('https://letcode.in/buttons')
d.implicitly_wait(10)

# Get the X & Y co-ordinates
button=d.find_element_by_id('position')
x=button.location['x']
y=button.location['y']
print(f'按钮的x轴位置：{x}')
print(f'按钮的y轴位置：{y}')

# Find the color of the button
color=d.find_element_by_id('color').value_of_css_property('background-color')
print(f'按钮的颜色：{color}')


# Find the height & width of the button
size=d.find_element_by_id('property').size
print(f'按钮的高度：{size["height"]}')
print(f'按钮的宽度：{size["width"]}')

# Confirm button is disabled
isdisabled=d.find_element_by_id('isDisabled')
if isdisabled.is_enabled():
    print('按钮是可用的')
else:
    print('按钮是禁用的')

# Click and Hold Button
buttonid=d.find_element_by_css_selector('#isDisabled > div > h2')
# 点击并按住
actions=ActionChains(d)
actions.click_and_hold(buttonid).perform()
# 释放按钮
actions.release().perform()

# sleep(5)
# d.close()
