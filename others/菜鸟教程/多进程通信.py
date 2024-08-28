import multiprocessing

# var = 0
# def x1():
#     global var
#     var = 实例25_批量生成PPT版荣誉证书
#
# def x2():
#     print(var)
#
# t1=multiprocessing.Process(target=x1)
# t2=multiprocessing.Process(target=x2)
#
# t1.start()
# t1.join()
# t2.start()

# The "freeze_support()" line can be omitted if the program
#         is not going to be frozen to produce an executable.

from multiprocessing import Queue
q=Queue()

# 存数据
def x1():
    q.put(1)
    q.put(2)

# 取数据
def x2():
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    t1=multiprocessing.Process(target=x1)
    t2=multiprocessing.Process(target=x2)

    t1.start()
    t2.start()
# print(q.get())#当没有数据时会阻塞，直到等别的进程存入数据

# # 队列长度
# print(q.qsize())
#
# # 是否空的
# print(q.empty())
#
# # 是否满的
# print(q.full())