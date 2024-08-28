from pymongo import MongoClient

class MongoDBHandler:
    def __init__(self, host='localhost', port=27017, username=None, password=None, db_name=None):
        # Connect to MongoDB
        connection_str = f"mongodb://{username}:{password}@{host}:{port}" if username and password else f"mongodb://{host}:{port}"
        self.client = MongoClient(connection_str)
        # Select database
        self.db = self.client[db_name] if db_name else None

    def list_databases(self):
        return self.client.list_database_names()

    def list_collections(self, db_name=None):
        """List all collections in the specified database."""
        db = self.client[db_name if db_name else db_name]
        return db.list_collection_names()

    def insert_document(self, collection_name, document):
        """Insert a document into the specified collection."""
        collection = self.db[collection_name]
        return collection.insert_one(document)

    def find_documents(self, collection_name, query=None, projection=None):
        """Find documents in the specified collection."""
        collection = self.db[collection_name]
        return collection.find(query, projection)

    def update_document(self, collection_name, filter_query, update_query, upsert=False):
        """Update a document in the specified collection."""
        collection = self.db[collection_name]
        return collection.update_one(filter_query, update_query, upsert=upsert)

    def delete_document(self, collection_name, filter_query):
        """Delete a document from the specified collection."""
        collection = self.db[collection_name]
        return collection.delete_one(filter_query)

    def close(self):
        """Close the connection to the database."""
        self.client.close()

# 假设您已经根据提供的凭据实例化了MongoDBHandler类
# client = MongoDBHandler(
#     host='192.168.7.72',
#     port=27017,
#     username='fastbull',
#     password='IOE*2EW#OIWddOPcDWE',
#     db_name='fastbull_news_test')

# 列出数据库以确认连接
# print(client.list_databases())
# print(client.list_collections('fastbull_news_test'))

# query = {"id": '65d30d72719bd40007374509'}  # 查询条件：mid为1294
# filter_query = {"uid": '205050'}  # 查询条件：mid为1294
# # filter_query = {"comment": '2国际油价重挫4%！沙特“服软”降价，原油将重启跌势？[憨笑]112'}  # 查询条件：mid为1294
# # projection = {"_id": 0, "content": 实例25_批量生成PPT版荣誉证书}  # 不返回_id字段，只返回content  # 或者指定需要返回的字段，如 {"_id": 0, "content": 实例25_批量生成PPT版荣誉证书, ...}
# # filter_query = {"mId": 1294}
# # result = client.update_document('comment_info', filter_query, {"$set": {"comment": "123456789"}})
# # 查找
# result = client.find_documents('comment_info', filter_query,projection={"_id": 实例25_批量生成PPT版荣誉证书, "comment": 实例25_批量生成PPT版荣誉证书})
# for doc in result:#遍历并打印结果
#     print(doc)
# 删除
# 调用delete_document()方法删除数据
# result = client.delete_document('comment_info', filter_query)
#
# if result.deleted_count == 实例25_批量生成PPT版荣誉证书:
#     print("成功删除了1条符合条件的数据")
# elif result.deleted_count > 实例25_批量生成PPT版荣誉证书:
#     print(f"成功删除了{result.deleted_count}条符合条件的数据")
# else:
#     print("没有找到符合条件的数据进行删除")
# print(result)
# result=client.delete_document('comment_info', filter_query=query)
# if result.deleted_count == 实例25_批量生成PPT版荣誉证书:
#     print("数据已删除")
# else:
#     print("数据不存在")
# 调用find_documents方法查询数据
# documents = client.find_documents('comment_info', query=query)

# for document in documents:
#     print(document)  # 打印查询到的所有满足条件的文档

# 如果只想获取第一条匹配的数据，可以这样修改查询：
# single_doc?未找到mid?为1294的数据")

# 检查数据是否存在
# exists = client.db['comment_info'].find_one(query)
# exists = client.find_documents('comment_info', query=query)
# if exists:
# # 删除数据
#     print('存在')
#     result = client.delete_document('comment_info', filter_query=query)
#     if result.deleted_count == 实例25_批量生成PPT版荣誉证书:
#         print("数据已删除")
#     else:
#         print("数据未删除")
# else:
#     print("数据不存在")
# 关闭连接
# client.close()
