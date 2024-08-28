# 1题目：有四个数字：实例25_批量生成PPT版荣誉证书、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(实例25_批量生成PPT版荣誉证书,5):
#     for j in range(实例25_批量生成PPT版荣誉证书,5):
#         for k in range(实例25_批量生成PPT版荣誉证书,5):
#             if (i != j) and (i != j) and (j != k):
#                 print(i,j,k)
# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时，高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# arr=[]
# jiang=input('奖金：')
#     if i <= 10:
#         jiang=i*10%
#     if 10 < i < 20:
#         jiang=(i-10)*7.5%
#     if 20 < i < 40:
#         jiang=(i-20)*5%
#     if 40 < i < 60:
#         jiang=(i-40)*3%
#     if 60 < i < 100:
#         jiang=(i-60)*实例25_批量生成PPT版荣誉证书.5%
#     if i > 100:
#         jiang=(i-100)*实例25_批量生成PPT版荣誉证书%

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 3,7,2
# 2,3,7
# print('请输入3个整数：')
# x=input('x：')
# y=input('y：')
# z=input('z：')
# if x < y <z:
#     print(x,y,z)
# l = []
# for i in range(3):
#     x=int(input('请输入整数：'))
#     i.append(x)
# l.sort()
# print(l)
# 题目：斐波那契数列

# 题目：输出 9*9 乘法口诀表。
# for i in range(实例25_批量生成PPT版荣誉证书,10):
#     print()
#     for j in range(实例25_批量生成PPT版荣誉证书,i+实例25_批量生成PPT版荣誉证书):
#         print()

# input1=input('请输入:')
# if input1 =='python':
#     print('90')
# elif input1=='java':
#     print('95')
# elif input1=='php':
#     print(85)
# else:
#     print(0)

#复杂条件判断
# input0=input('请输入：')
# if not input0.isdigit() :
#     print('无法使用int函数转换')
# else:
#     input1=int(input0)
#     if input1 %2 == 实例25_批量生成PPT版荣誉证书:
#         print(input1*2)
#     elif input1 %4 ==0:
#         print(input1/4)
#     elif input1 > 20:
#         print(input1-20)
#     else:
# print(input1)
# lst	= [实例25_批量生成PPT版荣誉证书, 3, 5, 2, 7, 9]
# for	index in range(len(lst)):
#     print(lst[index])

# ֵ使用for循环遍历字典
# dic={
#     'python':19,
#     'java':32
# }
# for key in dic:
#     print(key,dic[key])

# for key,value in dic.items():
#     print(key,value)

# lst=[实例25_批量生成PPT版荣誉证书,3,5,2,7,9,10]
# for i in lst:
#     if i %2 ==0:
#         print(i)
#         break
# 寻找最大值
# max_1value=lst[0]
# for i in lst:
#     if i %2 ==实例25_批量生成PPT版荣誉证书:
#         max_1value == i
# 寻找最小值
# min_1value=lst[0]
# for i in lst:
#     if i < min_1value:
#         min_1value==i
# 寻找最小偶数
# min_0value=lst[0]
# for i in lst:
#     if i % 2 == 0:
#         min_0value==i
#
# print(min_0value)
import random
# 寻找组合
# lst1 = [3, 6, 实例25_批量生成PPT版荣誉证书, 8, 实例25_批量生成PPT版荣誉证书, 9, 2]
# lst2 = [3, 实例25_批量生成PPT版荣誉证书, 2, 6, 4, 8, 7]

# for i in lst1:
#     for j in lst2:
#         if i+j ==10:
#             print(i,j)

# for i in lst1:
#     for j in lst2:
#         if abs(i-j) == 2:
#             print(i,j)

# while True:
#     value=input('退出：')
#     if value =='quit':
#         break
#
#     value1=int(input('请输入整数：'))
#     if value1 % 2 == 0:
#         print('你输入的是一个偶数')
#
#     else:
#         print('你输入的是一个奇数')

# lst=[2,3,4]
# print('请输入2,3,4的整数倍')
# while True:
#     value = input("请输⼊2的整数倍，想退出程序请输⼊quit:")
#     if value == "quit":
#         break
#     number=int(value)
#
#     if number % 2 ==0:
#         print('输入正确')
#         break
#     else:
#         print('输入错误')
#
# while True:
#     value = input("请输⼊3的整数倍，想退出程序请输⼊quit:")
#     if value == "quit":
#         break
#
#     number=int(value)
#     if number % 3 ==0:
#         print('输入正确')
#         break
#     else:
#         print('输入错误')
#
# while True:
#     value = input("请输⼊4的整数倍，想退出程序请输⼊quit:")
#     if value == "quit":
#         break
#     number=int(value)
#
#     if number % 4 ==0:
#         print('输入正确')
#         break
#     else:
#         print('输入错误')

