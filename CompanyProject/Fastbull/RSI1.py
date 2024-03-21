'''RS = average_gain / average_loss
RSI = 100 - (100 / (1 + RS))

其中，
average_gain：过去一段时间内平均收益
average_loss：过去一段时间内平均损失

首次计算时，需要将前14个周期的收益和损失分别求和，然后计算平均值。

以下是修改后的代码示例，用于获取数据并计算RSI（这里假设`change`为当前周期收盘价与上一周期收盘价之差）：

```python'''
import datetime

import redis
import json
# from datetime import datetime, timedelta
import numpy as np

r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1)

# 获取前15条数据（包括最新一个周期的数据以计算变化）
data = r.zrevrange('8100_AUDUSD_M15', 0, 14, withscores=True)

gains = []
losses = []

for i in range(1, len(data)):
    member, score = data[i]
    prev_member, _ = data[i-1]
    member = json.loads(member)
    prev_member = json.loads(prev_member)
    close_price = float(member[3])
    prev_close_price = float(prev_member[3])

    change = close_price - prev_close_price
    if change > 0:
        gains.append(change)
    else:
        losses.append(-change)  # 计算损失时取绝对值

# 初始化平均收益和损失
avg_gain = np.mean(gains[:14]) if gains else 0
avg_loss = np.mean(losses[:14]) if losses else 0

RS = avg_gain / avg_loss if avg_loss != 0 else np.inf
RSI = 100 - (100 / (1 + RS))

print(f"RSI: {RSI:.2f}")

# 输出时间戳
for member, score in data[:14]:
    dt_utc = datetime.datetime.fromtimestamp(score)
    time_stamp = dt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
    print(time_stamp)