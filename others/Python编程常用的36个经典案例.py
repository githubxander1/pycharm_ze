# https://mp.weixin.qq.com/s/nSWMfNUNRsd8rDM-W-fCTA
# 列表推导式：
fizz_buzz_list = [
    "FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)
]
print(fizz_buzz_list)

# 2. 使用with语句和csv模块读取CSV文件
import csv

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# 3.正则表达式查找字符串
import re
pattern = r"[a-zA-Z]+"  #使用正则表达式匹配一个或多个字母（大小写均可）
matches = re.findall(pattern, "Hello World!")
print(f'正则表达式:{matches}')

# 4. 计算字符串中某个字符的数量
string = "Hello World!"
count = string.count("l")
print(f'计数：{count}')

# 5. 使用set进行去重
string = "Hello World!"
unique_chars = set(string)
print(f'去重:{unique_chars}')

# 6. 使用format()格式化字符串
name = "John"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(f'格式化:{message}')

# 7. 使用lambda函数创建匿名函数
add = lambda x, y: x + y
result = add(2, 3)
print(f'匿名函数:{result}')

# 7. 实现一个简单的缓存装饰器
def cache(func):
    cache_dict = {}
    def wrapper(num):
        if num in cache_dict:
            return cache_dict[num]
        else:
            val = func(num)
            cache_dict[num] = val
            return val
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

# 8. 使用try-except-else-finally处理异常
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("No exception occurred")
finally:
    print("Finally block executed")

# 9. 断言（assertion）的使用
assert 2 + 2 == 4, "2 + 2 should be 4"

# 10. 路径操作
import os
current_dir = os.getcwd()
dirname = os.path.dirname(__file__)
print(f'当前文件名:{dirname}')
print(f'路径操作:{current_dir}')

# 11. 环境变量的读取和设置
import os
#设置环境变量
os.environ["MY_ENV_VAR"] = "Hello World!"
print(f'环境变量:{os.environ["MY_ENV_VAR"]}')

# 12. 使用itertools模块 创建迭代器的函数
import itertools
for i in itertools.count(1):
    print(i)
    if i >= 5:
        break

# 13. 日期时间计算和操作
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(f'日期时间计算和操作:{tomorrow}')

# 14. 排序和反序列表
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_lst = sorted(lst)
reversed_lst = sorted(lst, reverse=True)
# reversed_lst = list(reversed(lst))
print(f'排序列表:{sorted_lst}, 倒序列表:{reversed_lst}')

# 15. 使用json模块处理JSON数据
import json
json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print(f'处理JSON数据:{data}')

# 16. 使用collections模块的defaultdict:defaultdict 是字典的一个子类，它提供了一个默认值，用于字典中尝试访问不存在的键
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
print(f'使用collections模块的defaultdict:{d}')

# 17. 使用functools模块的reduce函数:reduce 函数可以将一个二元函数累积地应用到一个序列的元素上，从左到右，以便将序列减少为单个值
from functools import reduce
lst = [1, 2, 3, 4, 5]
sum_of_lst = reduce(lambda x, y: x + y, lst)
print(f'使用functools模块的reduce函数:{sum_of_lst}')

# 18. 使用threading模块进行简单的多线程编程
import threading
def print_numbers():
    for i in range(1, 6):
        print(i)
        # threading.sleep(1)
        thread = threading.Thread(target=print_numbers)
        thread.start()
        thread.join()
        print("Done!")

# 19. 使用multiprocessing模块进行多进程编程
from multiprocessing import Process,cpu_count
def print_numbers1():
    for i in range(1, 6):
        print(i)
        process = Process(target=print_numbers1)
        process.start()

# 20. 使用requests模块进行HTTP请求
import requests
response = requests.get("https://www.example.com")
print(f'使用requests模块进行HTTP请求:{response.status_code}')

# 21. 使用matplotlib模块进行简单的绘图
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# plt.plot(x, y)
# plt.show()

# 22. 使用pandas模块进行数据处理
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(f'使用pandas模块进行数据处理:{df}')

# 21. 使用map()函数将字符串转换为整数列表:map() 函数可以对一个序列的每个元素应用指定的函数
string_list = ["1", "2", "3"]
int_list = list(map(int, string_list))
print(f'使用map()函数将字符串转换为整数列表:{int_list}')

# 22. 条件语句
if 2 > 1:
    print("2 is greater than 1")
elif 2 == 1:
    print("2 is equal to 1")
else:
    print("2 is less than 1")

# 23. for循环遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 24. while循环
count = 0
while count < 5:
    print(count)
    count += 1

# 25. 使用enumerate()获取列表的索引和值
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")

# 26. 列表切片
sliced_list = fruits[1:3]
print(f'列表切片:{sliced_list}')

# 27. 字符串格式化
name = "John"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(f'字符串格式化:{message}')

# 28. 异常处理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# 29. 类定义
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# 30. 集合并集
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f'集合并集:{union_set}')
print(set1 | set2)

# 31. 创建字典
dictionary = {"name": "John", "age": 25}
print(f'创建字典:{dictionary}')


# 32. 访问字典值
name = dictionary["name"]
print(f'访问字典值:{name}')

# 33. 删除字典元素
dictionary1 = {"name": "John", "age": 25}
del dictionary1["age"]
print(f'删除字典元素:{dictionary1}')

# 34. 生成器函数
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        for i in fibonacci_generator():
            print(i)

# 35. 使用zip()同时遍历多个列表
names = ["John", "Jane", "Jim"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")