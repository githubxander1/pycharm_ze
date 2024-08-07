import os
import subprocess


# main.py
import pytest

if __name__ == "__main__":
    pytest.main(["-s", "-v", "--html=report.html", "tests/"])



# if __name__ == "__main__":
    # 指定测试用例所在的文件夹
    # test_folder = "testcases"

    # 运行测试用例
    # run_tests('test_select_market')
