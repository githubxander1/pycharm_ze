import pymysql

# 连接 Mysql 服务器
conn = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='dbname')

# 游标 （具体操作数据库的对象）
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行 SQL 语句
cursor.execute('insert into tbname(name, age) values(%s, %s)', ('张三', 18))
cursor.execute('update tbname set age=%s where name=%s', (19, '张三'))
cursor.execute('delete from tbname where name=%s', ('张三', ))

cursor.execute('select * from tbname') # 获取数据到缓冲区
cursor.fetchone() # 从缓冲区获取一条数据
cursor.fetchmany(3) # 指定获取几条数据
cursor.fetchall() # 获取所有数据


# 提交事务
conn.commit()

# 回滚事务
conn.rollback()

# cursor.rowcount()
# cursor.lastrowid()
# 销毁游标
cursor.close()

# 断开服务器链接
conn.close()