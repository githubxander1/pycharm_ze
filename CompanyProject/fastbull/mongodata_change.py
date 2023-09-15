# -*-coding: utf-8 -*-
# @Time    : 2023/8/10 10:37
# @Author  : chengjianbo
# @File    : mongodata_change.py
# @Software: PyCharm
# 连接到 MongoDB
import pandas as pd
import pymongo

def get_mongo_data(type,table_name, cb:list):#cb:list,要删除的列因为涉及到文档和表的转换

    if type == "test":
        client = pymongo.MongoClient('mongodb://fastbull:IOE*2EW#OIWddOPcDWE@192.168.7.72:27017/fastbull_macro_data_test?authSource=admin')#测试
        db = client['fastbull_macro_data_test']
    else:
        client = pymongo.MongoClient('mongodb://fastbull_macro_data_preprod_user:QSKzvWi8gCvfZ4z*@192.168.7.105:27017/fastbull_macro_data_preprod?authSource=admin')#预发布
        db = client['fastbull_macro_data_preprod']
    # 选择数据库和集合
    collection = db[table_name]
    # 查询所有文档并转换为列表
    cursor = collection.find({})
    data_list = list(cursor)
    # print(data_list)
    # 将列表转换为 DataFrame
    df = pd.DataFrame(data_list)
    if cb != []:
        column_data_list = df["strategyName"].tolist()
        df1 = pd.DataFrame([item[1]['content'] for item in column_data_list], columns=['strategy_Name'])
        merged_df = pd.merge(df1, df, left_index=True, right_index=True)

        df = merged_df.drop(cb, axis=1)

    return df


if __name__ == '__main__':
    df = get_mongo_data("pre","strategy",[ 'strategyName','guide','strategyIntroduce'])
    print(df)