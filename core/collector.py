import time
import threading
# from termcolor import colored
from interfaces.local_mongo import LocalMongo

class Collector():

	"""
	Constructor
	"""
	def __init__(self, interface=LocalMongo, frequency=5):
		self.__interface = interface
		self.__frequency = frequency

	def __collect(self):
		response = self.__interface.get()


    def __persist(self, data):
        pass 

	def run(self):
		while(True):
			self.__collect()
			if self.__frequency == 0:
				break
			time.sleep(self.__frequency)

	