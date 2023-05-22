import pymysql

# 连接数据库
db = pymysql.connect(host='192.168.7.84', port=3306, user='product_statistics', password='OwDXEIs*8eIeED23s', database='product_statistics')
# db = pymysql.connect(host='192.168.7.84', port=3306, user='fxchat_user', password='123456', database='fxchat_test')

# 测试连接是否成功
is_connected = db.ping(reconnect=True)
print(is_connected)

# 打印测试结果
if is_connected:
    print("数据库连接成功")
else:
    print("数据库连接失败")
# 创建游标对象
cursor = db.cursor()

# 执行SQL语句
sql = "SELECT COUNT(*) FROM t_activity_bill WHERE user_id=17141 AND device_id='3d18321ba7e437baaae5245e3f02be3d' AND activity_id=180;"
cursor.execute(sql)

# 获取查询结果
result = cursor.fetchone()[0]

# 打印查询结果
print("查询结果为：{} 条数据".format(result))

# 关闭游标对象和数据库连接
# cursor.close()
# db.close()