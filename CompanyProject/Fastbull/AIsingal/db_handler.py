import pymysql
import yaml
from pymysql.cursors import DictCursor




class DBHandler:
    def __init__(self,host,port, user,
                               password, charset, database=None,
                               cursorclass=DictCursor,**kw):#**kw支持其他参数这里没传进来
        '''初始化'''
        self.conn = pymysql.connect(host=host, port=port, user=user,
                               password=password, charset=charset, database=database,
                               cursorclass=cursorclass,**kw)
        self.cursor = self.conn.cursor()#新建游标

    def query(self,sql,args=None,one=True):
        '''查询语句'''
        self.cursor.execute(sql,args)
        #TODD：提交事务
        self.conn.commit()#提交之后再查询就是最新数据
        #获取结果
        if one:
            return self.cursor.fetchone()#fetch获取结果
        else:
            return self.cursor.fetchall()#
    def close(self):
        self.cursor.close()
        self.conn.close()
if __name__ == '__main__':
    f = open('config.yaml', encoding='utf-8')

    yaml_data = yaml.load(f, Loader=yaml.FullLoader)  # 读取yaml
    db = DBHandler(host=yaml_data['database']['host'], port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'], password=yaml_data['database']['password'],
                   charset=yaml_data['database']['charset'], database=yaml_data['database']['database'])
    # 第二部分
    # 图表 - 开仓信号数量
    sql_opentime_signal_count = """
        select count(*) from strategy_signal where openTime>=1693497600000  and openTime< 1696089600000 and status =1 
        """
    # 图表 - 平仓信号数量
    sql_closetime_signal_count = """
        select count(*) from strategy_signal where closetime>=1693497600000  and closetime< 1696089600000 and status =1 and positionType =2
        """
    # 图表 - 平仓盈亏点数
    sql_profit_signal_count = """
        select sum(profitLoss) from strategy_signal where closetime>=1693497600000  and closetime< 1696089600000 and status =1 and positionType =2
            """
    # 平均每周信号数量
    # 平均每周盈亏

    result1 = db.query(sql_opentime_signal_count, one=False)
    result2 = db.query(sql_closetime_signal_count, one=False)
    result3 = db.query(sql_profit_signal_count, one=False)

    print("开仓信号数量:", result1)
    print("平仓信号数量:", result2)
    print("平仓盈亏点数:", result3)
    print(result1[0]["count(*)"])
    print(result2[0]["count(*)"])
    print(result3[0]["sum(profitLoss)"])