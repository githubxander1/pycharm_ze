# str1 = '''
# 熊宁
# 杰益
#
# 王伟伟
#
# 青芳
#
# 玉琴
# 焦候涛
# 莫福
# 杨高旺
# 唐欢欢
# 韩旭
# '''
#
# str2 = '''
# 焦候涛
# 熊宁
# 玉琴
#
# 骆龙
#
# 韩旭
# 杨高旺
#
# 杰益
#
# 莫福
#
# 伟伟
#
# 李福
# '''
# 请写一个程序
#找出str1中所有str2中不存在的人名，并且
#找出str2中所有str1中不存在的人名
#
str1 = '''
熊宁
杰益

王伟伟

青芳

玉琴
焦候涛
莫福
杨高旺
唐欢欢
韩旭
'''

str2 = '''
焦候涛
熊宁
玉琴

骆龙

韩旭
杨高旺

杰益

莫福

伟伟

李福
'''
def get_namelist():
    tem = str.splitlines()
    names=[]
    for name in tem:
        name=name.strip()
        if name == '':
            continue

        names.append(name)

    return names

name1=get_namelist(str1)
name2=get_namelist(str2)

print('str1中独有的人名：')
for name in name1:
    if name not in name2:
        print(name)

printI('str2中独有的人名：')
for name in name2:
    if name not in name1:
        print(name)

#
# 题目2
# 有如下的字符串，记录了三国人物的名字和年龄
#
# ageTable = '''
#     诸葛亮, 28
#     刘备, 48
#     刘琦, 25
#     赵云, 32
#     张飞, 43
#     关羽, 45
# '''
# 请写一个程序将其中30岁以上和以下的人分别打印出来，类似这样
# 大于等于30岁的人有：
# 刘备
# 赵云
# 张飞
# 关羽
#
# 小于30岁的人有：
# 诸葛亮
# 刘琦

ageTable = '''
            诸葛亮, 28
            刘备, 48
            刘琦, 25
            赵云, 32
            张飞, 43
            关羽, 45
        '''
ageList=[]
for item in ageTable.split('\n'):
    if item.strip() == '':
        continue

    ageList.append(item)

g30=[]
l30=[]

for oneman in ageList:
    name,age = oneman.split(',')
    age = int(age.strip())
    name= name.strip()
    if age >= 30:
        age.append(name)
    else:
        l30.append(name)

print('大于等于30岁的人有：')
for man in g30:
    print(man)

print('小于30岁的人有：')
for man in l30:
    print(man)