
from demo_mode import *
import demo_mode

# keys = globals().copy().keys()
# for k in keys:
#     print(k)

# __file__和__cached__：__file__属性可以获取模块的源代码文件的路径，而__cached__属性则用于获取与模块代码对应的二进制文件的路径（即编译后的文件，扩展名为.pyc）。
print(f'代码文件路径：{demo_mode.__file__}')
print(f'编译后的文件路径{demo_mode.__cached__}')