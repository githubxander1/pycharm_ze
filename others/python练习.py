#
# a=int(input('请输入数字：'))
# if a % 2 == 0:
#     print('偶数')
# else:
#     print('不是偶数')

# grade=int(input('请输入成绩：'))
# if grade >= 90:
#     print('A')
# elif 80 < grade < 89:
#     print('B')
# elif 70 <grade <79:
#     print('C')
# elif 60 < grade < 69:
#     print("D")
# else:
#     print('E')
# score = int(input("Please enter your score: "))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("E")

# lst=[实例25_批量生成PPT版荣誉证书,2,3]
# sum=0
# for i in lst:
#     sum+=sum
#     print(sum)
# str='hello'
# for cha in str:
#     print(ord(cha))
# i=实例25_批量生成PPT版荣誉证书
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 实例25_批量生成PPT版荣誉证书
# i=实例25_批量生成PPT版荣誉证书
# sum=0
# while i <= 100:
#     i +=实例25_批量生成PPT版荣誉证书
#     sum+=i
# print(sum)
# 编写一个程序，找出列表中的最大值并输出。
# lst=[实例25_批量生成PPT版荣誉证书,2,3,4]
# max=lst[0]
# for i in lst:
#     if i > max:
#         max = i
# print(max)
# 编写一个程序，要求用户输入一个字符串，并将字符串反转后输出。
# str=str(input())
# print(str.)
# 编写一个程序，要求用户输入两个字符串，分别将其首位拼接在一起并输出。
# str1=str(input('str1:'))
# str2=str(input('str2:'))
# print(str1[0]+str2[0])
# 编写一个程序，要求用户输入一个字符串和一个子字符串，如果字符串中包含子字符串则将其替换为另一个字符串并输出，否则输出原字符串。
# 编写一个程序，创建一个包含10个整数的列表，要求分别求出列表中的最大值、最小值、和以及平均值。
# lst=[i for i in range(10) ]
# print(lst)
# lst.sort()
# newlst=[]
# for i in lst:
#     if i % 2 ==0:
#         newlst.append(i)
# print('max:',max(lst))
# print('min:',min(lst))
# print('average:',sum(lst)/len(lst))
# 编写一个程序，创建一个包含10个整数的列表，要求对列表进行排序并输出排序后的结果。
#
# 编写一个程序，创建一个包含10个整数的列表，要求将列表中的偶数提取出来并存放在一个新的列表中
# def num_is_hui(num: int):
#     num = input()
#     if num == num[::-实例25_批量生成PPT版荣誉证书]:
#         return True
#     else:
#         return False
#
#
# print(num_is_hui(132))
# def jia(product_type,type,n):
#     if product_type=='指定单日门票':
#         if type=='标准票':
#             return 638*n
#         elif type in ('儿童票,老年票') :
#             return 480*n
#     elif product_type=='指定1.5日门票':
#         if type=='标准票':
#             return 1020*n
#         elif type in ('儿童票,老年票'):
#             return 765*n
# shuru=input()
# shuru2=input()
# shuru3=eval(input())
# print(jia(shuru,shuru2,shuru3))

# 迭代
# 迭代是循环的一种，迭代是指在可迭代对象上实现for循环
# 迭代器是实现了__next__()方法的对象
# 迭代器对象可以被next()函数调用并不断返回下一个值
# mystr=iter('banner')
# print(next(mystr))
# print(next(mystr))
#
# print('使用for循环迭代')
# for i in mystr:
#     print(i)
#
# print('使用while循环迭代')
# mystr=iter('banner')
# while True:
#     try:
#         print(next(mystr))
#     except StopIteration:#为了防止迭代永远进行，我们可以使用 StopIteration 语句
#         break
#
# print('使用enumerate()函数迭代')
# mylist=[实例25_批量生成PPT版荣誉证书,2,3,4,5]
# for i,j in enumerate(mylist):
#     print(i,j)
#
# print('使用zip()函数迭代')
# mylist=[实例25_批量生成PPT版荣誉证书,2,3,4,5]
# mylist2=['a','b','c','d','e']
# for i,j in zip(mylist,mylist2):
#     print(i,j)
#
# print('使用reversed()函数迭代')
# mylist=[实例25_批量生成PPT版荣誉证书,2,3,4,5]
# for i in reversed(mylist):
#     print(i)
#
# print('使用sorted()函数迭代')
# mylist=[实例25_批量生成PPT版荣誉证书,2,3,4,5]
# for i in sorted(mylist):
#     print(i)
#
# print('使用filter()函数迭代')
# def is_odd(n):
#     return n%2==实例25_批量生成PPT版荣誉证书
#
# mylist=[实例25_批量生成PPT版荣誉证书,2,3,4,5]
# for i in filter(is_odd,mylist):
#     print(i)
#
# print('使用map()函数迭代')
# def power(x):
#     return x**2
#
# mylist=[实例25_批量生成PPT版荣誉证书,2,3,4,5]
# for i in map(power,mylist):
#     print(i)
#
# print('使用reduce()函数迭代')
# from functools import reduce
# def add(x,y):
#     return x+y
#
# mylist=[实例25_批量生成PPT版荣誉证书,2,3,4,5]
# for i in reduce(add,mylist):
#     print(i)
#
# print('创建迭代器')
# class myiter:
#     def __iter__(self):
#         self.a=实例25_批量生成PPT版荣誉证书
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=实例25_批量生成PPT版荣誉证书
#         return x
# myiter=iter(myiter())
# print(next(myiter))

