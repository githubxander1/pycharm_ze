# get_ddt
import unittest

import openpyxl
import pyaml
from ddt import ddt, data, unpack, file_data


from com_excel import readExcel
@ddt  # 声明类装饰器
class TestDdt(unittest.TestCase):
    # 加载excel文件
    @data(*readExcel())
    @unpack
    def test_getExcel(self,id,name,password):
        id = id
        name = name
        print(id,name)
    # 加载json文件
    # @file_data('data_json.json')
    # def test02(self, name, age, addr):
    #     name = name
    #     age = age
    #     addr = addr
    #     print(name, age, addr)

    # @file_data('data_json.json')
    # def test_logs(self,**testdata):#将提取到的数据存到testdata里
    #     name=testdata['name']
    #     age=testdata['age']
    #     addr=testdata['addr']
    #     print(name,age,addr)
    #     print(testdata)

    # 加载yaml文件
    # @file_data('data_yaml.sina.yaml')
    # def test04(self,model,title,url,method,data,check):
    #     username=data['username']
    #     password=data['password']
    #
    #     print(model,title,url,method,data,check)
    #     print(username,password)

    # @file_data('data_yaml.sina.yaml')
    # def test03(self, **testd):  # 将提取到的数据存到testd里
    #     model = testd['model']
    #     title = testd['title']
    #     print(model, title)
    #     print(testd)



if __name__ == '__main__':
    unittest.main()
    # ddtTest.readExcel()
