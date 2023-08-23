import threading

def thread_1():
    print(threading.currentThread().name)

def thread_2():
    print(threading.currentThread().name)


# 定义任务
t1=threading.Thread(target=thread_1,args=(),name="进程1")
t2=threading.Thread(target=thread_2,args=(),name="进程2")


# 启动任务
print("主线程开始:"+threading.currentThread().name)
t1.start()
t2.start()