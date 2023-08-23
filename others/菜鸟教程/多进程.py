from multiprocessing import Process
from time import sleep


# 多任务
def AB(word):
    while True:
        sleep(1)
        print(word)


# 定义任务
task1 = Process(target=AB, args=('第一'))
task2 = Process(target=AB, args=('第二'))
# task3 = Process(target=AB, args=('第三'))

# 启动任务
task1.start()
# task1.join() #同步|等待A任务执行完毕后B任务才执行
task2.start()
# task3.start()


# # 结束某个任务
# task1.terminate()
# task2.terminate()