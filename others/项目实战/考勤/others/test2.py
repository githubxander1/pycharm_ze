import pandas as pd

# 定义计算工作时长和加班时长的函数
def calculate_work_and_overtime_v3(start_work, end_work, date):
    # 定义正常工作时间
    normal_work_start, normal_work_end = "08:30", "18:00"
    # 午休时间
    lunch_start, lunch_end = "12:00", "13:30"
    # 晚餐时间
    dinner_start, dinner_end = "18:00", "19:00"

    # 将时间转换为分钟
    def time_to_minutes(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    # 将日期和时间结合，处理次日的情况
    if "次日" in end_work:
        day, end_work = end_work.split(" ")
        date = pd.to_datetime(date.split(" ")[0], format='%y-%m-%d') + pd.Timedelta(days=1)
        end_work = time_to_minutes(end_work) + 24 * 60  # 加上一天的分钟数，使时间变为正数
    else:
        end_work = time_to_minutes(end_work)

    start_work = time_to_minutes(start_work)
    normal_work_start = time_to_minutes(normal_work_start)
    normal_work_end = time_to_minutes(normal_work_end)
    lunch_start = time_to_minutes(lunch_start)
    lunch_end = time_to_minutes(lunch_end)
    dinner_start = time_to_minutes(dinner_start)
    dinner_end = time_to_minutes(dinner_end)

    # 如果上班时间早于8:30，则按8:30算
    if start_work < normal_work_start:
        start_work = normal_work_start

    # 如果下午开始打上班卡，按13:30开始算
    if start_work >= lunch_end:
        start_work = lunch_end

    # 计算工作时长
    work_minutes = end_work - start_work

    # 减去午休时间
    if start_work < lunch_start and end_work > lunch_end:
        work_minutes -= (lunch_end - lunch_start)

    # 减去晚餐时间
    if start_work < dinner_start and end_work > dinner_end:
        work_minutes -= (dinner_end - dinner_start)

    # 计算加班时长
    overtime_minutes = max(0, work_minutes - (normal_work_end - normal_work_start))
    overtime_hours = round(overtime_minutes / 60)

    # 工作时长和加班时长
    work_hours = work_minutes / 60
    return round(work_hours, 1), overtime_hours

# 读取'考勤表.xlsx'文件
file_path = '考勤表.xlsx'
file_path_result = '考勤表1.xlsx'
df = pd.read_excel(file_path)

# 应用更新后的函数计算工作时长和加班时长
df['工作时长'], df['加班时长'] = zip(*df.apply(lambda row: calculate_work_and_overtime_v3(row['上班1打卡时间'], row['下班1打卡时间'], row['日期']), axis=1))

# 重新计算餐补次数和交补次数
df['餐补次数'] = (df['工作时长'] > 9).astype(int)
df['交补次数'] = (df['工作时长'] > 10).astype(int)
df.to_excel(file_path_result, index=False)
