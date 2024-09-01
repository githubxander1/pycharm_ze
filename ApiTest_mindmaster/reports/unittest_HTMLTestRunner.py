import unittest
import os
from HTMLTestRunner import HTMLTestRunner

report_dir = "reports/"
report_file = report_dir + "mindmaster_html_report.html"

# 判断reports目录是否存在，如果不存在就创建目录
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

with open(report_file, "wb") as fl:
    module_path = "../"
    discover = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="flashing_icon*.py")
    runner = HTMLTestRunner(title='测试标题', description='描述本次测试的大概内容', stream=fl)
    runner.run(discover)