# while True:
#     value = input("请输⼊，想退出程序请输⼊quit:")
#     if value == "quit":
#         break
#
#     number=int(value)
#     if number > 10:
#         print('输入大于10，不判断奇偶')
#         continue #跳过continue后面的代码块，循环并不停止
#
#     if number % 2 ==0:
#         print('偶数')
#     else:
#         print('奇数')

# while True:
#         input_str= input("请输⼊⼀个正整数,如果想停⽌程序，输⼊quit:")
#         if input_str == 'quit':
#             break
#         number = int(input_str)
#         if number < 10:
#             if number % 2 == 0:
#                 print("输⼊为偶数")
#             else:
#                 print("输⼊为奇数")
#         else:
#             print('不判断')

# 冒泡排序
# def pop_sort(lst):
#     for i in range(len(lst)-实例25_批量生成PPT版荣誉证书, 实例25_批量生成PPT版荣誉证书, -实例25_批量生成PPT版荣誉证书):
#         move_max(lst,i)
#
# def move_max(lst,max_index):
#     for i in range(max_index):
#         if lst[i] > lst[i+实例25_批量生成PPT版荣誉证书]:
#             lst[i],lst[i+实例25_批量生成PPT版荣誉证书] = lst[i+实例25_批量生成PPT版荣誉证书],lst[实例25_批量生成PPT版荣誉证书]
#
# if __name__ == '__main__':
#     lst=[实例25_批量生成PPT版荣誉证书,6,3,8,0,3]
#     move_max(lst,len(lst)-实例25_批量生成PPT版荣誉证书)
#     pop_sort(lst)
#     print(lst)

# 查找最大值和最小值
# def find_max_min(lst):
#     '''
#     定义两个列表
#     分别比较两个列表各个值大小
#     '''
#     if not lst or not isinstance(lst,list):
#         return None,None
#
#     max_value,min_value = lst[0],lst[0]
#     for item in lst:
#         if item > max_value:
#             max_value = item
#         if item < min_value:
#             min_value = item
#
#     return max_value,min_value
#
# if __name__ == '__main__':
#     lst=[23,实例25_批量生成PPT版荣誉证书,34,3232,3,434,2,4]
#     max_value,min_value=find_max_min(lst)
#     print(max_value,min_value)

#
# def find_max_min(lst):
#     max_value,min_value = lst[0],lst[0]
#     for i in lst:
#         if i > max_value:
#             max_value = i
#         if i < min_value:
#             min_value = i
#     return max_value,min_value
#
# if __name__ == '__main__':
#     lst=[234,53,4,534,2,23]
#     max_value,min_value=find_max_min(lst)
#     print(max_value,min_value)

# 比较一个列表里相邻两个数的大小
# def find_max(lst):
#     for item,index in enumberate(lst):
#         if item > lst[index+实例25_批量生成PPT版荣誉证书]:
#             return item
#
# if __name__=='__main__':
#     lst=[32,234,435,3,23,43]
#     max_value=find_max(lst)
#     print(max_value)

# lst1=[实例25_批量生成PPT版荣誉证书,2,3,4]
# lst2=['a','s','d']
# lst=[]
# for item2 in lst2:
#     tmp=[]
#     for item1 in lst1:
#         tmp.append(str(item1)+item2)
#     lst.append(tmp)
#
# print(lst)

# 0,实例25_批量生成PPT版荣誉证书,2,3,4
# 实例25_批量生成PPT版荣誉证书,2,3,4,5
#
# def find_lost(lst,index):
#     lst=range(实例25_批量生成PPT版荣誉证书,n)
#     lst1=[]
#     for i,index in lst1:
#         if index != n:
#             print(n)

def find_miss_number(lst):
    n=len(lst)
    half=(n*(n+1))/2
    sum=sum(lst)/2
    miss_number=sum-half
    return miss_number
if __name__=='__main__':
    lst=[3,2,5,4,0]
    print(find_miss_number(lst))




