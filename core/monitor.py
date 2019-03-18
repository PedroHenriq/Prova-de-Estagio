import time
import threading
# from termcolor import colored

class Monitor():

	"""
	Constructor
	"""
	def __init__(self, frequency=5):
		self.__frequency = frequency


	def __get_formula(self):
        pass

    def __get_dataset(self):
        pass
    
    def __check_event(self):
        pass

	def run(self):
		while(True):
			pass
			if self.__frequency == 0:
				break
			time.sleep(self.__frequency)

	