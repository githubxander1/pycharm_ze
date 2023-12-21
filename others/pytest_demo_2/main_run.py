import os
import pytest


def run():
    pytest.main(['-v', './case/test_Tree.py',
                 '--alluredir', './result', '--clean-alluredir'])
    os.system('allure serve result')
    # os.system('allure generate ./result/ -o ./report_allure/ --clean')

if __name__ == '__main__':
    run()