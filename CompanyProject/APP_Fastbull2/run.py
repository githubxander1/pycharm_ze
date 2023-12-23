import os
import time

import pytest

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    pytest.main([os.path.join(current_dir, 'testcases', 'test_home_search.py')])
    # 加3秒延迟时为了让用例能完整执行，并生成临时文件
    time.sleep(3)
    # 通过 os.system 向系统终端输入指令 allure generate 表示生成 html 报告，
    # ./allureTemps 表示用来生成html的JSON临时文件目录
    # ./reports 表示html文件生成目录
    # --clean 表示生成前清空之前的文件
    os.system("allure generate ./allureTemps -o ./reports --clean")

    # 将报告.html文件移动到reports目录下（如果还没有的话）
    if not os.path.exists('./reports/report.html'):
        os.rename('./report.html', './reports/report.html')
    else:
        print('警告：./report.html 文件不存在')