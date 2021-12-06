from pymongo import MongoClient

mongoUrl = 'mongodb://localhost:27017/'
dbName = "indeed"
try:
    connection = MongoClient(mongoUrl)[dbName]
    print('Database Connected TO: ', mongoUrl, dbName)
except Exception as e:
    # print(e)
    print('Database not Connected')


def connect_to_collection(coll_name):
    if coll_name in connection.list_collection_names():
        collection = connection[coll_name]
        return collection
    else:
        collection = connection.create_collection(coll_name)
        return collection
