from pymongo import MongoClient

# 用你提供的连接字符串替换这里的<your_connection_string>
connection_string = "mongodb://fastbull:IOE*2EW#OIWddOPcDWE@192.168.7.72:27017/fastbull_quotes_test?authSource=admin"

# 创建MongoDB客户端
client = MongoClient(connection_string)

# 连接到你的数据库，默认情况下，数据库名称已经在连接字符串中指定（本例中为fastbull_quotes_test）
db = client['fastbull_quotes_test']
# print("连接成功到 MongoDB")
# 获取并打印MongoDB实例上的所有数据库名称
databases = client.list_database_names()
print("数据库名称:")
for database in databases:
    print(database)

# 获取并打印数据库中的所有集合（表）名称
# collections = db.list_collection_names()
# print("Collections in the database:")
# for collection in collections:
#     print(collection)

# 现在你可以操作这个数据库了，比如访问一个集合（collection）
# collection = db['your_collection_name']  # 替换your_collection_name为你实际的集合名称
#
# # 示例：插入一条数据
# sample_document = {"name": "Test Document", "content": "This is a flashing_icon document."}
# result = collection.insert_one(sample_document)
# print(f"Inserted document with ID: {result.inserted_id}")

# 记得关闭连接（虽然在现代驱动程序中这通常是自动管理的）
# client.close()
