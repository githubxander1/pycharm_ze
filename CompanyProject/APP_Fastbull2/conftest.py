# from datetime import datetime
# from py.xml import html
# import pytest
# from selenium import webdriver
#
#
import time

# 函数收集测试结果
from datetime import datetime

from CompanyProject.APP_Fastbull2.base.basePage import d


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # print(terminalreporter.stats)
    print("total:", terminalreporter._numcollected)
    print('passed:', len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown']))
    print('failed:', len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown']))
    print('error:', len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown']))
    print('skipped:', len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown']))
    if terminalreporter._numcollected > 0:
        success_rate = len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100
        print('成功率：%.2f%%' % success_rate)
    else:
        print('没有执行任何测试用例')

    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times:', duration, 'seconds')
# def _capture_screenshot():
#     """
#     截图，并返回base64编码
#     """
#     # chrome_options = Options()
#     # chrome_options.add_argument('--headless')
#     # chrome_options.add_argument('--disable-gpu')
#     # browser = webdriver.Chrome(chrome_options=chrome_options)
#     browser = webdriver.Edge()
#     return browser.get_screenshot_as_base64()
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     # 检查描述文档是否存在，如果存在则设置为报告的description属性
#     description = getattr(item.function, '__doc__', None)
#     if description:
#         report.description = str(description)
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#                 # 检查描述文档是否存在，如果存在则设置为报告的description属性
#         # description = getattr(item.function, '__doc__', None)
#         # if description:
#         #     report.description = str(description)
#         report.extra = extra
#         # report.description = str(item.function.__doc__)
#         report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(实例25_批量生成PPT版荣誉证书, html.th('Description'))
#     cells.insert(2, html.th('Test_nodeid'))
#     # cells.insert(实例25_批量生成PPT版荣誉证书, html.th('Time', class_='sortable time', col='time'))
#     cells.pop(2)
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(实例25_批量生成PPT版荣誉证书, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     # cells.insert(实例25_批量生成PPT版荣誉证书, html.td(datetime.utcnow(), class_='col-time'))
#     cells.pop(2)
#
# #
# # def brower():
# #     global driver
# #     if driver is None:
# #         driver=webdriver.Edge()
# #     return driver
import os
import allure
import pytest
# from webdriver_helper import get_webdriver

# driver = None


# @pytest.fixture(scope='session', name="mydriver")
# def driver(request):
#     global driver
#     driver = get_webdriver()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
#     def end():
#         driver.quit()
#
#     request.addfinalizer(end)  # 终结函数
#     # 这里为什么不用yield呢因为yield不能return，addfinalizer这个功能可以实现饿yield功能一样
#     # 而且可以return参数传给后面的用例
#     return driver


# 用例失败后自动截图
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, file_basename,sc_name):
#     """
#     获取每个用例的钩子函数
#     :param item:
#     :param call:
#     :return:
#     """
#     outcome = yield
#     rep = outcome.get_result()
#     # 以下为实现异常截图的代码：
#     # rep.when可选参数有call、setup、teardown，
#     # call表示为用例执行环节、setup、teardown为环境初始化和清理环节
#     # 这里只针对用例执行且失败的用例进行异常截图
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s) " % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         item.name = item.name.encode("utf-8").decode("unicode-escape")
#
#         basename_without_extension = os.path.splitext(file_basename)[0]
#         file_without_prefixAndextension = basename_without_extension[5:]  # 去掉前面的text_
#         print(file_without_prefixAndextension)
#         if os.path.exists(f'./result_screenshots/{file_without_prefixAndextension}'):
#             pass
#         else:
#             os.makedirs(f'./result_screenshots/{file_without_prefixAndextension}')
#             os.path.join(f'./result_screenshots/{file_without_prefixAndextension}', '__init__.py')  # 创建__init__.py文件
#         timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#         filename = f'./result_screenshots/{file_without_prefixAndextension}/{sc_name}_{timestamp}.png'
#         time.sleep(4)
#         d.screenshot(filename)
#
#         # file_name = '{}.png'.format(str(round(time.time() * 1000)))
#         # path = os.path.join(PRPORE_SCREEN_DIR, file_name)
#         #
#         # driver.save_screenshot(path)
#
#         if hasattr(driver, "get_screenshot_as_png"):
#             with allure.step("添加失败截图"):
#                 # get_screenshot_as_png实现截图并生成二进制数据
#                 # allure.attach直接将截图二进制数据附加到allure报告中
#                 allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
                # logger.info("错误页面截图成功，图表保存的路径:{}".format(path))
# @pytest.mark.hookwrapper
# def _take_screenshot(file_basename,sc_name):
#     basename_without_extension = os.path.splitext(file_basename)[0]
#     file_without_prefixAndextension = basename_without_extension[5:]  # 去掉前面的text_
#     print(file_without_prefixAndextension)
#     if os.path.exists(f'./result_screenshots/{file_without_prefixAndextension}'):
#         pass
#     else:
#         os.makedirs(f'./result_screenshots/{file_without_prefixAndextension}')
#         os.path.join(f'./result_screenshots/{file_without_prefixAndextension}', '__init__.py')  # 创建__init__.py文件
#     timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#     filename = f'./result_screenshots/{file_without_prefixAndextension}/{sc_name}_{timestamp}.png'
#     time.sleep(4)
#     d.screenshot(filename)
#     return filename
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _take_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'οnclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

