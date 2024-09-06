import pandas as pd
from datetime import datetime, timedelta

# 初始化 DataFrame 时指定列的数据类型
data = {
    '姓名': ['肖泽华', '肖泽华', '肖泽华', '肖泽华', '范德萨', '范德萨', '范德萨', '范德萨', '范德萨', '范德萨', '范德萨'],
    '日期': ['24-08-01 星期四', '24-08-02 星期五', '24-08-03 星期六', '24-08-02 星期五', '24-08-16 星期五'],
    '考勤状态': ['早到', '正常', '弹性', '迟到', '早退','上半天', '下半天', '上下晚餐补','上下晚餐交补','上到第二天'],
    '上班1打卡时间': ['08:20','08:30', '08:40', '09:40', '08:30','08:30','13:30','08:30', '08:30','08:53'],
    '下班1打卡时间': ['18:30','18:00', '18:10', '19:10', '17:50','12:00','18:00','20:00', '21:00','次日 00:03'],
    '工作时长': ['0'] * 10,  # 初始化为字符串，确保长度一致
    '加班时间': ['0'] * 10,  # 初始化为字符串，确保长度一致
    '餐补次数': [0] * 10,
    '交补次数': [0] * 10
}
午休时间：12:0-13:30
晚餐时间：18:00-19:00

df = pd.DataFrame(data)

# 定义一个函数来计算工作时长和加班时间
def calculate_time(row):
    # 解析日期
    date_str = row['日期'].split()[0]
    date = datetime.strptime(date_str, '%y-%m-%d')

    # 解析上班打卡时间
    start_punch_str = row['上班1打卡时间']
    start_punch = datetime.strptime(f'{date_str} {start_punch_str}', '%y-%m-%d %H:%M')

    # 解析下班打卡时间
    end_punch_str = row['下班1打卡时间']
    if '次日' in end_punch_str:
        next_day_str = (date + timedelta(days=1)).strftime('%Y-%m-%d')
        end_punch = datetime.strptime(f'{next_day_str} {end_punch_str.split(" ")[1]}', '%Y-%m-%d %H:%M')
    else:
        end_punch = datetime.strptime(f'{date_str} {end_punch_str}', '%y-%m-%d %H:%M')

    # 计算上午工作时长
    morning_start = datetime.strptime(f'{date_str} 08:30', '%y-%m-%d %H:%M')
    morning_end = datetime.strptime(f'{date_str} 12:00', '%y-%m-%d %H:%M')
    morning_duration = min(morning_end, end_punch) - max(morning_start, start_punch)
    morning_hours = morning_duration.total_seconds() / 3600
    morning_duration_formatted = f"{int(morning_hours)}:{int((morning_hours % 1) * 60):02d}"

    # 计算下午开始时间
    afternoon_start = datetime.strptime(f'{date_str} 13:30', '%y-%m-%d %H:%M')

    # 计算满足8小时的工作时长,下午还需要工作时长
    x_hours_to_eight = timedelta(hours=(8 - morning_hours))
    can_punch_out_time = afternoon_start + x_hours_to_eight

    # 计算下午实际工作时长
    afternoon_duration = end_punch - afternoon_start
    afternoon_hours = afternoon_duration.total_seconds() / 3600
    afternoon_duration_formatted = f"{int(afternoon_hours)}:{int((afternoon_hours % 1) * 60):02d}"
    print('下午工作时长:', afternoon_hours)

    # 调试输出
    print(f"可以打下班卡的时间: {can_punch_out_time.strftime('%Y-%m-%d %H:%M')}")

    # 判断实际下班打卡时间是否晚于19:00
    late_evening = datetime.strptime(f'{date_str} 19:00', '%y-%m-%d %H:%M')

    # 计算加班时间
    overtime = max(timedelta(), end_punch - can_punch_out_time)
    overtime_hours = overtime.total_seconds() / 3600
    overtime_hours_formatted = f"{int(overtime_hours)}:{int((overtime_hours % 1) * 60):02d}"

    # 如果加班时间超过50分钟，则调整下班时间
    if end_punch > late_evening and overtime_hours >= 0.8333:  # 50分钟 = 0.8333小时
        adjusted_can_punch_out_time = can_punch_out_time + timedelta(hours=1)
        overtime = max(timedelta(), end_punch - adjusted_can_punch_out_time)
        overtime_hours = overtime.total_seconds() / 3600
        overtime_hours_formatted = f"{int(overtime_hours)}:{int((overtime_hours % 1) * 60):02d}"

    # 计算总工作时长
    total_work_duration = morning_duration + x_hours_to_eight + timedelta(seconds=overtime.total_seconds())
    total_work_duration_hours = total_work_duration.total_seconds() / 3600
    total_work_duration_formatted = f"{int(total_work_duration_hours)}:{int((total_work_duration_hours % 1) * 60):02d}"

    print('总工作时长:', total_work_duration_hours)

    # 根据工作时长计算餐补和交补
    meal_subsidy = 1 if total_work_duration_hours >= 10 else 0
    transport_subsidy = 1 if total_work_duration_hours >= 11 else 0

    return total_work_duration_formatted, overtime_hours_formatted, meal_subsidy, transport_subsidy, can_punch_out_time

# 应用函数到每一行
for i, row in df.iterrows():
    work_duration, overtime_hours_formatted, meal_subsidy, transport_subsidy, can_punch_out_time = calculate_time(row)
    if work_duration is not None:
        df.at[i, '工作时长'] = work_duration
        df.at[i, '加班时间'] = overtime_hours_formatted
        df.at[i, '餐补次数'] = meal_subsidy
        df.at[i, '交补次数'] = transport_subsidy
        # df.at[i, '可打下班卡时间'] = can_punch_out_time.strftime('%Y-%m-%d %H:%M')

# 导出结果到新的 Excel 文件
df.to_excel('考勤结果.xlsx', index=False)

# 打印结果
print(df)
