import pandas as pd
from datetime import datetime, timedelta

# 读取 Excel 文件并确保相关列的数据类型为字符串
dtype_dict = {
    '姓名': str,
    '日期': str,
    '上班1打卡时间': str,
    '下班1打卡时间': str,
    '工作时长': str,
    '加班时间': str,
    '餐补次数': int,
    '交补次数': int
}

df = pd.read_excel('考勤表.xlsx', dtype=dtype_dict)

# 定义一个函数来计算工作时长和加班时间
def calculate_time(row):
    # 解析日期
    date_str = row['日期'].split()[0] if pd.notna(row['日期']) and isinstance(row['日期'], str) else None
    if date_str is None:
        print(f"无法解析日期: {row['日期']}")
        return None, None, None, None, None
    date = datetime.strptime(date_str, '%y-%m-%d')

    # 解析上班打卡时间
    start_punch_str = row['上班1打卡时间']
    if pd.isna(start_punch_str) or not isinstance(start_punch_str, str):
        print(f"无法解析上班打卡时间: {start_punch_str}")
        return None, None, None, None, None
    try:
        start_punch = datetime.strptime(f'{date_str} {start_punch_str}', '%y-%m-%d %H:%M')
    except ValueError:
        print(f"无法解析上班打卡时间: {start_punch_str}")
        return None, None, None, None, None

    # 解析下班打卡时间
    end_punch_str = row['下班1打卡时间']
    if pd.isna(end_punch_str) or not isinstance(end_punch_str, str):
        print(f"无法解析下班打卡时间: {end_punch_str}")
        return None, None, None, None, None
    if '次日' in end_punch_str:
        next_day_str = (date + timedelta(days=1)).strftime('%Y-%m-%d')
        try:
            end_punch = datetime.strptime(f'{next_day_str} {end_punch_str.split(" ")[1]}', '%Y-%m-%d %H:%M')
        except ValueError:
            print(f"无法解析次日下班打卡时间: {end_punch_str}")
            return None, None, None, None, None
    else:
        try:
            end_punch = datetime.strptime(f'{date_str} {end_punch_str}', '%y-%m-%d %H:%M')
        except ValueError:
            print(f"无法解析下班打卡时间: {end_punch_str}")
            return None, None, None, None, None

    # 计算上午工作时长
    morning_start = datetime.strptime(f'{date_str} 08:30', '%y-%m-%d %H:%M')
    morning_end = datetime.strptime(f'{date_str} 12:00', '%y-%m-%d %H:%M')
    morning_duration = min(morning_end, end_punch) - max(morning_start, start_punch)
    morning_hours = morning_duration.total_seconds() / 3600

    # 计算下午开始时间
    afternoon_start = datetime.strptime(f'{date_str} 13:30', '%y-%m-%d %H:%M')

    # 计算满足8小时的工作时长
    x_hours = 8 - morning_hours
    can_punch_out_time = afternoon_start + timedelta(hours=x_hours)

    # 计算加班时间
    overtime = max(timedelta(), end_punch - can_punch_out_time)
    overtime_hours = overtime.total_seconds() / 3600

    # 考虑加班时间扣除
    if "星期六" in row['日期'] or "星期日" in row['日期']:
        # 周末加班需去掉1.5小时午休时间
        lunch_break = timedelta(hours=1.5)
        # 避免重复扣除午休时间
        if morning_end <= afternoon_start:
            overtime -= lunch_break
    else:
        # 工作日加班需去掉1小时晚餐时间
        dinner_break = timedelta(hours=1)
        overtime -= dinner_break

    # 确保加班时间不小于0
    overtime = max(timedelta(), overtime)

    # 格式化加班时间
    overtime_hours = overtime.total_seconds() / 3600
    overtime_formatted = f"{int(overtime_hours)}:{int((overtime_hours % 1) * 60):02d}"

    # 计算总工作时长
    total_work_duration = (end_punch - start_punch).total_seconds() / 3600
    total_work_duration_formatted = f"{int(total_work_duration)}:{int((total_work_duration % 1) * 60):02d}"

    # 根据工作时长计算餐补和交补
    meal_subsidy = 1 if total_work_duration >= 10 else 0
    transport_subsidy = 1 if total_work_duration >= 11 else 0

    return total_work_duration_formatted, overtime_formatted, meal_subsidy, transport_subsidy, can_punch_out_time

# 应用函数到每一行
for i, row in df.iterrows():
    work_duration, overtime, meal_subsidy, transport_subsidy, can_punch_out_time = calculate_time(row)
    if work_duration is not None:
        df.at[i, '工作时长'] = work_duration
        df.at[i, '加班时间'] = overtime
        df.at[i, '餐补次数'] = meal_subsidy
        df.at[i, '交补次数'] = transport_subsidy
        df.at[i, '可打下班卡时间'] = can_punch_out_time.strftime('%Y-%m-%d %H:%M')

# 导出结果到新的 Excel 文件
df.to_excel('考勤结果.xlsx', index=False)

# 打印结果
print(df)
