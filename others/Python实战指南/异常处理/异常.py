# 自定义异常类
class custException(Exception):
    def __init__(self,*args,message=None):
        #调用基类的构造函数
        super().__init__(*args)
        self.message=message

try:
    raise custException(6,7,message='未知错误')
except custException as e:
    print(f'参数：{e.args}')
    print(f'异常信息：{e.message}')

# else
# 当else子句出现在try代码块中时，如果try之后的代码成功执行（未引发异常），随后会执行else子句，最后执行finally子句（如果存在）；
# 如果在执行try之后的代码时发生异常，就会执行except子句，else子句被忽略（不会执行）。
try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为0')

else:
    print('没有异常')

# finally
# finally子句始终会被执行，无论try代码块中是否发生异常。
try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为0')
finally:
    print('无论是否有异常都：运行结束')

# 抛出异常
# raise语句抛出一个异常，使用raise语句抛出异常时，必须指定异常的类型。
# raise语句抛出异常时，还可以同时抛出一个值，该值将作为异常实例的参数值。
try:
    raise Exception('异常信息')
except Exception as e:
    print(e)

# 捕获异常
try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)

# 捕获多个异常
try:
    print(1/0)
except (ZeroDivisionError,TypeError) as e:
    print(e)

# 捕获所有异常
try:
    print(1/0)
except Exception as e:
    print(e)

# 捕获异常并处理
try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为0')
