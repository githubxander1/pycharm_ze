import threading

lock= threading.Lock()

n=0
def run_thread():
    # 锁
    lock.acquire()
    global n
    n += 1
    print(n)
    # 解锁
    lock.release()


t1=threading.Thread(target=run_thread)
t2=threading.Thread(target=run_thread)
t1.start()
t2.start()

# ThreadLocal是一个全局的字典，用每个线程的名称做为key去存储和访问变量，这样每个线程之间的数据就变得独立，互相不受到干扰。
l=threading.local()
def a():
    print(l.name)
def b():
    l.name=1
    a()
p1=threading.Thread(target=b)
p2=threading.Thread(target=b)
p1.start()
p2.start()