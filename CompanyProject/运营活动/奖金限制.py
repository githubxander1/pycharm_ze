from pprint import pprint

import pymysql
import requests

url='https://qrpromotionapitest.tostar.top/manager/activity/test?activityId=180&uid=17141'
headers={'swagger':'1',
         'token':'0a4b697b631e4de6ab32692f8acd0cd0'}

r=requests.get(url,headers=headers)
print('奖金为：{}'.format(r.json()))

# 查询数据库
db_conn=pymysql.Connect(host='192.168.7.84', port=3306, user='product_statistics', password='OwDXEIs*8eIeED23s', database='product_statistics')
# is_connected=db_conn.ping(reconnect=True)
# if is_connected:
#         print('数据库链接成功')
# else:
#         print('数据库连接失败')
# 创建游标
cursor=db_conn.cursor()

# 执行sql语句
import pandas as pd

sql = "select * from t_user_money where activity_id = 180 and uid = 17141"
# sql2 = "select count(*) from t_user_money where activity_id = 180 and uid = 17141"
cursor.execute(sql)
# cursor.execute(sql2)
result = cursor.fetchall()

df = pd.DataFrame(result, columns=[i[0] for i in cursor.description])
print(df.to_string(index=False, header=True))
print(f"共查询到 {len(df)} 条数据。")

# pprint('查询结果为：{}'.format(result))
