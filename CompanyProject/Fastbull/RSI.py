import pandas as pd
import numpy as np
import pandas as pd
import redis
import json
from datetime import datetime, timedelta
# 创建一个示例DataFrame
r = redis.Redis(host='3.71.83.141', port=6379, password='L7lfDSe#OIEWQ*R', db=1, socket_timeout=5)

# 获取最近15条数据的分数（假设是Unix时间戳）和成员
data = r.zrevrange('8100_AUDUSD_M15', start=1, end=15, withscores=True)
# 定义转换函数，将时间戳转换为东八区的具体时间
def timestamp_to_eastern_timezone(timestamp):
    utc_time = datetime.utcfromtimestamp(timestamp)
    # 假设始终是8小时的偏移量，无需考虑夏令时
    eastern_offset = timedelta(hours=8)
    eastern_time = utc_time + eastern_offset
    return eastern_time.strftime('%Y-%m-%d %H:%M:%S')

# 使用列表推导式代替for循环提高性能
prices = [
    {
        'Index': idx + 1,
        'Time': timestamp_to_eastern_timezone(int(score)),
        'Open': float(json.loads(member.decode())[0]),
        'High': float(json.loads(member.decode())[1]),
        'Low': float(json.loads(member.decode())[2]),
        'Close': float(json.loads(member.decode())[3]),
    }
    for idx, (member, score) in enumerate(data, start=0)
]
items=[]
close_prices = []
for item in prices:
    items.append(item['Close'])
    # print(close_price)
# 打印所有提取出的 Close 价格
for close_price in items:
    # close_prices.append(close_price)
    print(close_price)

# 创建DataFrame
df = pd.DataFrame(prices)

# 计算指标
def rsi(close, period=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    print(avg_gain)
    print(avg_loss)
    print(rs)
    return rsi

def stoch(close, low, high, k_period=14, d_period=3):
    lowest_low = low.rolling(window=k_period).min()
    highest_high = high.rolling(window=k_period).max()
    rsv = ((close - lowest_low) / (highest_high - lowest_low)) * 100
    k = rsv.rolling(window=d_period).mean()
    d = k.rolling(window=d_period).mean()
    return k, d

def macd(close, fast_period=12, slow_period=26, signal_period=9):
    fast_ema = close.ewm(span=fast_period, adjust=False).mean()
    slow_ema = close.ewm(span=slow_period, adjust=False).mean()
    macd_line = fast_ema - slow_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    return macd_line, signal_line


def adx(high, low, close, period=14):
    high_series = pd.Series(high)
    low_series = pd.Series(low)
    close_series = pd.Series(close)

    up_moves = high_series.diff()
    down_moves = low_series.diff()

    plus_dm = pd.Series(np.where((up_moves > down_moves) & (up_moves > 0), up_moves, 0))
    minus_dm = pd.Series(np.where((down_moves > up_moves) & (down_moves > 0), down_moves, 0))

    truerange = pd.concat([high_series - low_series,
                           (high_series - close_series.shift(1)).abs(),
                           (low_series - close_series.shift(1)).abs()],
                          axis=1).max(axis=1)
    atr = truerange.rolling(window=period).mean()

    plus_di = 100 * (plus_dm.rolling(window=period).mean() / atr)
    minus_di = 100 * (minus_dm.rolling(window=period).mean() / atr)

    dx = (plus_di + minus_di) / 2
    adx = (dx / (dx.rolling(window=period).mean() + 0.0000001)) * 100

    return adx

def sma(close, period):
    return close.rolling(window=period).mean()
def williams_r(close, period=14):
    highest_high = close.rolling(window=period).max()
    lowest_low = close.rolling(window=period).min()
    wr = -(close - highest_high) / (highest_high - lowest_low) * 100
    return wr.fillna(100)
def cci(high, low, close, period=20):
    tp = (high + low + close) / 3
    atr = (high - low).rolling(window=period).mean()
    cci = (tp - tp.rolling(window=period).mean()) / (0.015 * atr)
    return cci

# 已在adx函数中实现了真实范围（ATR），此处仅作为单独指标输出
def atr(high, low, close, period=14):
    tr = pd.concat([high - low,
                    abs(high - close.shift(1)),
                    abs(low - close.shift(1))],
                   axis=1).max(axis=1)
    return tr.rolling(window=period).mean()

def roc(close, period=14):
    return (close - close.shift(period)) / close.shift(period) * 100



# 计算指标
# df['rsi'] = rsi(df['Close'])
k, d = stoch(df['Close'], df['Low'], df['High'])
df['stoch_k'] = k
df['stoch_d'] = d
macd_line, signal_line = macd(df['Close'])
df['macd'] = macd_line
df['macd_signal'] = signal_line
df['adx'] = adx(df['High'], df['Low'], df['Close'])
for period in [5, 10, 20, 50, 100, 200]:
    df[f'sma_{period}'] = sma(df['Close'], period)

# 添加新高/新低指标
# df['new_high'] = df['High'].rolling(window=period).max() == df['High']
# df['new_low'] = df['Low'].rolling(window=period).min() == df['Low']
df['new_high'] = df['High'].diff().fillna(0) > 0
df['new_low'] = df['Low'].diff().fillna(0) < 0
# 将布尔值转换为整数值
df['new_high'] = df['new_high'].astype(int)
df['new_low'] = df['new_low'].astype(int)


# 计算并添加新的技术指标到DataFrame
df['williams_r'] = williams_r(df['Close'])
df['cci'] = cci(df['High'], df['Low'], df['Close'])
df['atr'] = atr(df['High'], df['Low'], df['Close'])
df['roc'] = roc(df['Close'])

# 计算最高价和最低价的前14周期滚动最大最小值
df['HHV_14'] = df['High'].rolling(window=14).max()
df['LLV_14'] = df['Low'].rolling(window=14).min()

# 计算K值
df['K'] = ((df['Close'] - df['LLV_14']) / (df['HHV_14'] - df['LLV_14'])) * 100

# 计算D值，这里假设使用3期简单移动平均
df['D'] = df['K'].rolling(window=3).mean()

# 移除计算过程中产生的NaN（在窗口期内无法计算）
df = df.dropna(subset=['K', 'D'])

print(df[["K", "D"]])
# 显示结果
print(df.to_string(index=False))

