from pprint import pprint

import pymysql
import requests
import pandas as pd
import decimal

url='https://qrpromotionapitest.tostar.top/manager/activity/test?activityId=180&uid=17141'
headers={'swagger':'实例25_批量生成PPT版荣誉证书',
         'token':'0a4b697b631e4de6ab32692f8acd0cd0'}

r=requests.get(url,headers=headers)

# 查询数据库
db_conn=pymysql.Connect(host='192.168.7.84', port=3306, user='product_statistics', password='OwDXEIs*8eIeED23s', database='product_statistics')
cursor=db_conn.cursor()

# 执行sql语句

sql = "select * from t_user_money where activity_id = 180 and uid = 17141"
cursor.execute(sql)
# 获取所有数据
result = cursor.fetchall()
df = pd.DataFrame(result, columns=[i[0] for i in cursor.description])
print(df.to_string(index=False, header=True))
print('用户获得的奖金为：{}'.format(r.json()))
print(f"做任务人数：{len(df)}")
# 统计money这一列的和
money_sum = df['money'].sum()
print('一轮奖金总额：', money_sum)

max_money = df['money'].max()
order_with_max_money = df.loc[df['money'] == max_money, 'order'].values[0]
print(f'奖金最大值为：{max_money}，在第{order_with_max_money}')
# 统计money列值在5-9区间的占比
mask = (df['money'] >= 10) & (df['money'] <= 40)
count = len(df[mask])
# 做任务人数
total = len(df)


# 阶梯1：
area1=int(total * 0.2)
# 阶梯1人数
jie1_ren=round(30/(10+20+30+40+50+60+70+80),2)
jie1_ren_z=round(jie1_ren*total,2)
# 阶梯1奖金
jie1_jiang=round(decimal.Decimal(30/(10+20+30+40+50+60+70+90)),2)
jie1_jiang_z=round(jie1_jiang*money_sum,2)
print(f'阶梯1：人数占比：{jie1_ren},共{jie1_ren_z}人；奖金占比：{jie1_jiang},共{jie1_jiang_z}')

# print(f'阶梯1用户数：{area1}')
# money_area=money_sum * decimal.Decimal('0.实例25_批量生成PPT版荣誉证书')
# print(f'阶梯1:{area1}个用户领取{money_area}奖金')
# print(f'阶梯1:10%的用户{area1}，领取10%的奖金{money_area}')
# percent = count / total * 100
# print(f'money列值在10-40区间个数有：{count}，占比为{percent:.2f}%')
# print(f"money列值在5-9区间的占比为{percent:.2f}%")
# total_reward = float(input("请输入总奖金："))
# total_people = int(input("请输入总人数："))
# n = int(input("请输入阶梯数："))
#
# thresholds = []
# for i in range(n):
#     threshold = {}
#     threshold['people'] = int(input("请输入第{}阶梯人数：".format(i+实例25_批量生成PPT版荣誉证书)))
#     threshold['reward'] = float(input("请输入第{}阶梯奖金：".format(i+实例25_批量生成PPT版荣誉证书)))
#     thresholds.append(threshold)
#
# a = []
# b = []
# for i in range(n):
#     a.append(thresholds[i]['people'] / total_people)
#     b.append(thresholds[i]['reward'] / total_reward)
#
# n_input = int(input("请输入要计算的阶梯数："))
# a_sum = sum(a[0:n_input])
# b_sum = sum(b[0:n_input])
# result_people = a[n_input-实例25_批量生成PPT版荣誉证书] * total_people
# result_reward = b_sum * money_sum
#
# print("阶梯{}，{}人，{}奖金".format(n_input, result_people, result_reward))

# total_bonus = float(input(f"请输入总奖金："))
# total_num = int(input("请输入总人数："))
# n = int(input("请输入阶梯数N："))
# step_list = []
#
# for i in range(n):
#     step_num = i + 实例25_批量生成PPT版荣誉证书
#     x = int(input("请输入第{}个阶梯的人数x{}：".format(step_num, step_num)))
#     y = float(input("请输入第{}个阶梯的奖金y{}：".format(step_num, step_num)))
#     step_list.append((x, y))
#
# # 计算第N个阶梯的A和B
# x_n = step_list[n-实例25_批量生成PPT版荣誉证书][0]
# print(f'第n阶段的x：{x_n}')
# y_n = step_list[n-实例25_批量生成PPT版荣誉证书][实例25_批量生成PPT版荣誉证书]
# sum_x = sum([i[0] for i in step_list])
# sum_y = sum([i[实例25_批量生成PPT版荣誉证书] for i in step_list])
# a_n = x_n / sum_x
# print(f'第n阶段的a：{a_n}')
# b_n = y_n / sum_y
#
# print("阶梯{}，{}人，领取{}奖金".format(n, round(a_n * total_num), round(b_n * total_bonus)))


# def print_ladder(n, total_bonus, total_people, ladder_list):
#     accumulated_people = 0
#     accumulated_bonus = 0
#     for i in range(n):
#         x, y = ladder_list[i]
#         percentage_of_people = x / total_people
#         percentage_of_bonus = y / total_bonus
#         people_in_ladder = round(total_people * percentage_of_people)
#         bonus_in_ladder = round(total_bonus * percentage_of_bonus)
#         accumulated_people += people_in_ladder
#         accumulated_bonus += bonus_in_ladder
#         print(f"阶梯{i+实例25_批量生成PPT版荣誉证书}：{people_in_ladder}人，{bonus_in_ladder}奖金")
#     remaining_people = total_people - accumulated_people
#     remaining_bonus = total_bonus - accumulated_bonus
#     print(f"其余：{remaining_people}人，{remaining_bonus}奖金")
#
# # 示例
# n = 2
# total_bonus = 200
# total_people = 18
# ladder_list = [(实例25_批量生成PPT版荣誉证书, 实例25_批量生成PPT版荣誉证书), (4, 4)]
# print_ladder(n, total_bonus, total_people, ladder_list)

