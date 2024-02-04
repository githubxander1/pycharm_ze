from bson import ObjectId
from pymongo import MongoClient

from CompanyProject.Fastbull.Api_fastbull.common.mongoDB_handler import MongoDBHandler

client = MongoDBHandler(
    host = '192.168.7.72',
    port = 27017,
    username = 'fastbull',
    password = 'IOE*2EW#OIWddOPcDWE')
    # da_name = 'fastbull_universal_test')
# MongoDB连接信息
# uri = "mongodb://fastbull:IOE*2EW#OIWddOPcDWE@192.168.7.72:27017/fastbull_universal_test?authSource=admin&authMechanism=SCRAM-SHA-1"
# 创建MongoDB客户端实例
# client = MongoClient(uri)
# MongoDB连接参数
# host = '192.168.7.72'
# port = 27017
# username = 'fastbull'
# password = 'IOE*2EW#OIWddOPcDWE'
#
# # 创建MongoDB客户端实例并连接到admin数据库进行身份验证
# client = MongoClient(host, port)
# client.admin.authenticate(username, password, mechanism='SCRAM-SHA-1')

# 连接到数据库
# db = client['fastbull_universal_test']
# db = client['mongo_quotes_ask_reply']
# 连接到目标数据库和集合


# 获取当前数据库的所有集合名称
# collections = db.list_collection_names()
# print(f'包含的表：{collections}')
# # 选择要查询的集合（表）
# collection_name = "mongo_quotes_ask_reply"  # 替换为您的集合名称
# collection = db[collection_name]
# #
# # # 查询集合中所有文档
# all_documents = collection.find()
# print(all_documents)

# 打印所有文档
# for document in all_documents:
#     print(document)
# 连接到目标数据库和集合
db = client.select_database('fastbull_news_test')
collection = db['comment_info']

# 删除指定ID的文档
document_id = "65bcbec1e506270008821266"
result = collection.delete_one({"_id": ObjectId(document_id)})

if result.deleted_count == 1:
    print(f"成功删除了ID为 {document_id} 的评论信息.")
else:
    print(f"未能找到ID为 {document_id} 的评论信息.")

# 关闭连接
client.close()
# 关闭连接
# client.close()