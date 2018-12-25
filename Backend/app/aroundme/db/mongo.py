from pymongo.mongo_client import MongoClient

class MongoConnector:

    @staticmethod
    def get_connection(db_name, collection_name):
        client = MongoClient("mongodb://localhost:27017/");
        db = client[db_name];
        collection = db[collection_name];
        return collection;




