import time
import threading
# from termcolor import colored
from interfaces.local_mongo import LocalMongo
from interfaces.listener import Listener

class Collector():
    def __init__(self, mongo_interface=LocalMongo, listener_interface=Listener, frequency=5):
        self.__mongo_interface = mongo_interface
        self.__listener_interface = listener_interface
        self.__frequency = frequency

    def __collect(self):
        response = self.__listener_interface().get()
        self.__persist(response)



    def __persist(self, data):
        if data['client']:
            self.__mongo_interface().send(collection='client', data=data['client'])
        if data['service']:
            self.__mongo_interface().send(collection='service', data=data['service'])
        if data['data']:
            self.__mongo_interface().send(collection='data', data=data['data'])



    def run(self):
        while(True):
            self.__collect()
            if self.__frequency == 0:
                break
            time.sleep(self.__frequency)

	
Collector().run()