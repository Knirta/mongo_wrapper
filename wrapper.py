from pymongo import MongoClient


class ApiDB(object):
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')

    def choose_database(self, database_name):
        self.db = self.client[database_name]

    def choose_collection(self, collection_name):
        self.collection = self.db[collection_name]

    def insert_data(self, data):
        self.collection.insert(data)

    def get_data(self, query=None, projection=None):
        cursor = self.collection.find(query, projection)
        return cursor

    def update_data(self, query=None, data=None):
        self.collection.update(query, data)

    def remove_data(self, query=None):
        self.collection.remove(query)

    def check_data(self, query, projection, field, name):
        pass
        #for_checking = self.collection.find_one(query, projection)
        #if for_checking[field] == name:
         #   return 'true'
        #return 'false'

if __name__ == '__main__':
    apidb = ApiDB()
    apidb.choose_database('testdb')
    apidb.choose_collection('unicorns')
    #apidb.insert_data({'name': 'Kate', 'role':'student', 'age':29})
    #apidb.insert_data({'name': 'Ed', 'role':'programmer', 'age':29})
    #cursor = apidb.get_data({'name':'Ed'}, {'_id': 0, 'name': 1, 'age': 1} )
    #for row in cursor:
    #    print row
    #apidb.remove_data({'name':'Kate'})
    #result = apidb.check_data({'age': 29}, {'name': 1}, 'name', 'Ed')
    #print result
