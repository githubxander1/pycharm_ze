from pymongo import MongoClient

class MongoDBHandler:
    def __init__(self, host='localhost', port=27017,username=None, password=None, db_name=None):
        self.client = MongoClient(host=host, port=port)
        self.authenticate=self.client.admin.authenticate(username, password, mechanism='SCRAM-SHA-1')
        self.db = self.client[db_name] if db_name else None

    def select_database(self, db_name):
        self.db = self.client[db_name]

    def insert_one(self, collection_name, document):
        if not self.db:
            raise ValueError("No database selected")
        collection = self.db[collection_name]
        return collection.insert_one(document)

    def find(self, collection_name, filter_dict={}):
        if not self.db:
            raise ValueError("No database selected")
        collection = self.db[collection_name]
        return collection.find(filter_dict)

    def update_one(self, collection_name, filter_dict, update_dict):
        if not self.db:
            raise ValueError("No database selected")
        collection = self.db[collection_name]
        return collection.update_one(filter_dict, {'$set': update_dict})

    def delete_one(self, collection_name, filter_dict):
        if not self.db:
            raise ValueError("No database selected")
        collection = self.db[collection_name]
        return collection.delete_one(filter_dict)

# 使用示例
handler = MongoDBHandler(db_name='my_database')
handler.insert_one('users', {'username': 'test_user', 'password': 'test_password'})