import requests
import json


MAC = ""
CHIPSET = ""
N_REQUESTS = 10
# URL = 'http://localhost:8000/'
URL = 'http://192.168.43.6:8000/'

def register_client(mac="FF:FF:FF:FF:FF:FF", chipset="AMD 790FX"):
    payload = {
        "mac": mac,
        "chipset":chipset,
        "clientTime": 1000000000.1111,
        "tags": [
            "example-tag"
        ],
        "name": "Raspberry PI",
        "serial": "C210",
        "processor": "Intel I3",
        "channel": "Ethernet",
        "location": "-15.7757876:-48.077829"
    }
    response = requests.post(URL + 'client', data=json.dumps(payload), headers={'Content-Type': "application/json"})
    print(payload)
    print(response.json())
    
def register_service(mac="FF:FF:FF:FF:FF:FF", chipset="AMD 790FX"):
    payload = {
        "mac": mac,
        "chipset": chipset,
        "clientTime": 1000000000.1,
        "tags": [
            "example-tag"
        ],
        "number": 3,
        "name": "Get temp",
        "parameter": "temperature",
        "unit": "°C",
        "numeric": 1
    }
    response = requests.post(URL + 'service', data=json.dumps(payload), headers={'Content-Type': "application/json"})

def register_data(mac="FF:FF:FF:FF:FF:FF", chipset="AMD 790FX", data=0):
    payload = {
        "mac": mac,
        "chipset": chipset,
        "clientTime": 1000000000.1,
        "tags": [
            "example-tag"
        ],
        "sensitive": 1,
        "serviceNumber": 3,
        "values": [ data ]
    }
    response = requests.post(URL + 'data', data=json.dumps(payload), headers={'Content-Type': "application/json"})


if MAC and CHIPSET:
    register_client(mac=MAC, chipset=CHIPSET)
    register_service(mac=MAC, chipset=CHIPSET)
else:
    register_client()
    register_service()
    

for i in range (0, N_REQUESTS):
    print("Sending Request Number " + str(i))
    if MAC and CHIPSET:
        register_data(mac=MAC, chipset=CHIPSET, data=i)
    else:
        register_data(data=i+1)


