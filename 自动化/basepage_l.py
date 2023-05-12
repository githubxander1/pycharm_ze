from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common import dir_config
from global_variable.check import *
from common import logger
import logging
import datetime
import time
import random

# from functools import wraps
#
# def Singleton(cls):
#     _instance = {}
#
#     @wraps(cls)
#     def _singlenton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#         return _instance[cls]
#
#     return _singlenton
#
# @Singleton
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_eleVisible(self, locator, by=By.XPATH, model='model', wait=30, requence=0.5):
        # 判断等待元素出现
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait, requence).until(EC.visibility_of_element_located((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}页面等待元素可见：{1},起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
            return True
        except:
            logging.exception("等待元素：{}可见异常".format(locator))
            self._save_screenShot(model)
            raise

    def wait_eleVisible_return(self, locator, by=By.XPATH, model='model', wait=30, requence=0.5):
        # 判断等待元素出现后并返回
        try:
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver, wait, requence).until(EC.visibility_of_element_located((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}页面等待元素可见：{1},起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
            return ele
        except:
            logging.exception("等待元素：{}可见并返回异常".format(locator))
            self._save_screenShot(model)
            raise

    def wait_elevisible_click(self, locator, by=By.XPATH, model='model', wait=10, requence=0.5):
        # 等待元素出现就去点击
        try:
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver, wait, requence).until(EC.visibility_of_element_located((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}页面等待元素可见：{1},起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
            ele.click()
            logging.info("等待元素：{}出现之后点击成功了".format(locator))
        except:
            logging.exception("等待元素：{}可见异常".format(locator))
            self._save_screenShot(model)
            raise

    def wait_elevisible_input(self, locator, testvalue, by=By.XPATH, model='model', wait=30, requence=0.5):
        # 等待元素出现就去输入值
        try:
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver, wait, requence).until(EC.visibility_of_element_located((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}页面等待元素可见：{1},起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
            ele.send_keys(testvalue)
            logging.info("等待元素出现输入：{0}成功".format(testvalue))
        except:
            logging.exception("等待元素{}可见输入异常".format(locator))
            self._save_screenShot(model)
            raise

    def wait_elePrences(self, locator, by=By.XPATH, model='model', wait=30, requence=0.5):
        # 判断元素是否存在
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("等待元素存在：{0},起始时间：{1},等待时长：{2}".format(locator, start, wait_times))
        except:
            logging.exception("等待元素:{}存在异常".format(locator))
            self._save_screenShot(model)
            raise

    def wait_elePrences_return(self, locator, by=By.XPATH, model='model', wait=30, requence=0.5):
        # 判断元素是否存在 并返回
        try:
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("等待元素存在：{0},起始时间：{1},等待时长：{2}".format(locator, start, wait_times))
            return ele
        except:
            logging.exception("等待元素:{}存在异常".format(locator))
            self._save_screenShot(model)
            raise

    def wait_ele_clickable(self, locator, by=By.XPATH, model='model', wait=30, requence=0.5,index=None):
        #判断元素是否可点击,可以点击，就去点击
        try:
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver, wait, requence).until(EC.element_to_be_clickable((by, locator)))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("等待元素存在：{0},起始时间：{1},等待时长：{2}".format(locator, start, wait_times))
            ele[index].click()
        except:
            logging.exception("等待元素：{}存在异常".format(locator))
            self._save_screenShot(model)
            raise

    def find_element(self, locator, by=By.XPATH, model='model'):
        logging.info("开始查找元素：{0}={1}".format(by, locator))
        try:
            return self.driver.find_element(by, locator)
        except:
            logging.exception("查找元素：{}失败。".format(locator))
            self._save_screenShot(model)
            raise

    def find_elements(self, locator, by=By.XPATH, model='model'):
        logging.info("开始查找符合表达式的所有元素：{0}={1}".format(by, locator))
        try:
            return self.driver.find_elements(by, locator)
        except:
            logging.exception("查找多个元素：{}失败。".format(locator))
            self._save_screenShot(model)
            raise

    def click_element(self, locator, by=By.XPATH, model='model', index=None):
        '''
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
           index=None表示查找一个元素。
           index=-1 表示查找多个元素，并在多个元素中随机选一个；
           index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:无
        '''
        logging.info("{0}页面下执行点击操作！".format(model))
        ele = self._get_element(locator, by, model, index)
        try:
            ele.click()
        except:
            logging.exception("{0}页面{1}元素执行点击操作失败。".format(model, locator))
            self._save_screenShot(model)
            raise

    # 元素的输入操作
    def input_text(self, value, locator, by=By.XPATH, model='model', index=None):
        """
        :param value: 要输入的文本值
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:无
        """
        ele = self._get_element(locator, by, model, index)
        try:
            ele.send_keys(value)
        except:
            logging.exception("{0}下的元素:{1}执行输入操作失败。".format(model,locator))
            self._save_screenShot(model)
            raise

    # 获取元素的属性值。
    def get_element_attribube(self, attr_name, locator, by=By.XPATH, model='model', index=None):
        """
        :param attr_name: 元素的属性名称
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:元素的属性值。
        """
        logging.info("{0}：获取元素{1}={2} 的属性值：{3}。".format(model, by, locator, attr_name))
        ele = self._get_element(locator, by, model, index)
        try:
            return ele.get_attribute(attr_name)
        except:
            logging.exception("获取元素:{0}的属性：{1}  失败。".format(locator,attr_name))
            self._save_screenShot(model)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, by=By.XPATH, model='model', index=None):
        """
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
          index=None表示查找一个元素。
          index=-1 表示查找多个元素，并在多个元素中随机选一个；
          index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:元素的文本内容。
        """
        logging.info("{0}：获取元素{1}={2} 的文本内容。".format(model, by, locator))
        ele = self._get_element(locator, by, model, index)
        try:
            return ele.text
        except:
            logging.exception("获取元素:{}文本失败。".format(locator))
            self._save_screenShot(model)
            raise

    # 元素滚动操作
    def focus(self, locator, by=By.XPATH, model='model', index=None):
        """
        滚动到指定元素
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return: 无
        # """
        logging.info("{0}：滚动元素{1}={2} 到可见区域".format(model, by, locator))
        ele = self._get_element(locator, by, model, index)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        except:
            logging.exception("滚动失败")
            self._save_screenShot(model)
            raise

    def focus_bottom(self, locator, by=By.XPATH, model='model', index=None):
        """
        滚动到底部
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return: 无
        """
        logging.info("{0}：滚动元素{1}={2} 到可见区域".format(model, by, locator))
        ele = self._get_element(locator, by, model, index)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
        except:
            logging.exception("滚动失败")
            self._save_screenShot(model)
            raise

    def focus_top(self, top, model='model'):
        """
        滚动指定距离
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
              index=None表示查找一个元素。
              index=-1 表示查找多个元素，并在多个元素中随机选一个；
              index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return: 无
        """
        js = "var q=document.documentElement.scrollTop={}".format(top)
        try:
            self.driver.execute_script(js)
        except:
            logging.exception("滚动失败")
            self._save_screenShot(model)
            raise


    def _save_screenShot(self, model_name="model"):
        # 根据功能和时间点生成截图
        # 文件格式 ：功能名称_年月日-时分秒.png
        file_path = dir_config.screenshot_dir + "/{0}_{1}.png".format(model_name, time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                                 time.localtime()))
        # driver方法：self.driver.save_screenshot()
        self.driver.save_screenshot(file_path)
        logging.info("截图成功,路径为：{0}".format(file_path))

    # 确定要操作的元素 - 查找多个和查找单个。确定元素操作对象。
    def _get_element(self, locator, by, model="model", index=None):
        # index为None表示查找单个元素。不为None表示查找多个元素，并在多个元素中选一个。
        if index is not None:
            # 在查找到多个元素的基础之上，选择其中的一个。
            return self._select_ele_from_elements(locator, by, model, index)
        else:
            return self.find_element(locator, by, model)

    # 在查找到的多个元素中，选择一个元素。
    def _select_ele_from_elements(self, locator, by, model="model", index=-1):
        """
        :param index: -1 表示随机选；0及0以上的值表示按下标选值。
        :return:返回选中的元素
        """
        import random
        eles = self.find_elements(locator, by, model)
        if index == -1 or index < 0:
            pos = random.randint(0, len(eles) - 1)
            return eles[pos]
        else:
            return eles[index]

    def get_text(self, locator, by=By.XPATH, model='model', index=None):
        """
        :param locator:元素定位的表达式
        :param by:元素定位的类型
        :param model:模块或者用例名称。主要用在截图文件命名中，方便查找和定位。
        :param index: 是否要在多个元素中选择一个元素来操作。应用于查找多个元素的基础。
          index=None表示查找一个元素。
          index=-1 表示查找多个元素，并在多个元素中随机选一个；
          index > -1 表示查找多个元素，并且根据index的值取对应下标的元素。
        :return:元素的文本内容。
        """
        # logging.info("{0}：获取元素{1}={2} 的文本内容。".format(model,by,locator))
        ele = self._get_element(locator, by, model, index)
        try:
            return ele.text
        except:
            # logging.exception("获取元素文本失败。")
            self._save_screenShot(model)
            raise

    def get_pagesource(self, model='model'):
        # 获取页面的所有元素 xml格式的
        try:
            time.sleep(2)
            pagesource = self.driver.page_source
            return pagesource
        except:
            self._save_screenShot(model)
            logging.exception("获取{0}页面的元素失败。".format(model))

    def switch_handles(self, i=-1):

        model = "切换到新打开的窗口"
        time.sleep(1)

        try:
            logging.info(model)
            self.driver.switch_to.window(self.driver.window_handles[i])
        except:
            logging.info("窗口切换切换失败")

    def drag_to_bottom(self):

        model = "拖动到底部"
        time.sleep(1)
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)
        time.sleep(1)

    def check_text(self, locator, checktext, by=By.XPATH, model=None, index=0):
        text = self.get_text(locator, by=by, model=model, index=index)
        try:
            assert checktext in text
            logging.info("检查字段:{}正确".format(checktext))
            return check_results["success"]
        except:
            logging.error("检查字段:{0}错误,实际内容为:{1}".format(checktext, text))
            return check_results["fail"]

    def check_click_skip(self, local1, checktext, by=By.XPATH, model=None, index=0):
        self.click_element(local1, by=by, model=model, index=index)
        self.switch_handles()
        time.sleep(1)
        text = self.get_pagesource()
        try:
            assert checktext in text
            self.driver.close()
            self.switch_handles()
            logging.info("检查字段:{}正确".format(checktext))
            return check_results["success"]
        except:
            logging.error("检查字段:{0}错误,实际内容为:{1}".format(checktext, text))
            return check_results["fail"]


    def is_not_visible(self,locator, wait=10):
        try:
            WebDriverWait(self.driver, wait).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    def is_visible(self,locator, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except:
            return False

    def scrollIntoClick(self,scrollelement,offset=0):
        scrollist = self.wait_eleVisible_return(scrollelement)
        # ActionChains(self.driver).move_to_element(scrollist).perform()
        child_elements = scrollist.find_elements_by_xpath('.//*')
        if len(child_elements)!=0:
            randomint = random.randint(0, len(child_elements)-1)
            self.driver.execute_script("arguments[0].scrollIntoView(false);", child_elements[randomint])
            time.sleep(1)
            if offset!=0:
                # js = "document.documentElement.scrollTop=%s"%(str(offset))
                # self.driver.execute_script(js)

                js = "var q=document.body.scrollTop=%s"%(str(offset))
                self.driver.execute_script(js)
                time.sleep(1)

            # self.driver.navigate().refresh();
            if randomint==0:
                child_elements[0].click()
            else:
                for i in range(randomint+1):
                    try:
                        child_elements[randomint - i].click()
                        break
                    except:
                        pass
            time.sleep(1)