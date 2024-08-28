import json
import pandas as pd

# with open('数据.txt', 'rb') as f:
#     data = json.loads(f.read().decode(chardet.detect(f.read())['encoding']))

# txt转Excel
with open('正式_列表数据.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)
#
df = pd.json_normalize(data, record_path='bodyMessage', meta=['code', 'subCode', 'message'])
df.to_excel('output正式_列表数据.xlsx', index=False)

#统计
# import pandas as pd
# # 读取Excel表格
# df = pd.read_excel('output正式_列表数据.xlsx')
#
#
# # 划分reward列的值到不同的区间
# bins = [-float('inf'), 实例25_批量生成PPT版荣誉证书, 2, float('inf')]
# labels = ['[0,实例25_批量生成PPT版荣誉证书)', '[实例25_批量生成PPT版荣誉证书,2)', '[2,+)']
# df['reward_interval'] = pd.cut(df['reward'], bins=bins, labels=labels)
#
# # 对划分后的数据进行分组统计
# grouped = df.groupby('reward_interval').agg({'reward': 'count'})
#
# # 计算每个区间的比例
# total = grouped.sum()
# grouped['ratio'] = grouped['reward'] / total['reward']
#
# # 输出结果
# print('总数:', total['reward'])
# print(grouped)

# # 划分reward列的值到不同的区间
# bins = [0, 实例25_批量生成PPT版荣誉证书, 2, float('inf')]
# labels = ['[0,实例25_批量生成PPT版荣誉证书)', '[实例25_批量生成PPT版荣誉证书,2)', '[2,+)']
# df['reward_interval'] = pd.cut(df['reward'], bins=bins, labels=labels)
#
# # 对划分后的数据进行分组统计
# grouped = df.groupby('reward_interval').agg({'reward': 'count'})
#
# # 计算每个区间的比例
# total = grouped.sum()
# grouped['ratio'] = grouped['reward'] / total['reward']
#
# # 输出结果
# print('总数:', total['reward'])
# print(grouped)