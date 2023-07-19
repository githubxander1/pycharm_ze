import time

import uiautomator2 as u2

class BasePage:
    def __init__(self, device_url, package_name):
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
base_page = BasePage('127.0.0.1:21503', 'com.bv.forexchat')
base_page.launch_app()
# time.sleep(3)
# # 执行其他操作
# base_page.close_app()