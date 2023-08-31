
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

# # 字符串编解码
# str='测试字符串'
# str1=str.encode('utf-8')
# print(str1)
#
# str2=str1.decode('utf-8')
# print(str2)

# 获取字符编码
str='一二三四五'
for i in str:
    print(f'{i} --> {ord(i)}')

codes=[19968,20108,19978]
for i in codes:
    print(f'{i} --> {chr(i)}')