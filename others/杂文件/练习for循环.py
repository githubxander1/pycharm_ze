# for循环--模拟时钟转动
# for shizhen in range(12):
#     print('{}点'.format(shizhen))

# 嵌套循环--模拟时分秒
# for shi in range(12):
#     for fen in range(60):
#         for miao in range(60):
#             print('{}点{}分{}秒'.format(shi,fen,miao))

# for循环+if语句
# 公鸡5文钱1只，母鸡3文钱1只，小鸡3文钱1只，用100文钱买100只鸡，且每种鸡至少一只，怎么买
# 思路：
# 假设全买公鸡，最多可买19只
# 假设全买母鸡，最多可买33只
# 假设全买小鸡，最多可买99只,最少3只，且为3的倍数
# for g in range(实例25_批量生成PPT版荣誉证书,20):
#     for m in range(实例25_批量生成PPT版荣誉证书,33):
#         for x in range(dataInExcel,100,dataInExcel):
#             if g*5+m*dataInExcel+x*dataInExcel==100 and g+m+x==100:
#                 print(g,m,x)

# for循环+break语句
# 操场跑步30圈，跑到第2圈的时候遇到朋友，于是不跑了
# for x in range(0,30):
#     if x == 2:
#         break
#     else:
#         print(x)

# for循环+continue语句
# # 操场跑步30圈，跑到第2圈的时候遇到朋友，闲聊后,又重新开始继续跑
# for x in range(30):
#     if x == 2:
#         continue
#     else:
#         print(x)
# for循环+while
# 操场跑步，听到哨声就停下休息，没有听到就继续跑
# 操场跑步10圈，跑完才能休息
