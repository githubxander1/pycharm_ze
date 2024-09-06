import pandas as pd

# 定义计算工作时长和加班时长的函数
def calculate_work_and_overtime_v3(start_work, end_work, date_str):
    # 提取日期部分
    date = date_str.split(" ")[0]
    week = date_str.split(" ")[1]
    # print(week)

    # 正常工作时间
    normal_work_start, normal_work_end = "08:30", "18:00"
    # 午休时间
    lunch_start, lunch_end = "12:00", "13:30"
    # 晚餐时间
    dinner_start, dinner_end = "18:00", "19:00"

    # 将时间转换为分钟
    def time_to_minutes(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    # 处理次日情况
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

    # 计算加班时长，如果周末，则全部算作加班时长
    date_obj = pd.to_datetime(date, format='%y-%m-%d')
    is_weekend = date_obj.weekday() >= 5  # 5 表示周六，6 表示周日

    if is_weekend:
        overtime_minutes = work_minutes
    else:
        overtime_minutes = max(0, work_minutes - (normal_work_end - normal_work_start))

    overtime_hours = round(overtime_minutes / 60)

    # 工作时长和加班时长
    work_hours = work_minutes / 60
    return round(work_hours, 1), overtime_hours

# 将字典转换成 DataFrame
data = {
    '姓名': ['肖泽华', '肖泽华', '肖泽华', '肖泽华', '范德萨', '范德萨', '范德萨', '范德萨', '范德萨', '范德萨'],
    '日期': ['24-08-01 星期五', '24-08-02 星期五', '24-08-03 星期六', '24-08-02 星期五', '24-08-16 星期五',
             '24-08-17 星期六', '24-08-18 星期日', '24-08-19 星期一', '24-08-20 星期二', '24-08-21 星期三'],
    '考勤状态': ['早到', '正常', '弹性', '迟到', '早退', '上半天', '下半天', '上下晚餐补', '上下晚餐交补', '上到第二天'],
    '上班1打卡时间': ['08:20', '08:30', '09:00', '09:40', '08:30', '08:30', '13:30', '08:30', '08:30', '08:53'],
    '下班1打卡时间': ['18:30', '18:00', '18:10', '19:10', '17:50', '12:00', '18:00', '20:00', '21:00', '次日 00:03'],
}

# df = pd.DataFrame(data)
df = pd.read_excel('考勤表.xlsx')

# 应用更新后的函数计算工作时长和加班时长
df[['工作时长', '加班时长']] = df.apply(lambda row: calculate_work_and_overtime_v3(row['上班1打卡时间'], row['下班1打卡时间'], row['日期']), axis=1, result_type='expand')

# 重新计算餐补次数和交补次数
df['餐补次数'] = (df['工作时长'] > 9).astype(int)
df['交补次数'] = (df['工作时长'] > 10).astype(int)

# 将餐补次数和交补次数填入第13列和第14列
# df.insert(12, '餐补次数', df.pop('餐补次数'))
# df.insert(13, '交补次数', df.pop('交补次数'))

# 打印结果
# print(df)

# 导出结果到新的 Excel 文件
df.to_excel('考勤结果.xlsx', index=False)
