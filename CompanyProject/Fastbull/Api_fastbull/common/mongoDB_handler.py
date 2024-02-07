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
        db = self.client[db_name if db_name else self.db_name]
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
client = MongoDBHandler(
    host='192.168.7.72',
    port=27017,
    username='fastbull',
    password='IOE*2EW#OIWddOPcDWE',
    db_name='fastbull_universal_test')

# 列出数据库以确认连接
print(client.list_databases())

# 检查数据是否存在
exists = client.db['mongo_quotes_ask_reply'].find_one({'mld': 1288})
if exists:
    # 删除数据
    result = client.delete_document('mongo_quotes_ask_reply', {'mld': 1288})
    if result.deleted_count == 1:
        print("数据已删除")
    else:
        print("数据不存在")
else:
    print("数据不存在")
# 关闭连接
client.close()
