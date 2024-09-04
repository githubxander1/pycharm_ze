import pandas as pd

# 读取Excel文件
file_path = '考勤表.xlsx'
df = pd.read_excel(file_path)

# 定义一个函数来处理日期和时间
def process_datetime(time_str, date_str, is_next_day):
    if pd.isnull(time_str) or pd.isnull(date_str):
        return pd.NaT

    # 将日期字符串转换为日期对象
    date_obj = pd.to_datetime(date_str, format='%d-%m-%y')

    if is_next_day:
        # 处理次日情况，即加班到第二天
        time_part = time_str.replace('次日', '')
        # 将次日的时间转换为timedelta
        time_delta = pd.to_timedelta(time_part)
        # 计算加班到第二天的时间
        next_day_time = date_obj + pd.Timedelta(days=1) + time_delta
    else:
        # 处理正常打卡时间
        time_delta = pd.to_timedelta(time_str)
        next_day_time = date_obj + time_delta

    return next_day_time

# 定义一个函数来解析日期和星期
def parse_date_and_weekday(date_str):
    # 拆分日期和星期
    if pd.notnull(date_str) and '星期' in date_str:
        date_part, weekday_part = date_str.split('星期')
        return date_part.strip(), weekday_part.strip()
    return date_str, None

# 预处理日期列
df['日期'], df['星期'] = zip(*df['日期'].apply(parse_date_and_weekday))

# 应用函数处理上班和下班时间
df['上班1打卡时间'] = df.apply(lambda row: process_datetime(row['上班1打卡时间'], row['日期'], False), axis=1)
df['下班1打卡时间'] = df.apply(lambda row: process_datetime(row['下班1打卡时间'], row['日期'], '次日' in row['下班1打卡时间']), axis=1)

# 定义一个函数来计算工作时长和加班时长
def calculate_hours(row):
    if pd.isnull(row['上班1打卡时间']) or pd.isnull(row['下班1打卡时间']):
        return 0, 0, 0  # 如果时间数据无效，返回0

    # 计算工作时长（小时）
    work_duration = (row['下班1打卡时间'] - row['上班1打卡时间']).total_seconds() / 3600
    work_duration_hours = round(work_duration)

    # 检查是否是周末
    if '六' in row['星期'] or '日' in row['星期']:
        # 周末加班，减去1.5小时午休
        adjusted_duration = max(work_duration_hours - 1.5, 0)
    else:
        # 工作日加班，减去1小时晚餐时间
        adjusted_duration = max(work_duration_hours - 1, 0)

    # 计算餐补和交补
    meal_subsidy = 1 if adjusted_duration >= 10 else 0
    transport_subsidy = 1 if adjusted_duration >= 11 else 0

    return adjusted_duration, meal_subsidy, transport_subsidy

# 应用函数计算工作时长和补贴
df[['加班时长', '工作小时大于等于10h，餐补1次', '工作小时大于等于11h，交补1次']] = df.apply(calculate_hours, axis=1, result_type='expand')

# 保存结果到新的Excel文件
output_path = '考勤表_计算结果.xlsx'
df.to_excel(output_path, index=False)

print("计算完成，结果已保存到", output_path)