# 生成器
# 生成器是一种迭代器，生成器只能用于迭代操作，不能用于索引
# 生成器是迭代器，迭代器是生成器

# 生成器函数
# 生成器函数是返回生成器对象，生成器函数的返回值是生成器对象
# 生成器函数的返回值是生成器对象
# def mygenerator():

# 列表生成式
# 列表生成式是一种生成列表的简单方法，它以一种简洁的语法生成列表
# 列表生成式可以写成for循环的形式
# 列表生成式中，for前面的部分称为生成器，它产生待处理的对象，
# for后面的部分称为过滤器，它对产生的对象进行筛选，最终产生我们想要的结果

# 生成器
# 生成器是一种迭代器，生成器只能用于迭代操作，不能用于索引
# 生成器是迭代器，迭代器是生成器

# 日期
# import datetime
#
# # x= datetime.datetime.now()
# # print('当前时间是：',x)
# # print('当前时间：',x.year,'年',x.month,'月',x.day,'日',x.strftime('%H:%M:%S'))
# # 创建日期对象
# x=datetime.datetime(2023,8,18)
# print('创建日期对象：',x)
import json
# x= '{"name":"张三","age":20,"name":"李四"}'
# # 解析x
# y=json.loads(x)
# print(y['name'])
# x1={'name':'张三','age':20}
# y1=json.dumps(x1)
# print(y1)
# print(json.dumps({"name": "Bill", "age": 63}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
from pprint import pprint

# x = {
#   "name": "Bill",
#   "age": 63,
#   "married": True,
#   "divorced": False,
#   "children": ("Jennifer","Rory","Phoebe"),
#   "pets": None,
#   "cars": [
#     {"model": "Porsche", "mpg": 38.2},
#     {"model": "BMW M5", "mpg": 26.9}
#   ]
# }
# # 使用 indent 参数定义缩进数：使用 separators 参数来更改默认分隔符：使用 sort_keys 参数来指定是否应对结果进行排序：
# print(json.dumps(x,indent=4, sort_keys=True,separators=(',', ': ')))

# RegEx正则表达式
# import re
# text='Hello 123 4567 World_This is a Regex Demo'
# # findall:查找所有匹配并返回一个列表：
# # search:如果字符串中的任意位置存在匹配，则返回match对象
# print(re.search('\s',text))
# print('split:拆分')
# print(re.split('\s+',text))
# print('通过指定 maxsplit 参数来控制出现次数：')
# print(re.split('\s*',text,5))
# print('sub:替换')
# print(re.sub('\s*','替换',text))
# print('通过指定 count 参数来控制替换次数：')
# print(re.sub('\s*','替换',text,3))

# 字符串格式化
# 字符串 format()
# 索引号
# print('{0},{实例25_批量生成PPT版荣誉证书},{2}'.format('a','b','c'))
# # 关键字
# print('{name},{age},{sex}'.format(name='a',age='b',sex='c'))
# # 格式化 f
# a=实例25_批量生成PPT版荣誉证书
# b=2
# print(f'{实例25_批量生成PPT版荣誉证书},{2}')
# # 格式化字典
# print(f'{a},{b}')
# # 格式化列表
# print(f'{[a,b]}')
# # 格式化元组
# print(f'{(a,b)}')

# 文件处理
# 读取文件
# f=open('flashing_icon.txt','r')
# print(f.read(5))#读取前五个字符
# print(f.readline())#读一行
# for x in f:#遍历文件
#     print(x)
# f.close()
# 追加
# f=open('flashing_icon.txt','a')
# f.write('hello world')
# f.close()
# f=open('flashing_icon.txt','r')
# print(f.read())
# 覆盖
# f=open('flashing_icon.txt','w')
# f.write('hello world')
# f.close()
# f=open('flashing_icon.txt','r')
# print(f.read())
# 创建
# f=open('flashing_icon.txt','x')
# f.close()
# 删除
# import os
# if os.path.exists('flashing_icon.txt'):
#         os.remove('flashing_icon.txt')
#         os.rmdir('testfolder')
# else:
#     print('文件不存在')
