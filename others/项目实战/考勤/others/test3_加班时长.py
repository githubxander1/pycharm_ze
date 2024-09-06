import pandas as pd
from datetime import datetime, timedelta

# 读取Excel文件
df = pd.read_excel('考勤表.xlsx')

# 分割日期和星期
date_parts = df['日期'].str.split(' ', expand=True)
df['日期'] = pd.to_datetime(date_parts[0], format='%y-%m-%d').dt.date  # 转换为日期格式
df['星期'] = date_parts[1].str.strip()  # 移除可能的前后空格

# 将星期列放到日期列后面
cols = df.columns.tolist()
cols = cols[0:2] + ['星期'] + cols[3:]
df = df[cols]


# 处理“次日”情况
def process_next_day(time_str):
    if '次日' in str(time_str):
        return str(time_str).split('次日')[1].strip(), '是'
    return str(time_str), '否'


# 应用处理函数并拆分结果
df['处理后下班时间'], df['是否次日'] = zip(*df['下班1打卡时间'].apply(lambda x: process_next_day(x)))

# 定义工作日的上下班时间和休息时间
work_start = datetime.strptime('08:30', '%H:%M').time()
work_end = datetime.strptime('18:00', '%H:%M').time()
lunch_start = datetime.strptime('12:00', '%H:%M').time()
lunch_end = datetime.strptime('13:30', '%H:%M').time()
evening_start = datetime.strptime('18:00', '%H:%M').time()
evening_end = datetime.strptime('19:00', '%H:%M').time()

# 转换打卡时间格式
df['上班1打卡时间'] = pd.to_datetime(df['上班1打卡时间'], format='%H:%M', errors='coerce').dt.time
df.loc[df['是否次日'] == '是', '下班1打卡时间'] = pd.to_datetime(df.loc[df['是否次日'] == '是', '处理后下班时间'],
                                                                 format='%H:%M', errors='coerce').dt.time
df.loc[df['是否次日'] == '否', '下班1打卡时间'] = pd.to_datetime(df.loc[df['是否次日'] == '否', '下班1打卡时间'],
                                                                 format='%H:%M', errors='coerce').dt.time


# 计算工作时长、加班时长
def calculate_hours(row):
    start = row['上班1打卡时间']
    end = row['下班1打卡时间']
    date = row['日期']
    if pd.isnull(start) or pd.isnull(end):
        return '0:00', 0  # 工作时长, 加班时长

    start_dt = datetime.combine(date, start)
    if row['是否次日'] == '是':
        end_dt = datetime.combine(date + timedelta(days=1), end)
    else:
        end_dt = datetime.combine(date, end)

    work_duration = (end_dt - start_dt).total_seconds() / 3600

    # 计算午休时间
    lunch_duration = 0
    if start < lunch_start and end > lunch_end:
        lunch_duration = (datetime.combine(date, lunch_end) - datetime.combine(date,
                                                                               lunch_start)).total_seconds() / 3600
    elif start < lunch_start and end < lunch_end:
        lunch_duration = (datetime.combine(date, end) - datetime.combine(date, lunch_start)).total_seconds() / 3600
    elif start >= lunch_start and end > lunch_end:
        lunch_duration = (datetime.combine(date, lunch_end) - datetime.combine(date, start)).total_seconds() / 3600

    # 计算晚上休息时间
    evening_duration = 0
    if start < evening_start and end > evening_end:
        evening_duration = (datetime.combine(date, evening_end) - datetime.combine(date,
                                                                                   evening_start)).total_seconds() / 3600
    elif start < evening_start and end < evening_end:
        evening_duration = (datetime.combine(date, end) - datetime.combine(date, evening_start)).total_seconds() / 3600
    elif start >= evening_start and end > evening_end:
        evening_duration = (datetime.combine(date, evening_end) - datetime.combine(date, start)).total_seconds() / 3600

    # 调整工作时长
    adjusted_work_duration = max(0, work_duration - lunch_duration - evening_duration)

    # 计算加班时长
    overtime = max(0, adjusted_work_duration - 8)

    return f'{int(adjusted_work_duration)}:{int((adjusted_work_duration % 1) * 60):02d}', overtime


df['工作时长'], df['加班时长'] = zip(*df.apply(calculate_hours, axis=1))

# 计算餐补和交补次数
df['工作小时大于等于10h，餐补1次'] = df['工作时长'].apply(lambda x: 1 if int(x.split(':')[0]) >= 10 else 0)
df['工作小时大于等于11h，交补1次'] = df['工作时长'].apply(lambda x: 1 if int(x.split(':')[0]) >= 11 else 0)

# 保存结果到新的Excel文件
df.to_excel('考勤表_处理后.xlsx', index=False)

print("处理完成，结果已保存到 '考勤表_处理后.xlsx'")