# # get_ddt.py
#
# import unittest
# from ddt import ddt, data, unpack, file_data
#
# # ddt类装饰器++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# @ddt
# class MyddtTest(unittest.TestCase):
#
#     # @data方法装饰器，会将数据以逗号分隔，有几个就是几组数据，循环传入函数++++++++++++++++++++++++++++++++++++++
#     # @data(实例25_批量生成PPT版荣誉证书,2,dataInExcel)
#     # def test_01(self, value):   # value用来接受data的数据
#     #     print(value)
#     #     # 实例25_批量生成PPT版荣誉证书
#     #     # 2
#     #     # dataInExcel
#
# # 列表
# #     @data([{'name':'peter','age':18},{'name':'tom','age':21}])
#     # def test03(self,value1):
#     #     print(value1)
#     # [{'name': 'peter', 'age': 18}, {'name': 'tom', 'age': 21}]
#  # @unpack拆分，相当于把数据的最外层结构去掉，data装饰器传过来的数据进行拆分++++++++++++++++++++++++++++++++++++++
#  #    @data([5,6],[7,8])
#  #    @unpack
#  #    def test04(self,value1,value2):
#  #        print(value1,value2)
#     # 5 6
#     # 7 8
# # # 多个列表字典，拆分
# #     @data([{'name':'peter','age':12,'addr':'chang'},
# #            {'name':'xiao','age':11,'addr':'gan'}])
# #     @unpack
# #     def test05(self,value1,value2):
# #         print(value1,value2)
#         # {'name': 'peter', 'age': 12, 'addr': 'chang'}
#         # {'name': 'xiao', 'age': 11, 'addr': 'gan'}
#
# # 单个字典，拆分
#     # # @data里的数据key必须与字典的key保持一致
#     @data({'name':'jack','age':31})
#     @unpack
#     def test06(self,name,age):
#         print(name,age)
#
#     # # 多个字典, 拆分
#     @data({'name':'peter','age':11},
#           {'name':'tom','age':23},
#           {'name':'jim','age':32})
#     @unpack
#     def test07(self,name,age):
#         print(name,age)
#
# if __name__ == '__main__':
#     unittest.main()
#
# # from ddt import data, unpack, ddt
# # import unittest
# # #
# # testda=(("byhy",88888888),(23,45),(实例25_批量生成PPT版荣誉证书,2))
# # @ddt
# # class ztest(unittest.TestCase):
# #     @data(*testda)
# #     @unpack
# #     def test_data1(self,user,pass1):
# #         print(user,pass1)
#
# # test_data = (实例25_批量生成PPT版荣誉证书, 2, dataInExcel)
# # @ddt      # 需要在要引用的类前面加上 @ddt声明
# # class TestAdd(unittest.TestCase):
# #     @data(test_data)       # 调用ddt的数据
# #     def test_add(self, a):
# #         print(a)
# #
# # """元组、列表数据驱动"""
# # import unittest
# # from ddt import ddt, data, unpack
# #
# # test_data = ((实例25_批量生成PPT版荣誉证书, 2, dataInExcel), (4, 5, 6), (7, 8, 9))
# # @ddt      # 需要在要引用的类前面加上 @ddt声明
# # class TestAdd(unittest.TestCase):
# #     @data(test_data)   # 调用ddt的数据
# #     @unpack
# #     def test_add(self, a, b, c):
# #         print('数据类型为', type(a), '数值为', a)
# #         print('数据类型为', type(b), '数值为', b)
# #         print('数据类型为', type(c), '数值为', c)
# # """字典类型数据驱动"""
# # import unittest
# # from ddt import ddt, data, unpack
# #
# # test_data = {"tall": 180, "sex": "boy"}
# # @ddt
# # class TestAdd(unittest.TestCase):
# #     @data(test_data)
# #     @unpack
# #     def test_add(self, tall, sex):   # 此处的形参必须要是字典的键值
# #         print("身高是", tall, "性别是", sex)
#
#
# #
# # import unittest
# # from ddt import ddt, data, unpack
# #
# # case_data = [{"url": "www.baidu.com", "data": "test_logs"},
# #              {"url": "www.baidu.com", "data": "test2"},
# #              {"url": "www.baidu.com", "data": "test3"}]
# #
# #
# # @ddt
# # class TestDemo(unittest.TestCase):
# #     @data(*case_data)
# #     def test_case(self, case):
# #         print(case)
# import unittest
# import requests  # 导入接口自动化的库
# from ddt import ddt, data, unpack, file_data
#
#
# # 接口的地址
# @ddt
# class Demo(unittest.TestCase):
#     # 第一种:不加unpack，直接传字典
#     @data({'email': "2695418206@qq.com", 'from': "web", 'product': "master-online",
#            'pw': "f2d8ddfc169a0ee6f8b0ecd924b1d300"},
#           )
#     def test_01(self, value):
#         url = 'https://userapi.edrawsoft.cn/api/user/login'
#         re = requests.post(url=url, data=value)
#         print(re)
#
#         # 第二种：加unpack，把列表解析成字典，，，
#         # @data([{'email': "2695418206@qq.com", 'from': "web", 'product': "master-online",
#         #        'pw': "f2d8ddfc169a0ee6f8b0ecd924b1d300"}]
#         #       )
#         # @unpack
#         # def test_01(self, value):
#         #     url = 'https://userapi.edrawsoft.cn/api/user/login'
#         #     re = requests.post(url=url, data=value)
#         # result=pre in re.json()
#         # print(result)
#
#
# if __name__ == '__main__':
#     unittest.main()
#
