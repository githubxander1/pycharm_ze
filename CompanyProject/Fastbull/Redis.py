import json

import redis
import pandas as pd
from datetime import datetime

# 连接到Redis数据库
r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1)

# 获取前14条数据
data = r.zrange('8100_AUDUSD_D1', 1, 14, withscores=True)
print(data)

# 定义时间戳转换函数
def timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M')


# 初始化DataFrame
df = pd.DataFrame(columns=['序号', '真实时间', '开盘价', '最高价', '最低价', '收盘价'])

# 遍历数据并处理每项
for i, (member_json_str, score) in enumerate(data, 1):
    # 将JSON字符串解析为Python对象
    member_dict = json.loads(member_json_str)

    # 从字典中提取所需的数据
    open_price = member_dict[0]
    high_price = member_dict[1]
    low_price = member_dict[2]
    close_price = member_dict[3]

    # 转换时间戳为日期
    real_time = timestamp_to_datetime(score)

    # 添加数据到DataFrame
    row = {'序号': i, '真实时间': real_time, '开盘价': open_price, '最高价': high_price,
           '最低价': low_price, '收盘价': close_price}
    df = df.append(row, ignore_index=True)

# 打印DataFrame
print(df)