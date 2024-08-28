# from mylib import *
#
# r1=add(实例25_批量生成PPT版荣誉证书,3)
# r2=sub(3,实例25_批量生成PPT版荣誉证书)
# r3=mul(2,3)
# r4=div(3,2)
#
# print(r1)
# print(r2)
# print(r3)
# print(r4)

# from root import *
# dic = globals().copy()
# print(dic.keys())
# membs = [x for x in dic.keys() if x[0] != "_"]
# for x in membs:
#     print(x)

from  mylib import *
import mylib
# from z_others.Python实战指南.模块 import mylib
from .mylib import test_fun_a
from .mylib import test_fun_b

test_fun_a()
test_fun_b()
print(mylib.__path__)