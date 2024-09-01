# 4、力法，抽还突的切行世
# --类方法，通过classmethodi声明，默认带一个cLs参数，表示调用方法的类。一般通过类调用，常用于修改类属性的值。
# ---实例方法，类中最常用的方法，默认带一个sLf参数，表示调用方法的对象。一般通过对象调用。
# 静态方法（了解），通过astaticmethod声明，通过类和对象都能调用
# 二、类的声明
# 语法：
# class 类名[（父类1，..）]：
#     语句1
#     。。。。。0
# 类名，必须满足标识符命名规范，通常首字母大写，比如Student
# 三、对象的声明（实例化）
# 。·语法：
# BI II IE
# #声明一个学生类，包含学生的国籍、学号、姓名、班级属性，学习、吃饭方法
# class Student:
#     country='China'#类属性
#     def info(self,no,name,cls):#实例方法
#         self.no= no    #学号，实例属性，声明--se1f,变量名
#         self.name=name #姓名
#         self.cls=cls   #班级
#     def study(self):
#         print(f'{self.name}爱学习，每天学习到12点')
#
#     @classmethod # 装饰器，声明类方法
#     def f1(cls):
#         print('类方法')
#     @staticmethod
#     def f2():
#         print('静态方法')
# class flashing_icon:
#     st1 = Student()#创建对象st1
#     st2 = Student()#创建对象st2
#     print(st1 is st2)
#     print(st1.country,st2.country)#对象访问类属性
#
#     st1.info(1001,'张三','高三五班')#对象访问实例方法
#     st2.info(1002,'李四','高二五班')
#     print(st1.no,st1.name,st1.cls)#对象访问实例属性
#     st1.f1()#对象访问类方法
#     st1.f2()#对象访问静态方法
#     st1.study()
#
#     print('################################')
#     # 修改类属性值
#     Student.country='USA'
#     print(st1.country,st2.country)
#     st2.country='Japan'
#     print(st1.country,st2.country)

# 士兵进行射击训练，统计在1分钟内的射击次数、总成绩（每次射击成绩在8-10环）
# 枪的弹夹容量为10，换弹夹需要3秒
# 每次射击后随机调整1-3秒才能开下一枪
# 枪（属性:名称、子弹数量；方法:开火、装弹）
# 士兵（属性：姓名、射击次数、成绩；方法：开火、装弹）
# 转行相
import random,time
class Gun:
    def __init__(self,name,bullet=10):
        self.name=name
        self.bullet=bullet
    def fire(self):
        if self.bullet>0:
            self.bullet -=1
    def add(self):
        self.bullet=10
class Soldier:
    def __init__(self,name,gun):
        self.name=name
        self.gun=gun
        self.count=0
        self.score=0
    def fire(self):
        if self.gun.bullet>0:
            self.gun.fire()
            self.gun.bullet-=1
            self.count+=1
            result=random.randint(8,10)
            self.score+=result
            print(f'射击次数：{self.count}\t成绩：{result}环')
            time.sleep(random.randint(1,3))
        else:
            self.add()

    def add(self):
        self.gun.add()
        print('更换弹夹中',end='')
        for i in range(10):
            print('.',end='')
            time.sleep(0.3)
        print('')

if __name__ == '__main__':
    gun=Gun('AK47')
    soldier=Soldier('张三',gun)
    start=time.time()
    print('训练开始'.center(30,'*'))
    while time.time()-start <= 30:
        soldier.fire()
    print('训练结束'.center(30,'*'))
    print(f'姓  名: {soldier.name}\n枪  械: {gun.name}\n射  击: {soldier.count}次\n总成绩: {soldier.score}')
