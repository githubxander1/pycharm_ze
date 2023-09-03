
# print(f"{'左对齐':<20s}")
# print(f"{'居中对齐':^20s}")
# print(f"{'右对齐':>20s}")
# print(f"{'左对齐':*<20s}")
# print(f"{'居中对齐':%^20s}")
# print(f"{'右对齐':#>20s}")
# print(f"{111:= #2Ob}")

# 数字的千位分隔符
# num=123456789
# print(f'{int(num):,d}')
# #d标志符只能用于整型数值，因此需要调用int类的构造函数int（num）将浮点数值num转换为整数值
# print(f'{int(num):,.2f}')
#
# # "_"分隔符
# print(f'{num:#_o}')#八进制
# print(f'{num:#_d}')#十进制
# print(f'{num:#_b}')#二进制
# print(f'{num:#_x}')#十六进制

# 自定义日期格式
# import datetime
#
# t=datetime.time(20,14,25)
# t1=datetime.date(2023,11,11)
# print(f'{t1:%Y-%m-%d}')
# print(f'{t1:%Y}年{t1:%m}月{t1:%d}日')
# print(t)

# format格式化
# import string
#
# print('{0},{1}'.format('第一','第二'))
# print('{first},{second}'.format(first='第一个',second='第二个'))
#
# # 字符串模板
# tp=string.Template('天空飘着几朵$what')
# s1=tp.substitute(what='白云')
# print(s1)
# tp1=string.Template('屏幕尺寸为${len}inch')
# s2=tp1.substitute(len=6.9)
# print(s2)

# 字符串模板的安全替换模式：safe_substitute
# from string import Template
#
# t=Template('$who likes $football')
# r=t.safe_substitute(who='Tom')
# print(r)

# 文本缩进
# import textwrap
#
# def ignoreETLines(line):
#     if line == '\n' or line =='\r':
#         return False
#     return True
# sorcel='首行文本\n第二行文本\n第三行文本'
# result=textwrap.indent(sorcel,prefix='++')
# print(result)
# sorcel1='首行文本\n\n\n第二行文本\n第三行文本'
# result1=textwrap.indent(sorcel,prefix='++',predicate=ignoreETLines)
# print(result1)

# 嵌套使用格式化语法
# width = 19
# s= '{0:{wd}d}'.format(200,wd=width)
# print(s)

# num=input('请输入一个十进制整数：')
# if not num.isdecimal():
#     print('不是有效整数值')
# else:
#     print('''
#     x---十六进制
#     b---二进制
#     o--八进制
#     ''')
# type=input('请输入要打印的格式：')
# valuetypes='b','o','x'
# if not type in valuetypes:
#     print('无效')
# else:
#     # 转换成整数
#     num=int(num)
#     print(f'结果：{num:#{type}}')

# str字符串转化
# print('XMNxbn'.upper())
# print('XMNxbn'.lower())
# print('XMNxbn'.swapcase())

# 用0填充
# print('155'.zfill(8))
# print('-155'.zfill(8))
# print('-abc'.zfill(8))

# 字符串对齐方式
# print('测试文本'.ljust(25,'>'))
# print('测试文本'.rjust(25,'>'))
# print('测试文本'.center(25,'#'))

# 查找子字符串
# str='床前明月光，疑是地上霜'
# index1=str.find('月')
# index2=str.rfind('月')
#
# print(f'原字符串：{str}')
# print(f'‘月’的位置:\n从左往右:{index1}\n从右往左:{index2}')

# startswith和endswith
# str1='captions'
# print(str1.startswith('cap'))
# print(str1.endswith('s'))

# 统计字符串出现次数
# str1='database'
# print(f"'a'出现次数:{str1.count('a')}")

# 文本的标题样式
# str1='what is the name'
# print(str1.capitalize())
# print(str1.title())

# 串联字符串
# a=('a','b','c','d','e','f','g')
# print('*'.join(a))
# print(' '.join(a))

# 拆分字符串
# str='#sdafds#fds#123'
# print(str.split('#'))
# print(str.split('#',2))
# print(str.rsplit('#',2))

# 替换字符串
# str='三宫六院'
# str1=str.replace('宫','高')
# print(str1)

# 去掉字符串首尾空格
a='   abc   '
a1='   \tabc\n\n   '
b=a.strip()
b1=a1.strip()
c=a.lstrip()
d=a.rstrip()

print(a)
print(a1)
print(b)
print(b1)
print(c)
print(d)