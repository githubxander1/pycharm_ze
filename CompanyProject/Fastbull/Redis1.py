import datetime
import json
# from datetime import datetime
from pprint import pprint

import redis
import numpy as np

# 连接到Redis数据库
r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1)

# 获取前14条数据
data = r.zrevrange('8100_AUDUSD_M15', 1, 14, withscores=True)
pprint(data)
for member, score in data:
    member = json.loads(member)
    open_price = float(member[0])
    close_price = float(member[3])
    higher_price = float(member[1])
    lower_price = float(member[2])
    print(close_price)
    print(open_price)
    print(member)
    score = float(score)
    print(score)
    # time_stamp = datetime.utcfromtimestamp(score).strftime('%Y-%m-%d %H:%M')
    dt_utc = datetime.datetime.fromtimestamp(score)
    time_stamp = dt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
    print(time_stamp)
    # dt_utc = datetime.datetime.fromtimestamp(score)
    # # 添加一个偏移量将UTC转换为北京时间
    # tz_offset = datetime.timezone(datetime.timedelta(hours=8))
    # dt_bj = dt_utc.astimezone(tz_offset)
    # # 修改时间格式，使时区部分有一个空格
    # time_format = '%Y-%m-%d %H:%M:%S %z'
    # time_stamp = dt_bj.strftime(time_format)
    # 输出结果
    # print(time_stamp.replace(':', ' ', 1))
# 计算价格变动
price_changes = []
for i in range(1, len(close_price)):
    price_change = close_price[i] - close_price[i-1]
    price_changes.append(price_change)

# 计算平均涨幅和平均跌幅
positive_changes = [change for change in price_changes if change > 0]
negative_changes = [abs(change) for change in price_changes if change < 0]
average_gain = sum(positive_changes) / len(positive_changes)
average_loss = sum(negative_changes) / len(negative_changes)

# 计算相对强度（RS）
rs = average_gain / average_loss

# 计算RSI值
rsi = (100 - (100 / (1 + rs)))

print("RSI值为：", rsi)