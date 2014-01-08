from pymongo import MongoClient

class ApiDB(object):
	def __init__(self):
		self.client = MongoClient('mongodb://localhost:27017/')

	def choose_database(self, database_name):
		self.db = self.client[database_name]

	def choose_collection(self, collection_name):
		self.collection = self.db[collection_name]

	def insert_data(self, kwargs):
		self.collection.insert(kwargs)

	def get_data(self):
		return self.collection.find()


if __name__ == '__main__':
	apidb=ApiDB()
	apidb.choose_database('testdb')
	apidb.choose_collection('unicorns')
	apidb.insert_data({'name': 'Kate', 'role':'student', 'age':29})
	for row in apidb.get_data():
		print row