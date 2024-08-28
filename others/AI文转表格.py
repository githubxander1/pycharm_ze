import pandas as pd

# 创建一个字典列表，其中每个字典代表一行数据
data = [
    {
        '标题': '测试getStockPage接口基本功能',
        '请求头': '{"clientType": 4,"langId": 1,"uid": "123456"}',
        '请求体': '{"pageIndex": 1,"pageSize": 20}',
        '预期状态码': 200,
        '预期结果': '返回第一页的股票数据，包括20条记录，每条记录包含股票基本信息和市场数据。',
        '实际结果': '按照预期返回了20条股票数据，每条数据包含stockId、stockName、currentPrice等字段。'
    },
    # 添加其他测试案例...
]

# 创建DataFrame
df = pd.DataFrame(data)

# 导出到Excel文件
df.to_excel('测试结果.xlsx', index=False)
