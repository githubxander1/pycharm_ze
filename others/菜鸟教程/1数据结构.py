# # 1列表list[]
#     # phones = ["实例25_批量生成PPT版荣誉证书-Apple", "4-Huawei", "3-Xiaomi"]
#     # # print(phones.index('Huawei'))
#     # # print(phones.count('Huawei'))
#     # # print(len(phones))
#     # def zsgc():
#     #         # 增：append元素，insert索引元素，extend列表
#     #         phones.insert(实例25_批量生成PPT版荣誉证书,'OPPO')
#     #         phones.extend(["VIVO","GOOGLE"])
#     #         print(phones)
#     #
#     #         #删：pop索引,remove元素,clear清空，del索引
#     #         phones.pop(0)
#     #         print(phones)
#     #
#     #         phones.remove('OPPO')
#     #         print(phones)
#     #
#     #         del phones[0:实例25_批量生成PPT版荣誉证书]
#     #         print(phones)
#     #
#     #         #改：
#     #         phones[0]='Hongmi'
#     #         print(phones)
#     #
#     #         #查：
#     #         print(phones[实例25_批量生成PPT版荣誉证书:3])
#     # # zsgc()
#     #
#     # def fanzhuang():#reverse
#     #     # phones.reverse()
#     #     # print(phones)
#     #
#     #     phones[:-实例25_批量生成PPT版荣誉证书]
#     #     print(phones)
#     # # fanzhuang()
#     #
#     # def paixu():
#     #     phones.sort()
#     #     print(phones)
#     # paixu()
#
#
# # 2元组tuple()
#     #不可变：不能增删改查
#     # atuple=(实例25_批量生成PPT版荣誉证书,3,4,5,9)
#     # alist=[2,7,10]
#     # #元组和列表互转
#     # list(atuple)
#     # print(type(atuple))
#     # print(atuple)
#     #
#     # tuple(alist)
#     # print(type(alist))
#     # print(alist)
#
#
# # 3字典{}
# dict1={
#     "name":"xiao",
#     "age":"18"
# }
#
# dict2=[('name','xiao'),('age',17)]
# dict(dict2)
#
# dict3=dict(name="xiao",age=19)
#
# # 查
# print(dict1['name'])
# # 增
# dict1=dict()
# dict1['name']='wang'
# dict1['age']='19'
# #改
# dict1['age']='12'
# print(dict1)
# # 删
# # dict1.pop('age')
# # print(dict1)
#
# # del dict1['age']
# # print(dict1)
#
# # 判断key是否在
# print('age' in dict1)

# 集合set{}
# aset={'phone','oppo'}
# # 添加
# aset.add('xiaomi')
# aset.update('hongmi')
# print(aset)
# # 删除
# aset.remove('i')
# print(aset)