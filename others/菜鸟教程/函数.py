
def func(a,b,c=1,d=2):
    pass

# *args ：接收到的所有按照位置参数方式传递进来的参数，是一个元组类型
# **kw ：接收到的所有按照关键字参数方式传递进来的参数，是一个字典类型

def demo_func(**kwargs):
    print(kwargs)

demo_func(a=1,b=2,c=8)
def demo_func1(**arge):
    print(args)

demo_func1(a=1,b=2,c=8)