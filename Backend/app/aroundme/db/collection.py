import pymongo
from db.mongo import MongoConnector
from bson.objectid import ObjectId

class databaseServices:

    def savelocations(self,db_name, db_collection, request):
        connection = MongoConnector.get_connection(db_name, db_collection)
        connection.insert_one(request)
        response = {}
        response['status'] = 'success'
        return response

    def getEmpDetails(self, db_name, db_collection, id):
        connection = MongoConnector.get_connection(db_name, db_collection)
        value = str(id)
        cursor = connection.find({"id":value})
        print(cursor)
        records = []
        for document in cursor:
            print(document)
            records.append(document)
        return records

    def getAllEmpDetails(self,db_name,db_collection):
        connection = MongoConnector.get_connection(db_name, db_collection)
        records = []
        cursor = connection.find()
        for document in cursor:
            records.append(document)
        return records

