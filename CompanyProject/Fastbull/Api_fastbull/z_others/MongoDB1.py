from bson import ObjectId
from pymongo import MongoClient

from CompanyProject.Fastbull.Api_fastbull.common.mongoDB_handler import MongoDBHandler

# client = MongoDBHandler(
#     host = '192.168.7.72',
#     port = 27017,
#     username = 'fastbull',
#     password = 'IOE*2EW#OIWddOPcDWE')
    # da_name = 'fastbull_universal_test')
# 1.1MongoDB连接信息
from pymongo import MongoClient

host = '192.168.7.72'
port = 27017
username = 'fastbull'
password = 'IOE*2EW#OIWddOPcDWE'

# 创建一个MongoClient对象
client = MongoClient(host, port, username=username, password=password)

# 现在您可以使用client对象来访问数据库
# 例如，获取所有的数据库名称：
databases = client.list_database_names()
print(databases)
# # 创建MongoDB客户端实例
# client = MongoClient(host, port)
# # , mechanism='SCRAM-SHA-1'
# # 连接到admin数据库并进行身份验证
# client.admin.authenticate(username, password)

# 现在你可以使用client来操作各个数据库和集合了

# 1.2创建MongoDB客户端实例
# uri = "mongodb://fastbull:IOE*2EW#OIWddOPcDWE@192.168.7.72:27017/fastbull_universal_test?authSource=admin&authMechanism=SCRAM-SHA-1"
# client = MongoClient(uri)

# 2连接到数据库
db = client['fastbull_universal_test']
# db = client['mongo_quotes_ask_reply']

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
base=client.list_databases()
print(base)
# db = client.select_database('fastbull_news_test')
# collection = db['comment_info']
#
# # 删除指定ID的文档
# document_id = "65bcbec1e506270008821266"
# result = collection.delete_one({"_id": ObjectId(document_id)})
#
# if result.deleted_count == 1:
#     print(f"成功删除了ID为 {document_id} 的评论信息.")
# else:
#     print(f"未能找到ID为 {document_id} 的评论信息.")

# 关闭连接
# client.close()
# 关闭连接
# client.close()