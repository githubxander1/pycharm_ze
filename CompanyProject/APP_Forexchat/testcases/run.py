import os
import time

import pytest

if __name__ == '__main__':
    pytest.main(['test_home_search.py', '-vs', '--alluredir=./allureTemps' ])
    # 加3秒延迟时为了让用例能完整执行，并生成临时文件
    time.sleep(3)
    # 通过 os.system 向系统终端输入指令 allure generate 表示生成 html 报告，
    # ./allureTemps 表示用来生成html的JSON临时文件目录
    # ./reports 表示html文件生成目录
    # --clean 表示生成前清空之前的文件
    os.system("allure generate ./allureTemps -o ./reports --clean")