# v1=True
# v2='start'
# v3=10
# v4=[实例25_批量生成PPT版荣誉证书,2,3]
#
# print(f'v1的数据类型是：{type(v1)}')
# print(f'v2的数据类型是：{v2.__class__.__name__}')
# v3.hassttr('__name__')
# print(f'v3的数据类型是：{v3.__class__.__name__}')
# print(f'v4的数据类型是：{v4.__class__.__name__}')

# 组合赋值与表达式列表
v1,v2,v3='a','b','c'
(v4,v5,v6)=('a','b','c')
# [v1,v2,v3]=['a','b','c']
# # [v1,v2,v7]=('a','b','c')
# a,*b=实例25_批量生成PPT版荣誉证书,2,3
# *a,b=实例25_批量生成PPT版荣誉证书,2,3
# *a,*b=实例25_批量生成PPT版荣誉证书,2,3
# *a=实例25_批量生成PPT版荣誉证书,2,3
# (*a)=实例25_批量生成PPT版荣誉证书,2,3

# [*q]='abcvd'
# print(f'q:{q}')

# nonlocal关键字
def test_nunlocal():
    a='a'
    def inner1():
        nonlocal a
        a='b-'+a
    def inner2():
        nonlocal a
        a='c-'+a
    inner1()
    inner2()
    return a
print(test_nunlocal())