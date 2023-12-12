from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_runtest_makereport(item):
    """
    This function is called by pytest to create a report for each test.
    测试失败时，添加skip标记，自动截图展示到html报告中
    """
    pytest_html=item.config.pluginmanager.getplugin('html')
    outcome=yield
    report=outcome.get_result()
    extra=getattr(report, 'extra', [])
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html='<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:304px;height:228px;" ' \
                     'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot():
    """
    截图，并返回base64编码
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser.get_screenshot_as_base64()

def brower():
    global driver
    if driver is None:
        driver=webdriver.Edge()
    return driver
