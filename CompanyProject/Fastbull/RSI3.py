import redis
import json
import datetime
import numpy as np

# 连接Redis
r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1)

# 获取前14条数据
data = r.zrevrange('8100_AUDUSD_M15', 1, 14, withscores=True)

# 初始化变量
close_prices = []
for member, score in data:
    member = json.loads(member)
    close_prices.append(float(member[3]))

# 确保我们有足够的收盘价格数据来计算RSI
if len(close_prices) < 14:
    print("需要更多数据来计算RSI")
else:
    # 计算RSI
    gains = np.diff(close_prices)
    avg_gain = gains.mean()
    avg_loss = -np.diff(close_prices[::-1]).mean()
    RS = avg_gain / avg_loss
    RSI = 100 - (100 / (1 + RS))

    print(f"RSI: {RSI}")