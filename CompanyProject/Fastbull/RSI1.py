import csv

import pandas as pd
import redis
import json
from datetime import datetime, timedelta
import pytz
import numpy as np

# 为Redis连接设置超时时间以防止阻塞
r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1, socket_timeout=5)

# 获取最近15条数据的分数（假设是Unix时间戳）和成员
data = r.zrevrange('8100_AUDUSD_D1', start=1, end=50, withscores=True)
# 定义转换函数，将时间戳转换为东八区的具体时间
def timestamp_to_eastern_timezone(timestamp):
    utc_time = datetime.utcfromtimestamp(timestamp)
    # 假设始终是8小时的偏移量，无需考虑夏令时
    eastern_offset = timedelta(hours=8)
    eastern_time = utc_time + eastern_offset
    return eastern_time.strftime('%Y-%m-%d %H:%M:%S')

# 使用列表推导式代替for循环提高性能
prices = [
    {**{'Index': i+1},  # 开始从1计数
     'Time': timestamp_to_eastern_timezone(int(score)),
     'Open': float(json.loads(member.decode())[0]),
     'High': float(json.loads(member.decode())[1]),
     'Low': float(json.loads(member.decode())[2]),
     'Close': float(json.loads(member.decode())[3])}
    for i, (member, score) in enumerate(data)
]


# 将数据导出到CSV文件
# with open('audusd_m15_data.xlsx', 'w', newline='') as csvfile:
#     fieldnames = ['Time', 'Open', 'High', 'Low', 'Close']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for price_dict in prices:
#         writer.writerow(price_dict)
# 创建DataFrame
df = pd.DataFrame(prices)
# df.to_excel('audusd_m15_data.xlsx', index=False)
# 打印表格
print(df.to_string(index=False))

# 计算RSI
def calculate_rsi(close_prices, period=14):
    if len(close_prices) < period:
        return np.nan
    gains = close_prices.diff().dropna()
    losses = -gains
    avg_gain = gains.rolling(window=period).mean()
    avg_loss = losses.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]
rsi_value = calculate_rsi(df['Close'], period=14)
print(f"RSI (周期14): {rsi_value}")
# 计算SMA
def calculate_sma(close_prices, period):
    return close_prices.rolling(window=period).mean().iloc[-1]
sma_value = calculate_sma(df['Close'], period=50)
print(f"SMA (10): {sma_value}")
# print(sum(df['Close'])/len(df))


# 计算RSI
def calculate_rsi(series, period):
    # 计算价格变化
    delta = series.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    # 计算平均增益和平均损失
    avg_up = up.rolling(window=period).mean()
    avg_down = down.abs().rolling(window=period).mean()
    # print(avg_up, avg_down)

    # 计算RSI
    rsi = 100.0 - (100.0 / (1.0 + avg_up / avg_down))
    # print(rsi)
    return rsi

# 计算SMA
def calculate_sma(series, period):
    return series.rolling(window=period).mean()

#
# # 计算MACD
# def calculate_macd(series, short_period, long_period, signal_period):
#     ema_short = series.ewm(span=short_period, adjust=False).mean()
#     ema_long = series.ewm(span=long_period, adjust=False).mean()
#     macd_line, signal_line = ema_short - ema_long, ema_long.ewm(span=signal_period, adjust=False).mean()
#     return macd_line, signal_line
#
# # 计算ADX
# def calculate_adx(high, low, close, period):
#     tr = pd.concat([high - low, abs(high - close), abs(low - close)], axis=1).max(axis=1)
#     dx = 100 * (tr.rolling(window=period).mean() / tr.ewm(span=period, alpha=0.5).mean() - 50)
#     adx = dx.rolling(window=period).mean()
#     return adx
#
# # 假设 prices 是一个DataFrame，包含 'Close', 'High', 'Low' 列
# # 计算指标
# df['RSI'] = calculate_rsi(df['Close'], 14)
# df['SMA_5'] = calculate_sma(df['Close'], 5)
# df['SMA_10'] = calculate_sma(df['Close'], 10)
# df['SMA_20'] = calculate_sma(df['Close'], 20)
# df['SMA_50'] = calculate_sma(df['Close'], 50)
# df['SMA_100'] = calculate_sma(df['Close'], 100)
# df['SMA_200'] = calculate_sma(df['Close'], 200)
#
# macd_line, signal_line = calculate_macd(df['Close'], 12, 26, 9)
#
# df['MACD'], df['Signal'] = calculate_macd(df['Close'], 12, 26, 9)
# print(f'MACD:{macd_line}, SIN:{signal_line}')
#
# # 打印 SMA 各个周期列
# # print(df[['SMA_5', 'SMA_10', 'SMA_20', 'SMA_50', 'SMA_100', 'SMA_200']])
# #
# # # 打印 MACD 和 Signal 列
# # print(df[['MACD', 'Signal']])
#
# # 打印 RSI 列
# print(df['RSI'])
# print(df['SMA_5'])
#
#
#
# # df['MACD'] = macd_line[-1]
# # df['MACD_Signal'] = signal_line[-1]
#
# # adx = calculate_adx(df['High'], df['Low'], df['Close'], 14)
# # df['ADX'] = adx[-1]
#
# # 显示结果
# # print(prices.tail())
# # 计算最高价和最低价的前14周期滚动最大最小值
# df['HHV_14'] = df['High'].rolling(window=14).max()
# df['LLV_14'] = df['Low'].rolling(window=14).min()
#
# # 计算K值
# df['K'] = ((df['Close'] - df['LLV_14']) / (df['HHV_14'] - df['LLV_14'])) * 100
#
# # 计算D值，这里假设使用3期简单移动平均
# df['D'] = df['K'].rolling(window=3).mean()
#
# # 移除计算过程中产生的NaN（在窗口期内无法计算）
# df = df.dropna(subset=['K', 'D'])
#
# print(df[["K", "D"]])