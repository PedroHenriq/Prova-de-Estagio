import os
from pymongo import MongoClient


class LocalMongo():

	def __init__(self):
		client = MongoClient(os.environ['MONGO_HOST'], username=os.environ['MONGO_USER'], password=os.environ['MONGO_PWD'], authSource='LocalMongo')
		self.db = client.LocalMongo
	
	def send(self, data = [], collection = 'temp'):
		resultado = self.db[collection].insert_many(data)
		print(resultado)

	def get(self, collection = 'temp', parms = {}):
		formulas = list(self.db.formula.find(parms))
		print(formulas)
		return formulas



# LocalMongo().get()
# LocalMongo().send(
# 	{
# 		'Filter': {
# 			'service_names': [],
# 			'service_ids': [],
# 			'time': []
# 		},
# 		'Event':{
# 			'type': 'Quantity',
# 			'value': 100
# 		},
# 		'Formula': None,
# 		'Recipient':{
# 			'Type': 'UIoTService',
# 			'parms':{'service_name': 'MVP_SERVICE'}
# 		}
# 	}
# )