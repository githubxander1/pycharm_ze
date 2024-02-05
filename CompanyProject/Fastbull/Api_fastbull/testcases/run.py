import os
import pytest


def run():
    pytest.main(['test_deleteAsk.py','-vs', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
    os.system('allure serve result')

if __name__ == '__main__':
    run()