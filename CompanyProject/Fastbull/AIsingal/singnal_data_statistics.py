# -*-coding: utf-8 -*-
# @Time    : 2023/9/8 9:56
# @Author  : chengjianbo
# @File    : singnal_data_statistics.py
# @Software: PyCharm
import datetime
import time
from typing import List
import pandas as pd
import yaml

# from .base import calculate_average, time_format, get_time_day
# from .conversion_data import Synchronous_Data
# from .db_handler import DBHandler
from CompanyProject.Fastbull.base import get_time_day, calculate_average
from CompanyProject.Fastbull.conversion_data import Synchronous_Data
from CompanyProject.Fastbull.AIsingal.db_handler import DBHandler


# f = open(r'D:\1test\PycharmProject\pycharm_ze\CompanyProject\Fastbull\config.sina.yaml', encoding='utf-8')
f = open('config.yaml', encoding='utf-8')
        #
yaml_data = yaml.load(f, Loader=yaml.FullLoader)  # 读取yaml
db = DBHandler(host=yaml_data['database']['host'], port=yaml_data['database']['port'],
               user=yaml_data['database']['user'], password=yaml_data['database']['password'],
               charset=yaml_data['database']['charset'], database=yaml_data['database']['database'])
def get_start_end_time_week_time():
    res = db.query("""
                        SELECT
                                    openTime 
                                FROM
                                    strategy_signal 
                                WHERE
                                    status = 1
                                ORDER BY
                                    openTime ASC 
                                    LIMIT 1
        """, one=False)

    # 将毫秒级时间戳转换为秒级时间戳
    seconds_timestamp = res[0]["openTime"] / 1000.0

    # 使用datetime模块将秒级时间戳转换为年、月和日
    datetime_obj = datetime.datetime.fromtimestamp(seconds_timestamp)

    # 提取年、月和日
    year = datetime_obj.year
    month = datetime_obj.month
    day = datetime_obj.day
    start_date = datetime.datetime(year, month, day)
    end_date = datetime.datetime.now()

    timestamps = []

    current_date = start_date

    while current_date <= end_date:
        # 找到当前日期所在周的开始日期
        week_start = current_date - datetime.timedelta(days=current_date.weekday())

        # 找到当前日期所在周的结束日期（最后一天的23:59:59）
        week_end = week_start + datetime.timedelta(days=6, hours=23, minutes=59, seconds=59)

        # 转换为毫秒时间戳
        start_timestamp = int(week_start.timestamp()) * 1000
        end_timestamp = int(week_end.timestamp()) * 1000

        timestamps.append((start_timestamp, end_timestamp))

        # 移动到下一周的开始
        current_date = week_start + datetime.timedelta(weeks=1)

    print(timestamps)
    return timestamps
def get_start_end_time_month_time():
    res = db.query("""
                    SELECT
                                openTime 
                            FROM
                                strategy_signal 
                            WHERE
                                status = 1
                            ORDER BY
                                openTime ASC 
                                LIMIT 1
    """,one=False)

    # 将毫秒级时间戳转换为秒级时间戳
    seconds_timestamp = res[0]["openTime"] / 1000.0

    # 使用datetime模块将秒级时间戳转换为年、月和日
    datetime_obj = datetime.datetime.fromtimestamp(seconds_timestamp)

    # 提取年、月和日
    year = datetime_obj.year
    month = datetime_obj.month
    day = datetime_obj.day

    start_date = datetime.datetime(year, month, day)
    end_date = datetime.datetime.now()

    timestamps = []

    current_date = start_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    while current_date <= end_date:
        # 获取当前月份的结束日期
        next_month = current_date.replace(day=28) + datetime.timedelta(days=4)
        month_end = next_month - datetime.timedelta(days=next_month.day)
        month_end = month_end.replace(hour=23, minute=59, second=59)

        # 转换为毫秒时间戳
        start_timestamp = int(current_date.timestamp()) * 1000
        end_timestamp = int(month_end.timestamp()) * 1000

        timestamps.append((start_timestamp, end_timestamp))

        # 移动到下一个月的开始
        current_date = next_month.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    print(timestamps)
    return timestamps
