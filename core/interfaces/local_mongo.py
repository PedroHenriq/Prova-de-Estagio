import os
from pymongo import MongoClient


class LocalMongo():

	def __init__(self):
		# MONGO_URI = "mongodb://{2}/LocalMongo".format(os.environ['MONGO_HOST'])
		client = MongoClient(os.environ['MONGO_HOST'], username=os.environ['MONGO_USER'], password=os.environ['MONGO_PWD'], authSource='LocalMongo')
		self.db = client.LocalMongo
	
	def send(self, data):
		resultado = self.db.formula.insert_one(data)
		print(resultado)

	def get(self, parms = {}):
		formulas = list(self.db.formula.find(parms))
		print(formulas)



LocalMongo().get()
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