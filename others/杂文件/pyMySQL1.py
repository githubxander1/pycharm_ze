import pymysql

# 1链接数据库
conn = pymysql.connect(
    host="192.168.7.84",
    port=3306,
    user="fxchat_user",
    password="123456",
    db="fxchat_test"
)

# 2创建游标
cur = conn.cursor()

# 3数据库操作
sql = "select userId,nickname from user_base limit 10"
result = cur.execute(sql)
print(result)
print(cur.fetchmany(5))

# 4关闭游标,
# cur.close()
# 5关闭链接
# conn.close()
