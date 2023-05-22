from pprint import pprint

import pymysql
import requests
import pandas as pd

url='https://qrpromotionapitest.tostar.top/manager/activity/test?activityId=180&uid=17141'
headers={'swagger':'1',
         'token':'0a4b697b631e4de6ab32692f8acd0cd0'}

r=requests.get(url,headers=headers)
print('奖金为：{}'.format(r.json()))

# 查询数据库
db_conn=pymysql.Connect(host='192.168.7.84', port=3306, user='product_statistics', password='OwDXEIs*8eIeED23s', database='product_statistics')
cursor=db_conn.cursor()

# 执行sql语句

sql = "select * from t_user_money where activity_id = 180 and uid = 17141"
# sql2 = "select count(*) from t_user_money where activity_id = 180 and uid = 17141"
cursor.execute(sql)
# 获取所有数据
result = cursor.fetchall()
df = pd.DataFrame(result, columns=[i[0] for i in cursor.description])
print(df.to_string(index=False, header=True))
print(f"共查询到 {len(df)} 条数据。")
# 统计money这一列的和
money_sum = df['money'].sum()
print('money列的和为：', money_sum)
# 统计money列值在某区间的占比
# 统计money列值在5-9区间的占比
mask = (df['money'] >= 10) & (df['money'] <= 40)
count = len(df[mask])
total = len(df)
percent = count / total * 100
print(f'money列值在10-40区间个数有：{count}，占比为{percent:.2f}%')
# print(f"money列值在5-9区间的占比为{percent:.2f}%")

