import pymysql


class DBHandler:
    def __init__(self, host, port, user, password,
                 database, charset, **kwargs):
        # 连接数据库服务器
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password,
                                    database=database, cursorclass=pymysql.cursors.DictCursor,
                                    charset=charset, **kwargs)
        # 获取游标
        self.cursor = self.conn.cursor()

    def query(self, sql, args=None, one=True):
        self.cursor.execute(sql, args)
        # 提交事务
        self.conn.commit()
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    db = DBHandler(host='192.168.7.84', port=3306,
                   user='fxchat_user', password='123456',
                   database='fxchat_test', charset='utf8')
    sql = 'select * from user_base limit 实例25_批量生成PPT版荣誉证书;'
    data = db.query(sql)
    print(data)