def get_all_year_time(year=2023):
    # 设置年份
    year = year
    # 创建一个空列表来存储每个月份的第一天的零点毫秒时间戳
    timestamps = []
    # 循环遍历12个月份
    for month in range(1, 13):
        # 创建日期对象，表示每个月的第一天
        first_day_of_month = datetime.datetime(year, month, 1, 0, 0, 0, 0)
        # 获取毫秒时间戳并添加到列表中
        timestamp = int(first_day_of_month.timestamp()) * 1000
        timestamps.append(timestamp)
    print(timestamps)
    return timestamps
def check_singnal_data_statistics(table_strategy,table_strategy_signal):


    print("*"*80,"累计盈亏，昨日盈亏，上周总盈亏","*"*80)
    #累计盈亏
    sql1 = "select sum(b.profitLoss) from {} as a left join {} as b on a._id = b.strategyId where a.display =1 and a.status=1  "
    res1 = db.query(sql1.format(table_strategy,table_strategy_signal),one=False)

    list = get_time_day()
    res2 = []
    for i in list:#此处改动，与返回值有关
        sql = """
            SELECT sum(a.profitLoss) FROM {} AS a LEFT JOIN {} AS b ON a.strategyId = b._id WHERE a.positionType = 2 AND a.STATUS = 1 and
            b.display =1 AND a.closeTime >= {} AND a.closeTime < {} ORDER BY a.closeTime DESC
            """.format( table_strategy_signal,table_strategy,i[0], i[1])
        Yesterdays_profit_and_loss = db.query(sql)
        res2.append(Yesterdays_profit_and_loss['sum(a.profitLoss)'])

    print(f'累计盈亏:{res1[0]["sum(b.profitLoss)"]}')
    print(f"昨日盈亏:{res2[0]}")
    print(f"上周总盈亏:{res2[1]}")
    print(f"上月总盈亏:{res2[2]}")



    #第一部分
    print("*"*80,"策略数，信号量，总盈亏","*"*80)
    #策略数-已上架未隐藏的策略数量
    sql3 = "select count(*) from {} where status =1 and display =1"
    res3 = db.query(sql3.format(table_strategy), one=False)
    print(f'策略数:{res3[0]["count(*)"]}')

    # 信号量-所有策略的订单数量之和。
    sql4 = """
            select count(*) from  {} where STATUS = 1
    """
    res4 = db.query(sql4.format(table_strategy_signal), one=False)
    print(f'信号量:{res4[0]["count(*)"]}')
    print(f'总盈亏:{res1[0]["sum(b.profitLoss)"]}')#同33行

    print("*"*80,"近期表现","*"*80)
    #第二部分
    #获取2023年的月份数据
    time1_list = get_start_end_time_month_time()#返回2013到2023所有月份
    signalCount = []
    profitLossCount = []
    for i,value in enumerate(time1_list):
        print(f'第{i+1}遍历的近期表现:')
        #图表 - 开仓信号数量
        sql_opentime_signal_count="""
        select count(*) from strategy_signal where openTime>={}  and openTime<= {} and status =1
        """
        #图表 - 平仓信号数量
        sql_closetime_signal_count="""
        select count(*) from strategy_signal where closetime>={}  and closetime<= {} and status =1 and positionType =2
        """
        #图表 - 平仓盈亏点数
        sql_profit_signal_count = """
        select sum(profitLoss) from strategy_signal where closetime>={}  and closetime<= {} and status =1 and positionType =2
            """

        result1 = db.query(sql_opentime_signal_count.format(value[0],value[1]),one=False)
        result2 = db.query(sql_closetime_signal_count.format(value[0],value[1]), one=False)
        result3 = db.query(sql_profit_signal_count.format(value[0],value[1]), one=False)

        # 平均每月信号数量
        num1 = result1[0]["count(*)"]

        signalCount.append(num1)

        # 平均每月盈亏
        num2 = result3[0]["sum(profitLoss)"]
        if num2 != None:
            profitLossCount.append(num2)

        print('月开始时间：{},月结束时间：{}'.format(value[0], value[1]))
        print("月开仓信号数量:",result1[0]["count(*)"])
        print("月平仓信号数量:",result2[0]["count(*)"])
        print("月平仓盈亏点数:",result3[0]["sum(profitLoss)"])

    value1 = calculate_average(signalCount)
    value2 = calculate_average(profitLossCount)


    print('\n平均每月信号数量:',value1)#这里有疑问，就是未到的时间是否进行数目的计算
    print('平均每月盈亏:',value2)#盈亏为0的算不算？

    # 获取2023年的所有周数据
    time1_list1 = get_start_end_time_week_time()  # 返回2013到2023所有周数据
    signalCount1 = []
    profitLossCount1 = []
    for i,value in enumerate(time1_list1):
        # print(f'第{i + 1}遍历的近期表现:')
        # 图表 - 开仓信号数量
        sql_opentime_signal_count = """
            select count(*) from strategy_signal where openTime>={}  and openTime<= {} and status =1
            """
        # 图表 - 平仓信号数量
        sql_closetime_signal_count = """
            select count(*) from strategy_signal where closetime>={}  and closetime<= {} and status =1 and positionType =2
            """
        # 图表 - 平仓盈亏点数
        sql_profit_signal_count = """
            select sum(profitLoss) from strategy_signal where closetime>={}  and closetime<= {} and status =1 and positionType =2
                """

        result1 = db.query(sql_opentime_signal_count.format(value[0],value[1]), one=False)
        result2 = db.query(sql_closetime_signal_count.format(value[0],value[1]), one=False)
        result3 = db.query(sql_profit_signal_count.format(value[0],value[1]), one=False)

        # 平均每周信号数量
        num1 = result1[0]["count(*)"]
        signalCount1.append(num1)

        # 平均每周盈亏
        num2 = result3[0]["sum(profitLoss)"]
        if num2 != None:
            profitLossCount1.append(num2)
        # print('周开始时间：{},周结束时间：{}'.format(value[0],value[1]))
        # print("周开仓信号数量:", result1[0]["count(*)"])
        # print("周平仓信号数量:", result2[0]["count(*)"])
        # print("周平仓盈亏点数:", result3[0]["sum(profitLoss)"])
        # print('不打印周的')

    value1 = calculate_average(signalCount1)
    value2 = calculate_average(profitLossCount1)

    print('\n平均每周信号数量:', value1)  # 这里有疑问，就是未到的时间是否进行数目的计算
    print('平均每周盈亏:', value2)  # 盈亏为0的算不算？


    #第三部分
    print("*"*80,"品种表现","*"*80)
    #将所有策略的订单，按品种进行分类，把盈亏最高的几个品种
    sql5 = """
        SELECT
                b.symbol,
                sum( b.profitLoss ) AS profit_Loss 
            FROM
                {} AS a
                LEFT JOIN {} AS b ON a._id = b.strategyId 
            WHERE
                a.display = 1 
                AND a.STATUS = 1 
                and b.symbol is not null
            GROUP BY
                b.symbol 
            ORDER BY
                profit_Loss DESC 
                LIMIT 8
    """
    res5 = db.query(sql5.format(table_strategy,table_strategy_signal), one=False)
    df1 = pd.DataFrame(res5)
    print('盈亏最高的几个品种:\n',df1)

    #dataframe删除盈亏列后转换为列表
    df1 = df1.drop("profit_Loss",axis=1)
    list1: List = df1.values.tolist()#赋值的写法导致的底色
    flat_list = [item for sublist in list1 for item in sublist]


    # 1）信号数量-该品种的订单数量（未平仓的+已平仓的)
    sql6_number_of_signals = """
            SELECT
                        count(*) 
                    FROM
                        {} 
                    WHERE
                        symbol = "{}" 
                        AND STATUS = 1
    """
    # 2）盈利信号数量-该品种的已平仓的订单中，盈亏点数大于零的订单数量。
    sql7_Number_of_profit_signals = """
        SELECT
                    count(*) 
                FROM
                    {} 
                WHERE
                    symbol = "{}" 
                    AND STATUS = 1 
                    AND positionType = 2 
                    AND profitLoss >0
    """
    # 3）亏损信号-该品种的已平仓的订单中，盈亏点数小于零的订单数量。
    sql8_Number_of_loss_signals = """
        SELECT
                    count(*) 
                FROM
                    {} 
                WHERE
                    symbol = "{}" 
                    AND STATUS = 1 
                    AND positionType = 2 
                    AND profitLoss <0
    """
    # 4）平仓盈亏-该品种的已平仓订单的盈亏之和。
    sql9_Closing_Profit_and_Loss_Quantity = """
        SELECT
                    sum( profitLoss) 
                FROM
                    {} 
                WHERE
                    symbol = "{}" 
                    AND STATUS = 1 
                    AND positionType = 2
    """
    number_of_signals = []
    Number_of_profit_signals = []
    Number_of_loss_signals = []
    Closing_Profit_and_Loss_Quantity = []

    for i in flat_list:
        res6 = db.query(sql6_number_of_signals.format(table_strategy_signal,i))
        res7 = db.query(sql7_Number_of_profit_signals.format(table_strategy_signal,i))
        res8 = db.query(sql8_Number_of_loss_signals.format(table_strategy_signal,i))
        res9 = db.query(sql9_Closing_Profit_and_Loss_Quantity.format(table_strategy_signal,i))
        number_of_signals.append(res6["count(*)"])
        Number_of_profit_signals.append(res7["count(*)"])
        Number_of_loss_signals.append(res8["count(*)"])
        Closing_Profit_and_Loss_Quantity.append(res9["sum( profitLoss)"])
    # print(list1)

    #获取当前时间
    now_second_time = int(time.time())
    for i in range(len(number_of_signals)):
        value0 = flat_list[i]
        value1 = number_of_signals[i]
        value2 = Number_of_profit_signals[i]
        value3 = Number_of_loss_signals[i]
        value4 = Closing_Profit_and_Loss_Quantity[i]
        # 月平均信号量-该品种的第一个订单的开仓时间是 t1  monthly_average_semaphore
        sql10 = """
                SELECT
                            openTime 
                        FROM
                            {} 
                        WHERE
                            symbol = "{}" 
                            and status = 1
                        ORDER BY
                            openTime ASC 
                            LIMIT 1
            """
        # 该品种的总订单数
        sql11 = """
                SELECT
                            count(*) 
                        FROM
                            {} 
                        WHERE
                            symbol = "{}" 
                            AND STATUS = 1
        """
        res10 = db.query(sql10.format(table_strategy_signal,flat_list[i]))
        res11 = db.query(sql11.format(table_strategy_signal,flat_list[i]))
        # print(res10)#显示opentime
        t1 = res10["openTime"]
        all_number_order = res11["count(*)"]
        print('res10["openTime"]',res10["openTime"])
        print('now_second_time',now_second_time)
        # 计算秒数差异1694766074
        seconds_difference = abs(now_second_time - t1/1000)
        # 将秒数差异转换为天数差异
        days_difference = seconds_difference / (60 * 60 * 24)

        print("all_number_order",all_number_order)
        print("days_difference",days_difference)
        monthly_average_semaphore =(all_number_order/ days_difference*30)
        print('第 {} 个品种:'.format(i+1))
        print(f"品种:{value0}\n信号数量:{value1}\n盈利信号:{value2}\n亏损信号:{value3}\n平仓盈亏:{value4}\n月平均信号量:{monthly_average_semaphore}\n")

    # 4，第四部分-月度统计
    month_time_list = get_all_year_time()
    for i in range(len(month_time_list) - 1):
        print("*"*60,'第{}个月,第 {} 到 {} 个月的月度统计'.format(i+1,month_time_list[i], month_time_list[i + 1]),"*"*60)
        month_star_time = month_time_list[i]
        month_end_time = month_time_list[i + 1]
        # 筛出盈利总点数
        sql19 = """
            select sum(profitLoss) from {} where closeTime>={} and closetime<{} and positionType = "2"   and  status=1 and profitLoss>0 
             """
        sql20 = """
    
        select count(profitLoss) from {} where closeTime>={} and closetime<{} and positionType = "2"   and  status=1 and profitLoss>0 
                  """
        Total_profit_points= db.query(sql19.format(table_strategy_signal,month_star_time,month_end_time), one=False)
        number_Total_profit_points= db.query(sql20.format(table_strategy_signal,month_star_time,month_end_time), one=False)
        # 筛出亏损总点数
        sql21 = """
                select sum(profitLoss) from {} where closeTime>={} and closetime<{} and positionType = "2"  and  status=1  and  profitLoss<0
        """
        sql22 = """
                select count(profitLoss) from {} where closeTime>={} and closetime<{} and positionType = "2"  and  status=1  and  profitLoss<0
        """
        Total_loss_points = db.query(sql21.format(table_strategy_signal,month_star_time,month_end_time), one=False)
        number_Total_loss_points = db.query(sql22.format(table_strategy_signal,month_star_time,month_end_time), one=False)
        print(f"移动端h5有此数据此月\n    盈利:{Total_profit_points[0]['sum(profitLoss)']}数量:{number_Total_profit_points[0]['count(profitLoss)']}"
              f"    VS      亏损:{Total_loss_points[0]['sum(profitLoss)']}数量:{number_Total_loss_points[0]['count(profitLoss)']}")

        # 1）信号量-当月内开仓的订单数量。时间暂时定位8月 8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月8月时间只看八月
        sql12 = """
                select count(*) from {} where openTime>={} and openTime <{} and status=1			
        """
        res12 = db.query(sql12.format(table_strategy_signal,month_star_time,month_end_time))
        print(f'信号量-当月内开仓的订单数量: {res12["count(*)"]}')
        #总盈亏
        data1 = db.query("select sum(profitLoss) from {} where closeTime>={} and closetime<{} and positionType = 2  and  status=1".format(table_strategy_signal,month_star_time,month_end_time), one=False)
        print("总盈亏: {}".format(data1[0]["sum(profitLoss)"]))
        #胜率
        Number_of_profitable_orders = db.query("select count(*) from {} where  profitLoss>0 and closeTime>={} and closetime<{} and `status`=1".format(table_strategy_signal,month_star_time,month_end_time))
        Total_Orders = db.query("select count(*) from {} where closeTime>={} and closetime<{} and positionType =2  and  status=1".format(table_strategy_signal,month_star_time,month_end_time))
        # print('123123',Total_Orders["count(*)"])
        if Total_Orders["count(*)"] != 0:
            print("胜率 : {:.2f}%".format(Number_of_profitable_orders["count(*)"] / Total_Orders["count(*)"] * 100))
        else:
            print("胜率不存在")

        #盈亏#筛选出某月时间下的已平仓的品种类别
        res  = db.query('select DISTINCT(symbol) from {} where closeTime>={} and closetime<{} and positionType = "2"  and  status=1'.format(table_strategy_signal,month_star_time,month_end_time),one = False)

        profit_loss_ratio_list = []
        average_profit_list = []
        average_loss_list = []
        for i in res:
            symbol_name = i["symbol"]
            #a品种盈亏大于0的订单数
            sql13 = """
            select count(*) from {} where closeTime>={} and closetime<{} and positionType = "2" and symbol = "{}" and profitLoss>0  and  status=1
            """
            max_0_order = db.query(sql13.format(table_strategy_signal,month_star_time,month_end_time,symbol_name), one=False)
            # a品种盈亏小于0的订单数
            sql14 = """
            select count(*) from {} where closeTime>={} and closetime<{} and positionType = "2" and symbol = "{}" and profitLoss<0  and  status=1
            """
            min_0_order = db.query(sql14.format(table_strategy_signal,month_star_time,month_end_time,symbol_name), one=False)
            #筛出盈利总点数
            sql15 = """
            select sum(profitLoss) from {} where closeTime>={} and closetime<{} and positionType = "2" and symbol = "{}" and profitLoss>0  and  status=1
            """
            Total_Profit_Points = db.query(sql15.format(table_strategy_signal,month_star_time,month_end_time,symbol_name), one=False)
            #筛出亏损总点数
            sql16 = """
                    select sum(profitLoss) from {} where closeTime>={} and closetime<{} and positionType = "2" and symbol = "{}" and profitLoss<0  and  status=1
            """
            total_points_of_loss = db.query(sql16.format(table_strategy_signal,month_star_time,month_end_time,symbol_name), one=False)

            max_0_order = max_0_order[0]['count(*)']
            min_0_order = min_0_order[0]['count(*)']
            Total_Profit_Points = Total_Profit_Points[0]['sum(profitLoss)']
            total_points_of_loss = total_points_of_loss[0]['sum(profitLoss)']
            if Total_Profit_Points != None:
                Total_Profit_Points = abs(Total_Profit_Points)
            if total_points_of_loss != None:
                total_points_of_loss = abs(total_points_of_loss)
            #单个品种的盈亏比 = (盈利总点数/盈利订单数) : (亏损总点数/亏损订单数)
            if min_0_order == 0 and max_0_order == 0:
                # print("{}的盈亏比不存在".format(symbol_name))
                # print(f"{symbol_name}的盈利：{Total_Profit_Points},亏损：{total_points_of_loss}")
                continue
            elif  min_0_order == 0  :
                # print("{}的盈亏比不存在".format(symbol_name))
                # print(f"{symbol_name}的盈利：{Total_Profit_Points},亏损：{total_points_of_loss}")
                average_profit_list.append(Total_Profit_Points)
                continue
            elif max_0_order == 0:
                # print("{}的盈亏比不存在".format(symbol_name))
                # print(f"{symbol_name}的盈利：{Total_Profit_Points},亏损：{total_points_of_loss}")
                average_loss_list.append(total_points_of_loss)
                continue
            else:
                #平均盈利和平均亏损
                average_profit = Total_Profit_Points / max_0_order
                average_loss = total_points_of_loss / min_0_order
                #盈亏比
                profit_loss_ratio = average_profit / average_loss
                # print("{}品种的盈亏{}".format(symbol_name,profit_loss_ratio))
                profit_loss_ratio_list.append(profit_loss_ratio)
                average_profit_list.append(Total_Profit_Points)
                average_loss_list.append(total_points_of_loss)
                # print(f"{symbol_name}的盈利：{Total_Profit_Points},亏损：{total_points_of_loss}")

        # print("profit_loss_ratio_list", profit_loss_ratio_list)
        # print("average_profit_list", average_profit_list)
        # print("average_loss_list", average_loss_list)
        print("-------------")
        average1 = calculate_average(profit_loss_ratio_list)
        average2 = calculate_average(average_profit_list)
        average3 = calculate_average(average_loss_list)



        print("盈亏比:{:.2f}".format(average1))
        print("平均盈利:{:.2f}".format(average2))
        print("平均亏损:{:.2f}".format(average3))

        # 某个时间段的所有品种数据得开仓平仓列
        data = db.query('select openTime,closeTime from {} where closeTime>={} and closetime<{} and positionType = "2" and status=1'.format(table_strategy_signal,month_star_time,month_end_time), one=False)

        # 某个时间段的所有品种数据个数
        count = db.query(
            'select count(*) from {} where closeTime>={} and closetime<{} and positionType = "2" and  status=1'.format(table_strategy_signal,month_star_time,month_end_time), one=False)
        ##某个策略的所有品种数据个数
        count = count[0]["count(*)"]
        # print(data)
        if count != 0:
            time_format(data, count)
        else:
            print("平均持仓时间不存在")

        #3）日均信号量-当月信号量/22，四舍五入保留一位小数。
        sql17 = """
        select count(*)from {} where openTime>={} and openTime <{}  and status=1 
        """
        res13 = db.query(sql17.format(table_strategy_signal,month_star_time,month_end_time), one=False)
        # print(res13)
        print("日均信号量:{:.1f}".format(res13[0]["count(*)"]/22))

    print("*" * 80, "优质策略", "*" * 80)
    #5，第五部分-选取总盈亏最高的几个策略出来从左到右展示，策略名称下方展示的是该策略的总盈亏点数。
    sql18 = """
        SELECT
                    a.strategyId,
                    b.strategy_Name,
                    a.profit_Loss 
                FROM
                    ( SELECT strategyId, sum( profitLoss ) AS profit_Loss FROM {} WHERE STATUS = 1 GROUP BY strategyId ORDER BY profit_Loss DESC ) AS a
                    LEFT JOIN {} AS b ON a.strategyId = b._id 
                    LIMIT 5
        """
    res14 = db.query(sql18.format(table_strategy_signal,table_strategy), one=False)
    print("优质策略--总盈亏最高的几个策略:")
    df2 = pd.DataFrame(res14)
    print(df2)



if __name__ == '__main__':
    # 切换环境
    # environment = 'test'
    environment = 'test'

    if environment == 'test':
        table_strategy = 'strategy'
        table_strategy_signal = 'strategy_signal'
        Synchronous_Data("test")
        check_singnal_data_statistics(table_strategy,table_strategy_signal)
    else:
        table_strategy_pre = 'strategy_pre'
        table_strategy_signal_pre = 'strategy_signal_pre'
        Synchronous_Data('pre')
        check_singnal_data_statistics(table_strategy_pre,table_strategy_signal_pre)


    # get_all_year_time()
    # get_start_end_time_week_time()


