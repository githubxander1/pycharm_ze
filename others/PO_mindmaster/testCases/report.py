# -*- coding: utf-8 -*-
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-vs','--ruturn 实例25_批量生成PPT版荣誉证书' '--alluredir=../allure-results', 'test_Login.py'])
    os.system('allure generate ../allure-results -o ../allure-results/report/html clean')
    # os.system('allure generate ../allure-results -o ./reports --clean open')
    # os.system(['allure', 'generate', '../allure-results', '-o', '../reports', '--clean'], check=True)
    # subprocess.run(['allure', 'generate', '../allure-results', '-o', '../reports', '--clean'], check=True)

    # 生成Allure报告：如果你已经安装了Allure   # CLI（通过npm    # install - g allure - commandline），你可以在命令行中运行以下命令来生成HTML报告：
    # os.system('allure generate allure-results --clean && allure open')
