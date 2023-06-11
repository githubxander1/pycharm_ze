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

# lst=[1,2,3]
# sum=0
# for i in lst:
#     sum+=sum
#     print(sum)
# str='hello'
# for cha in str:
#     print(ord(cha))
# i=1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# i=1
# sum=0
# while i <= 100:
#     i +=1
#     sum+=i
# print(sum)
# 编写一个程序，找出列表中的最大值并输出。
# lst=[1,2,3,4]
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
#     if num == num[::-1]:
#         return True
#     else:
#         return False
#
#
# print(num_is_hui(132))
def jia(product_type,type,n):
    if product_type=='指定单日门票':
        if type=='标准票':
            return 638*n
        elif type in ('儿童票,老年票') :
            return 480*n
    elif product_type=='指定1.5日门票':
        if type=='标准票':
            return 1020*n
        elif type in ('儿童票,老年票'):
            return 765*n
shuru=input()
shuru2=input()
shuru3=eval(input())
print(jia(shuru,shuru2,shuru3))