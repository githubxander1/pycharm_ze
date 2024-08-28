import pandas as pd
import redis
import json
from datetime import datetime, timedelta

r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1, socket_timeout=5)

# 获取最近15条数据的分数（假设是Unix时间戳）和成员
data = r.zrevrange('8100_AUDUSD_D1', start=1, end=14, withscores=True)
# 定义转换函数，将时间戳转换为东八区的具体时间
def timestamp_to_eastern_timezone(timestamp):
    utc_time = datetime.utcfromtimestamp(timestamp)
    # 假设始终是8小时的偏移量，无需考虑夏令时
    eastern_offset = timedelta(hours=8)
    eastern_time = utc_time + eastern_offset
    return eastern_time.strftime('%Y-%m-%d %H:%M:%S')

# 使用列表推导式代替for循环提高性能
prices = [{
           'Time': timestamp_to_eastern_timezone(int(score)),
           'Open': float(json.loads(member)[0]),
           'High': float(json.loads(member)[1]),
           'Low': float(json.loads(member)[2]),
           'Close': float(json.loads(member.decode())[3]),  # 添加.decode()以解码字节串
           'Member': member
           }
            for member, score in data]

# 创建DataFrame
df = pd.DataFrame(prices)
print(df.to_string())
# print(df['Close'])

import numpy as np

# 计算相对强弱指标(RSI)
# def calculate_rsi(data, n=14):
#     delta = np.diff(data)
#     gain = delta * np.where(delta > 0, 1, 0)
#     loss = -delta * np.where(delta < 0, 1, 0)
#     avg_gain = np.convolve(gain, np.ones((n,))/n, mode='valid')
#     avg_loss = np.convolve(loss, np.ones((n,))/n, mode='valid')
#     rs = np.where(avg_loss == 0, 0, avg_gain / avg_loss)
#     rsi = 100.0 - (100.0 / (1.0 + rs))
#     return np.r_[np.zeros(n-1), rsi]
#
# # 计算KD随机指标(K)
# def calculate_kdj_k(data, n_slow=9, n_fast=3):
#     low_n = data['Low'].rolling(window=n_slow).min()
#     high_n = data['High'].rolling(window=n_slow).max()
#     rsv = (data['Close'] - low_n) / (high_n - low_n) * 100
#     k = rsv.ewm(span=n_fast, adjust=False).mean()
#     return k
#
# # 计算KD随机指标(D)
# def calculate_kdj_d(data, n=3):
#     k = calculate_kdj_k(data)
#     d = k.ewm(span=n, adjust=False).mean()
#     return d
#
# # 计算随机RSI(K)
# def calculate_rsi_k(data, n=5):
#     rsi = calculate_rsi(data['Close'], n)
#     rsi_k = rsi.ewm(span=3, adjust=False).mean()
#     return rsi_k
#
# # 计算随机RSI(D)
# def calculate_rsi_d(data, n=3):
#     rsi_k = calculate_rsi_k(data)
#     rsi_d = rsi_k.ewm(span=n, adjust=False).mean()
#     return rsi_d
#
# # 计算异同移动平均线(MACD)
# def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
#     ema_fast = data['Close'].ewm(span=fast_period, adjust=False).mean()
#     ema_slow = data['Close'].ewm(span=slow_period, adjust=False).mean()
#     macd = ema_fast - ema_slow
#     signal = macd.ewm(span=signal_period, adjust=False).mean()
#     return macd, signal, macd - signal
#
# # 计算简单移动平均线(SMA)
# def calculate_sma(data, periods=[5, 10, 20, 50, 100, 200]):
#     for period in periods:
#         sma_name = f"SMA_{period}"
#         data[sma_name] = data['Close'].rolling(window=period).mean()
#     return data
#
# # 在获取并处理Redis数据后
# # ...
# # 将DataFrame应用上述函数
# df = calculate_sma(df)
# df['RSI'] = calculate_rsi(df['Close'])
# df['KDJ_K'] = calculate_kdj_k(df)
# df['KDJ_D'] = calculate_kdj_d(df)
# df['RSI_K'] = calculate_rsi_k(df)
# df['RSI_D'] = calculate_rsi_d(df)
# macd, signal, hist = calculate_macd(df)
# df['MACD'], df['MACD_signal'], df['MACD_hist'] = macd, signal, hist

# 计算相对强弱指标(RSI)
def calculate_rsi(df, n=14):
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    count = len(gain.values if gain.values > 0)
    print(f'涨天数：{count}')
    print(f'涨：{gain}')
    loss = -delta.where(delta < 0, 0)
    print(f'跌：{loss}')
    gain_sum=sum(gain.values)
    print(f'涨和：{gain_sum}')
    a=gain_sum/count
    print(f'a：{a:6f}')
    avg_gain = gain.rolling(n).mean()
    print(f'平均涨：{avg_gain}')
    avg_loss = loss.rolling(n).mean()
    print(f'平均跌：{avg_loss}')
    rs = avg_gain / avg_loss
    print(f'rs：{rs}')
    rsi = 100 - (100 / (1 + rs))
    print(f'rsi：{rsi}')
    df['RSI'] = rsi.fillna(50)

print(calculate_rsi(df))

# 计算简单移动平均线(MA)
sma_periods = [5, 10, 20]
for period in sma_periods:
    df[f'MA_{period}'] = df['Close'].rolling(window=period).mean()

# 计算MACD指标
def calculate_macd(df, n_fast=12, n_slow=26, signal=9):
    ema_fast = df['Close'].ewm(span=n_fast, min_periods=n_fast).mean()
    ema_slow = df['Close'].ewm(span=n_slow, min_periods=n_slow).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    df['MACD'] = macd_line
    df['MACD_Signal'] = signal_line
    df['MACD_Histogram'] = histogram

calculate_macd(df)

# 打印最后一条记录的MACD、MACD_Signal和MACD_Histogram值
last_row = df.iloc[-1]
print(f"最后一条记录的MACD值: {last_row['MACD']}")
print(f"最后一条记录的MACD_Signal值: {last_row['MACD_Signal']}")
print(f"最后一条记录的MACD_Histogram值: {last_row['MACD_Histogram']}")

# 计算威廉指标（WR）
def calculate_williams_r(df, n=14):
    high_n = df['High'].rolling(n).max()
    print(f'最高价：{high_n}')
    low_n = df['Low'].rolling(n).min()
    print(f'最低价：{low_n}')
    wr = -100 * (high_n - df['Close']) / (high_n - low_n)
    print(f'wr：{wr}')
    df['Williams_R'] = wr.replace([-np.inf, np.inf], np.nan).fillna(100)
    # 返回最后一个威廉指标的值
    last_wr_value = df['Williams_R'].iloc[-1]
    return last_wr_value

# 调用函数并打印最后一个威廉指标的值
last_wr = calculate_williams_r(df)
print(f"最后一个威廉指标值: {last_wr}")