import redis
import pandas as pd
import json
import pytz

# 连接到Redis数据库
r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1)

# 获取所有数据（确保有足够的数据点计算RSI）
data = r.zrevrange('8100_AUDUSD_M15', 1, 15, withscores=True)

# 提取数据并转换为DataFrame
df = pd.DataFrame([(json.loads(member), int(score)) for member, score in data],
                   columns=['data', 'timestamp'])

# 转换时间戳为东八区时间
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s').dt.tz_localize(pytz.utc).dt.tz_convert('Asia/Shanghai')
df.set_index('timestamp', inplace=True)
df.index.name = None

# 提取收盘价
df['close_price'] = df['data'].apply(lambda x: float(x[3]))

# 计算涨跌值 (change)
df['change'] = df['close_price'].pct_change()

# 初始化平均涨跌值（填充前13个NaN值，以便后续计算RSI）
df['avg_gain'] = df['change'].where(df['change'] > 0).rolling(window=14, min_periods=1).mean().fillna(method='ffill').shift()
df['avg_loss'] = df['change'].where(df['change'] < 0).abs().rolling(window=14, min_periods=1).mean().fillna(method='ffill').shift()

# 计算RSI
df['rsi'] = 100 - (100 / (1 + df['avg_gain'] / df['avg_loss']))

# 显示包含收盘价与RSI以及具体时间的数据（去除初始的NaN值）
df = df.dropna(subset=['rsi'])
print(df[['close_price', 'rsi']])