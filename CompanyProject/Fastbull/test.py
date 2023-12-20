import json

from pymongo import MongoClient

# 创建MongoDB连接
client = MongoClient("mongodb://Fastbull:IOE*2EW#OIWddOPcDWE@192.168.7.72:27017/fastbull_macro_data_test?authSource=admin")

# 访问数据库和集合
db = client.fastbull_macro_data_test
collection = db.strategy_signal

# 构建查询条件
query = {
    "openTime": {"$gte": 1693497600000, "$lt": 1696089600000},
    "status": 1
}

# 执行查询
result = collection.find(query)

# 处理查询结果
for document in result:
    # 将ObjectId对象转换为字符串
    document['_id'] = str(document['_id'])
    print(json.dumps(document, indent=4, ensure_ascii=False))