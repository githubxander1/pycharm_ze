import time

import uiautomator2 as u2


class BasePage:
    def __init__(self, device_url, package_name):
        device_url='127.0.0.1:21503'
        package_name='com.bv.forexchat'
        base_page.launch_app()
        self.d = u2.connect(device_url)
        self.package_name = package_name

    def launch_app(self):
        self.d.app_start(self.package_name)

    def close_app(self):
        self.d.app_stop(self.package_name)

    def find_element(self, locator):
        locator_dict = {locator[0]: locator[1]}
        return self.d(**locator_dict)

    def click(self, locator):
        ele = self.find_element(locator)
        ele.click()

    def input_text(self, locator, text):
        ele = self.find_element(locator)
        ele.clear_text()
        ele.set_text(text)

    # 添加其他常用操作方法

    # ...

# 使用示例
# base_page = BasePage('127.0.0.1:21503', 'com.bv.forexchat')
# base_page.launch_app()
# time.sleep(3)
# # 执行其他操作
# base_page.close_app()

# import uiautomator2 as u2
#
#
# class BaseTestClass:
#     def __init__(self):
#         self.d = u2.connect('127.0.0.1:21503')
#         self.package_name = 'com.bv.forexchat'
#
#     def launch_app(self):
#         self.d.app_start(self.package_name)
#
#     def close_app(self):
#         self.d.app_stop(self.package_name)
#
#     def find_element(self, selector):
#         return self.d(resourceId=selector)
#
#     def click_element(self, selector):
#         element = self.find_element(selector)
#         element.click()
#
#     def input_text(self, selector, text):
#         element = self.find_element(selector)
#         element.set_text(text)
#
#     def swipe_left(self, selector):
#         element = self.find_element(selector)
#         bounds = element.info['bounds']
#         start_x = bounds['left']
#         end_x = bounds['right']
#         y = (bounds['top'] + bounds['bottom']) / 2
#         self.d.swipe(end_x, y, start_x, y)