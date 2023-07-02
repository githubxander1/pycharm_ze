class A:
    age= 10#普通类属性
    __age= 100
    #私有类属性
    def __init__(self):
        self.__name='Amike'#私有实例属性
    def __f1(self):#私有方法
        print('私有方法')
    def f2(self):#在类的内部可以直接访问私有属性和私有方法
        print(self.__age)
        print(self.__name)
        self.__f1()
    # a=A()
    # print(a.age)
    #    print(A.__age)

class B:
    a=10
    def __init_(self):
        print(1111111111)
    def f(self):
        print('B123')
    def __f2(self):
        print('B10000')
class C(A,B):
    a1=100
    # def __init__(self):
    #     print(2222222222222)
    def f1(self):
        print('C123')
    def __f21(self):
        print('C10000')

c=C()
c.f1()