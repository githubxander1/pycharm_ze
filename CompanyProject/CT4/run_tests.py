
# import pytest
#
# def run_tests():
#     test_directory = r'D:\1test\PycharmProject\pycharm_ze\CompanyProject\CT4'
#
#     # 获取目录中所有的测试文件
#     test_files = [f for f in os.listdir(test_directory) if f.endswith('_test.py') and f != 'run_tests.py']
#     print(test_files)
#
#     # 运行每个测试文件
#     for test_file in test_files:
#         file_path = os.path.join(test_directory, test_file)
#         command = ['pytest', file_path, '--html=report.html']
#         subprocess.run(command, check=True)
#
# if __name__ == '__main__':
#     run_tests()
import pytest

if __name__ == "__main__":
    pytest.main(["-s", "-v", "--html=report.html"])