import json
import redis
from datetime import datetime, timedelta
import pandas as pd
import pandas_ta as ta  # 假设已安装pandas_ta库

# 已连接数据库
r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1, socket_timeout=5)

# 获取最近15条数据
data = r.zrevrange('8100_AUDUSD_M15', start=1, end=14, withscores=True)
def timestamp_to_eastern_timezone(timestamp):
    utc_time = datetime.utcfromtimestamp(timestamp)
    # 假设始终是8小时的偏移量，无需考虑夏令时
    eastern_offset = timedelta(hours=8)
    eastern_time = utc_time + eastern_offset
    return eastern_time.strftime('%Y-%m-%d %H:%M:%S')
# 转换为DataFrame
df = pd.DataFrame([
    {'Time': timestamp_to_eastern_timezone(int(score)),
     'Open': float(json.loads(member)[0]),
     'High': float(json.loads(member)[1]),
     'Low': float(json.loads(member)[2]),
     'Close': float(json.loads(member)[3])}
    for member, score in data
])

# 将Time列转换为datetime类型
df['Time'] = pd.to_datetime(df['Time'])

# 设置时间列作为索引
df.set_index('Time', inplace=True)

# 计算技术指标
df['RSI'] = ta.rsi(df['Close'], length=14)  # 相对强弱指标
print(df['RSI'])
df['K'], df['D'] = ta.stoch(df['High'], df['Low'], df['Close'], k=9, d=3)  # KD随机指标(K,D)
df['StochRSIK'], df['StochRSID'] = ta.stochrsi(df['Close'], length=14)  # 随机RSI(K,D)
# df['MACD'], df['MACDSignal'], df['MACDHist'] = ta.macd(df['Close'], fast=12, slow=26, signal=9)  # MACD及其信号线
# df['ADX'] = ta.adx(df['High'], df['Low'], df['Close'], length=14)  # 平均趋向指标

# 计算简单移动平均线
for period in [5, 10, 20, 50, 100, 200]:
    df[f'SMA_{period}'] = ta.sma(df['Close'], length=period)  # 简单移动平均线

# 输出结果
# print(df.to_string(index=False))