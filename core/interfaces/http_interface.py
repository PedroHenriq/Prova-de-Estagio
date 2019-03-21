import requests
import json

class HTTP:

	def __init__(self):
		self._methods = {
			'post': requests.post,
			'put': requests.put,
		}

	def send(self, data):
		destiny = data['destiny']
		method = data['method']
		headers = data['headers']
		body = str(data['body'])
		data_to_be_sent = data['dataset']

		body = str(body).replace('{{data}}', str(data_to_be_sent))
		body = json.loads(body)

		print(body)
		response = self._methods[method](destiny, data=json.dumps(body), headers=headers)

		print("response: " + str(response.text) + " - "+ str(response.status_code))

		return response.text, response.status_code

	def get(self):
		pass


HTTP().send({
		"destiny": "http://localhost:8000/banana",
		"method": "post",
		"headers": {"Content-Type": "application/json"},
		"body": """{
			"oi": 1,
			"data":{
				"to":{
					"be":{
						"sent": {{data}},
						"not": 1
					},
					"not": 1,
					"not": 1
				},
				"not": 1
			},
			"not": 1
		}""",
		"dataset": [1,2,3,4]
})