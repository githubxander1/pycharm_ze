# -*- coding:utf-8 -*-
import unittest, os
from commen import HTMLTestRunner
from interface.login import login
from commen.headle_token import *

current_path = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(current_path, "case")

report_path = os.path.join(current_path, "report")
report = os.path.join(report_path, "report.html")


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern='ztest*.py')
    print(discover)
    return discover


def run_case_report():
    fb = open(report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title="xx项目测试报告",
        description="xx项目的测试报告"
    )
    runner.run(all_case())
    fb.close()


if __name__ == '__main__':
    # 调用登录获取token
    token = login("host", "登录的账号", "密码")
    # 把token写入 sina.yaml 文件
    write_yaml(token)
    # 执行用例的时候会读取 sina.yaml 中的token，case文件下 test_user_info.py 的
    run_case_report()


