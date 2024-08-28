# from datetime import datetime
# from py.xml import html
# import pytest
# from selenium import webdriver
#
#
import time

# 函数收集测试结果
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # print(terminalreporter.stats)
    print("total:", terminalreporter._numcollected)
    print('passed:', len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown']))
    print('failed:', len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown']))
    print('error:', len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown']))
    print('skipped:', len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown']))
    print('成功率：%.2f' % (len(terminalreporter.stats.get('passed', []))/terminalreporter._numcollected*100)+'%')

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
