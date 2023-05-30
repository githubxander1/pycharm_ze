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

url = 'https://qrpromotionapitest.tostar.top/invite/rewardRecordListTest?activityId=186'
headers = {
    "accept": "*/*",
    "productId": '32',
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
    }
    results.append(result)
print(result)
# Convert list of dictionaries to a pandas dataframe
# df = pd.DataFrame(results)
# print(df)

# Export dataframe to Excel file
# df.to_excel('output186.xlsx', index=False)