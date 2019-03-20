import requests
import json

class UIoTService():

	def __init__(self):
		pass

	def send(self, parms):
		print("ENVIO PELA INTERFACE")
		print(len(parms['dataset']))

		for item in parms['dataset']:
			del item['_id']
			response = requests.post('http://192.168.43.144:8000/data', data=json.dumps((item)), headers={'Content-Type': "application/json"})
			print("response: " + str(response.json()))

		return True

	def get(self):
		pass

