import requests
import json

class UIoTService():

	def __init__(self):
		pass

	def send(self, data):
		print("ENVIO PELA INTERFACE")
		print(len(data))

		response = requests.post('http://192.168.43.144:8000/data', data=json.dumps(data), headers={'Content-Type': "application/json"})
		print("response: " + str(response.json()))

		return True

	def get(self):
		pass

