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
lst=[1,2,3,4]
max=lst[0]
for i in lst:
    if i > max:
        max = i
print(max)

