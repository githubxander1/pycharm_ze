# -*-coding: utf-8 -*-
# @Time    : 2023/9/8 10:17
# @Author  : chengjianbo
# @File    : base.py
# @Software: PyCharm
import datetime


def get_time_day():
    # 获取当前日期和时间
    now = datetime.datetime.now()

    # 获取昨日的日期
    yesterday = now - datetime.timedelta(days=1)
    yesterday_start = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0, 0)
    yesterday_timestamp = int(yesterday_start.timestamp()) * 1000

    # 获取当天的日期
    now_start = datetime.datetime(now.year, now.month, now.day, 0, 0, 0, 0)
    now_timestamp = int(now_start.timestamp()) * 1000

    # 获取上周的起始日期
    last_week_start = now - datetime.timedelta(days=now.weekday() + 7)
    last_week_start = datetime.datetime(last_week_start.year, last_week_start.month, last_week_start.day, 0, 0, 0, 0)
    last_week_start_timestamp = int(last_week_start.timestamp()) * 1000

    # 获取上周的结束日期
    last_week_end = now - datetime.timedelta(days=now.weekday() + 1)
    last_week_end = datetime.datetime(last_week_end.year, last_week_end.month, last_week_end.day, 0, 0, 0, 0)
    last_week_end_timestamp = int(last_week_end.timestamp()) * 1000
    # 获取上月的起始日期
    last_month_start = datetime.datetime(now.year, now.month - 1, 1, 0, 0, 0, 0)
    last_month_start_timestamp = int(last_month_start.timestamp()) * 1000
    # 获取当月的起始日期
    last_month_end = datetime.datetime(now.year, now.month, 1, 0, 0, 0, 0)
    last_month_end_timestamp = int(last_month_end.timestamp()) * 1000

    print("昨日和今天的零点毫秒时间戳:", yesterday_timestamp, now_timestamp)
    print("上周的开始和结束零点毫秒时间戳:", last_week_start_timestamp, last_week_end_timestamp)
    print("上月和当月的零点毫秒时间戳:", last_month_start_timestamp, last_month_end_timestamp)
    return [[yesterday_timestamp, now_timestamp], [last_week_start_timestamp, last_week_end_timestamp],
            [last_month_start_timestamp, last_month_end_timestamp]]


def calculate_average(lst):#信号统计和后台计算调用
    total_sum = sum(lst)  # 计算列表中所有元素的总和
    total_count = len(lst)  # 获取列表中元素的总个数

    if total_count == 0:
        return 0  # 避免除以0的情况，返回0

    average = total_sum / total_count  # 计算平均值
    return average

def time_format(signals, count):
    from datetime import datetime, timedelta
    # 将毫秒级时间戳转换为datetime对象
    for signal in signals:
        signal['openTime'] = datetime.fromtimestamp(signal['openTime'] / 1000)
        signal['closeTime'] = datetime.fromtimestamp(signal['closeTime'] / 1000)

    # 计算每个信号的持仓时间并计算平均持仓时间
    total_hold_time = timedelta()
    for signal in signals:
        hold_time = signal['closeTime'] - signal['openTime']
        total_hold_time += hold_time

    average_hold_time = total_hold_time / count
    # print(average_hold_time.seconds)
    # formatted_time = f"{average_hold_time.seconds}秒"
    # print('秒',formatted_time)
    # print("12312312    {} 分钟".format(average_hold_time.seconds // 60))
    # print("12312312    {:.0f} 分钟".format(average_hold_time.seconds // 60))
    # 根据平均持仓时间的不同范围设置不同的格式
    if average_hold_time < timedelta(seconds=60):
        formatted_time = f"{average_hold_time.seconds}秒"
    elif average_hold_time < timedelta(minutes=60):
        formatted_time = f"{average_hold_time.seconds // 60}分钟"#这里2.7分钟显示了2分钟，没有四舍五入，后面优化
    elif average_hold_time < timedelta(hours=48):
        formatted_time = f"{average_hold_time.total_seconds() / 3600:.1f} 小时"
    elif average_hold_time < timedelta(days=90):
        formatted_time = f"{average_hold_time.total_seconds() / 86400:.1f} 天"
    elif average_hold_time < timedelta(days=365 * 2):
        formatted_time = f"{average_hold_time.days / 30:.1f} 个月"
    else:
        formatted_time = f"{average_hold_time.days / 365:.1f} 年"

    print(f"平均持仓时间为：{formatted_time}")
if __name__ == '__main__':
    get_time_day()