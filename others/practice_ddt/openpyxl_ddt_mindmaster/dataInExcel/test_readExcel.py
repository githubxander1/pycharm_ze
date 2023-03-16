# https://blog.csdn.net/baidu_41615818/article/details/120241397
import unittest
import requests
# 步骤1
from ddt import ddt, data, unpack, file_data
from com_getExcelData import get_excel_data

# 步骤2
@ddt  # 表示当前类要进行数据驱动测试
class Demo(unittest.TestCase):
    # 字典外加列表：因为unpack后是列表
    # @data()里面的是测试数据
    # @data([第一组数据]，[第二组数据])，有几组数据就执行几次测试用例
    # 步骤3
    @data(*get_excel_data())
    # 将一组数据（列表，元组）拆分成单个元素，然后一一对应传递给形式参数。只拆分一次。
    # 缺少@unpack的话，如此案例中，每组列表数据包含有入参和预期结果（多个值），不拆分这两个，
    # 会将它们全部传递给第一个形参，即value，进行传递（默认以逗号作为传递标准）。不符合要求，且会报错。
    # 步骤4
    # @unpack
    # 要进行数据驱动，我们就要为测试用例定义形式参数，形参的个数要与每组测试数据中的元素个数一致。
    # 执行测试的时候，测试数据会自动传递给对应的形式参数
    # 数据的传递，方法中传参，定义形式参数。变量的个数取决于每组数据里元素的个数，有2个值，就定义2个形参
    def test_01(self, value):  # 步骤5
        url = 'https://userapi.edrawsoft.cn/api/user/login'
        re = requests.post(url=url, data=value)  # 步骤6
        print(re)
        # result = pre in re.json()
        # print(result)


if __name__ == '__main__':
    unittest.main()
