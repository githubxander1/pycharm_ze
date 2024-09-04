import pandas as pd


# 定义函数来计算工作时长
def calculate_work_hours(row):
    start_time = pd.to_datetime(row['上班打卡时间'])
    end_time = pd.to_datetime(row['下班打卡时间'])
    work_duration = end_time - start_time

    # 减去午餐时间
    if start_time.hour < 13 and end_time.hour >= 13:
        work_duration -= pd.Timedelta(hours=1.5)

    # 减去晚餐时间
    if end_time.hour > 18:
        work_duration -= pd.Timedelta(hours=1)

    return work_duration.total_seconds() / 3600


# 定义函数来处理数据
def process_data(df):
    # 将日期列转换为字符串格式
    df['日期'] = df['日期'].astype(str)

    # 处理日期
    df['日期'] = df['日期'].apply(
        lambda x: pd.to_datetime(x.split()[0].replace('-', '/')) if '次日' not in x else pd.to_datetime(
            x.split()[0].replace('-', '/')) + pd.Timedelta(days=1))

    # 计算工作时长
    df['工作时长'] = df.apply(calculate_work_hours, axis=1)

    # 根据工作时长判断餐补和交补
    df['餐补'] = df['工作时长'].apply(lambda x: 1 if x >= 10 else 0)
    df['交补'] = df['工作时长'].apply(lambda x: 1 if x >= 11 else 0)

    # 计算加班时长
    def calculate_overtime(work_hours):
        if work_hours >= 10:
            overtime = (work_hours - 8) // 1
            return int(overtime)
        return 0

    df['加班时长'] = df['工作时长'].apply(calculate_overtime)

    return df


# 主程序
if __name__ == "__main__":
    # 读取Excel文件
    df = pd.read_excel('考勤表.xlsx')

    # 检查列名
    print("列名:", df.columns.tolist())

    # 处理数据
    processed_df = process_data(df)

    # 输出结果到新的Excel文件
    processed_df.to_excel('处理后的考勤表.xlsx', index=False)

    print("处理完成，结果已保存到'处理后的考勤表.xlsx'")