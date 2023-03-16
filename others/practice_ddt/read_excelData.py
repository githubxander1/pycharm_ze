import unittest

from ddt import ddt,data,unpack,file_data

from practice_ddt.read_excel import excelData


@ddt
class singTest(unittest.TestCase):
    excel = excelData()
    testdata=excel.get_all_row()

    @data(*testdata)
    def test_sign(self,datas):
        # 由于从excel中读取到的数据为列表形式，所以采用下标来提取各参数
        ID = datas[0]
        model = datas[1]
        title = datas[2]
        method = datas[3]
        url = datas[4]
        username = datas[5]
        pwd = datas[6]
        cpwd = datas[7]
        check = datas[8]
        body = {
            "username": username,
            "pwd": pwd,
            "cpwd": cpwd
        }
        self.sign_test(ID, model, title, url, method, body, check)

    def sign_test(self, ID, model, title, url, method, body, check):
        print("用例ID:", ID)
        print("模块:", model)
        print("用例标题:", title)
        response = requests.request(url=url, method=method, data=body).text
        try:
            # 通过断言，比较实际结果是否与预期结果一致
            # 由于从excel中读取到的check为str类型，所以response不用转换为dict，直接断言比较是否相等
            assert check == response
            print("测试通过")
        except Exception as e:
            print("测试失败")
            raise e


if __name__ == "__main__":
    unittest.main()
