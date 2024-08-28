import time

import uiautomator2 as u2

class BasePage:
    def __init__(self, device_url='127.0.0.实例25_批量生成PPT版荣誉证书:21503',package_name='com.bv.forexchat'):
        self.d = u2.connect(device_url)
        self.package_name = package_name
        self.d.implicitly_wait(10)

    def launch_app(self):
        self.d.app_start(self.package_name)

    def close_app(self):
        self.d.app_stop(self.package_name)

    def find_element(self, selector):
        element = None
        try:
            if 'xpath' in selector:
                element = self.d.xpath(selector['xpath'])
            elif 'description' in selector:
                element = self.d(description=selector['description'])
            elif 'resourceId' in selector:
                element = self.d(resourceId=selector['resourceId'])
            return element
        except Exception as e:
            # print(e)
            raise Exception(f"Element {selector} not found")

    def click(self, locator):
        ele = self.find_element(locator)
        ele.click()

    def input_text(self, locator, text):
        ele = self.find_element(locator)
        # ele.clear()
        ele.set_text(str(text))

    def swipe_left(self, selector):
        element = self.find_element(selector)
        bounds = element.info['bounds']
        start_x = bounds['left']
        end_x = bounds['right']
        y = (bounds['top'] + bounds['bottom']) / 2
        self.d.swipe(end_x, y, start_x, y)
    # 添加其他常用操作方法

    # ...
# if __name__ == '__main__':
#     BasePage().launch_app()
# 使用示例
# base_page = BasePage('127.0.0.实例25_批量生成PPT版荣誉证书:21503', 'com.bv.forexchat')
# base_page.launch_app()
# time.sleep(3)
# # 执行其他操作
# base_page.close_app()


