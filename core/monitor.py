import time
import threading
import os
from multiprocessing import Pool
# from termcolor import colored

class Monitor():

	"""
	Constructor
	"""
	def __init__(self, frequency=5, threads = 10):
		self.__frequency = frequency
        self.__pool = Pool(threads)
        self.db = client.LocalMongo


    def get_known_formulas(self):
        known_formulas = {}
        current_dir = os.path.join(os.path.dirname(os.path.abspath('formulas/*.py')))
        current_module_name = os.path.splitext(os.path.basename(current_dir))[0]
        for file in glob.glob(current_dir + "/*.py"):
             name = os.path.splitext(os.path.basename(file))[0]
             # Ignore __ files
             if name.startswith("__"):
                 continue
             module = importlib.import_module("." + name,package=current_module_name)
             for member in dir(module):
                 handler_class = getattr(module, member)
                 if handler_class and inspect.isclass(handler_class):
                     known_formulas[member] = handler_class
        return known_formulas

	def __get_formula(self):
        return list(self.db.formula.find())
        pass

    def __get_dataset(self):
        pass
    
    def __check_event(self):
        pass

	def run(self):
		while(True):
            formulas = self.__get_formulas()
            results = self.__pool.map(self.__check_event, formulas)
            
			# if self.__frequency == 0:
			# 	break
			time.sleep(self.__frequency)

	