from sqlalchemy import create_engine

# from .mongodata_change import get_mongo_data
from CompanyProject.Fastbull.AIsingal.mongodata_change import get_mongo_data


def Synchronous_Data(type):
    def df_to_sql(df ,engine,table_name):
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    def connect_mysql():
        # 通过修改参数，配置成你自己的 MySQL 连接信息
        db_username = 'root'
        db_password = '123456w'
        db_hostname = '192.168.实例25_批量生成PPT版荣誉证书.58'
        db_database = 'test_db'
        connection_string = f"mysql+pymysql://{db_username}:{db_password}@{db_hostname}/{db_database}"
        return create_engine(connection_string)

    engine = connect_mysql()
    df = get_mongo_data(type,"strategy",['strategyName', 'guide','strategyIntroduce'])

    df1 = get_mongo_data(type,"strategy_signal",[])

    if type == "test":
        table_name = 'strategy'  # 替换为实际的表名
        table_name1 = 'strategy_signal'  # 替换为实际的表名
    else:
        table_name = 'strategy_pre'  # 替换为实际的表名
        table_name1 = 'strategy_signal_pre'  # 替换为实际的表名
    df_to_sql(df,engine,table_name)
    df_to_sql(df1,engine,table_name1)
    print('数据同步成功')
if __name__ == '__main__':
    # Synchronous_Data("pre")
    Synchronous_Data("test")