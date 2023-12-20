import requests
import pandas as pd
# headers = {
#     'token': 'U81HC5JM36sWt9hK0NM/Mw8RhtRkkvVXIRidU9Iui7eozJbFIrLaFeUebCrTRtTh0Aiz0L6TJRRBfJdRSmdPiOoI7pfZ7wCiodwluUBhl5YuLIQGa8f5UA4Lu4vMIs++geqkDezCcDqlf36f/nXL9fulK/anoMKEkNcspGNheg4=',
#     'deviceId': '28f7b12416cc40e6f92cd946241639c4',
#     'bDeviceId': '309d6307761eda92e10cb839017b1861',
#     'randomstr': 'UlqAItm2rTQXIjvyLC3bzGT7D6Erjzyb',
#     'MEMBER_STATUS': '0',
#     'murmur': 'f9b107a69041a5d3995117fedd8af55d'
# }
# 产品id: 1 - huiliao;9 - huihu;10 - huichacha;13 - huiketang;15 - fazzaco;25 - brokers_show;26 - Fastbull;
# 27 - brokers_view;28 - fx110;32 - Fastbull.live;33 - fx110_overseas;36 - wikiforex;
# 37 - fastbull_finance;10001 - broker_spread
activityid=186
productId=32
url = f'https://qrpromotionapitest.tostar.top/invite/rewardRecordListTest?activityId={activityid}'
headers = {
    "accept": "*/*",
    "productId": f'{productId}',
    "token": "0a4b697b631e4de6ab32692f8acd0cd0"
}

response = requests.get(url, headers=headers).json()
data = response['bodyMessage']
# Extract relevant fields into a list of dictionaries
results = []
for item in data:
    result = {
        'name': item['name'],
        'reward': item['reward'],
        'time': item['time'],
        'prize': item['prize'],
        'user': item['user']
    }
    results.append(result)
df = pd.DataFrame(results)
print(df)
# rewards=df['reward']
# print(rewards)

# Assuming you have extracted the data into a DataFrame called 'df'
# Convert the 'reward' column to a numeric data type
df['reward'] = pd.to_numeric(df['reward'])
# print(df['reward'])
# Filter the data for the 'reward' values in the specified intervals
interval1 = df[(df['reward'] >= 0) & (df['reward'] < 1)]['reward']
interval2 = df[(df['reward'] >= 1) & (df['reward'] < 2)]['reward']
interval3 = df[(df['reward'] >= 2)]['reward']
# print(interval3)
# print(len(interval3))

# Calculate the ratios
ratio1 = len(interval1) / len(df)
ratio2 = len(interval2) / len(df)
ratio3 = len(interval3) / len(df)

# Print the results as percentages
print(f'共{len(df)}个')
print(f'[0,1)的比例: {ratio1:.2%},共{len(interval1)}个')
print(f'[1,2)的比例: {ratio2:.2%},共{len(interval2)}个')
print(f'[2,+)的比例: {ratio3:.2%},共{len(interval3)}个')
# Export dataframe to Excel file
# if f'output{activityid}.xlsx' not ex
df.to_excel(f'output{activityid}.xlsx', index=False)