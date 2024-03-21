import json
import datetime
from pprint import pprint

import numpy as np
import redis

r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1)

# 获取前14条数据
data = r.zrevrange('8100_AUDUSD_M15', 1, 14, withscores=True)
pprint(data)
prices = []
for member, score in data:
    member = json.loads(member)
    close_price = float(member[3])
    prices.append(close_price)

# 计算价格变动
price_changes = np.diff(prices)

# 计算平均涨幅和平均跌幅
up = price_changes.copy()
down = price_changes.copy()
up[up < 0] = 0
down[down > 0] = 0
average_gain = np.mean(up)
average_loss = np.abs(np.mean(down))

# 计算RSI
rsi = 100 - (100 / (1 + average_gain / average_loss))
print("RSI:", rsi)