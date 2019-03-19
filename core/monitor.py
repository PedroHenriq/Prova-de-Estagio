import time
import threading
import os
import glob
import inspect
import importlib


from multiprocessing.dummy import Pool
from pymongo import MongoClient

from dispatcher import Dispatcher

# from termcolor import colored


class Monitor():

    """
    Constructor
    """
    def __init__(self, frequency=5, threads = 10):
        self.__frequency = frequency
        self.__pool = Pool(threads)

        self.__event_types = {
            'Quantity': self.__quantity_event,
            'Time': self.__time_event,
            'Bool': self.__bool_event
        }

        client = MongoClient(os.environ['MONGO_HOST'], username=os.environ['MONGO_USER'], password=os.environ['MONGO_PWD'], authSource='LocalMongo')
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

    def __get_formulas(self):
        return list(self.db.formula.find())

    def __get_dataset(self, mongo_filter):
        return list(self.db.data.find(mongo_filter))
    
    def __check_event(self, formula):
        service_names = formula['Filter']['service_names']
        service_ids = formula['Filter']['service_ids']
        time = formula['Filter']['time']
        mongo_filter = self.mount_mongo_filter(service_names, service_ids, time)

        dataset = self.__get_dataset(mongo_filter)
        print("length of dataset: " + str(len(dataset)))
        if(self.__event_types[formula['Event']['type']](dataset, formula['Event'])):
            if formula['Formula']:
                pass
                #TODO
                # self.get_known_formulas()[formula['Formula']].send(self.get_known_formulas()[formula['Formula']](dataset))
            else:
                print(formula['Recipient'])
                interface_type = formula['Recipient']['Type']
                params = formula['Recipient']['parms']
                params['dataset'] = dataset
                return Dispatcher().send({
                    'interface_type': interface_type,
                    'params': params
                })

    def __quantity_event(self, dataset, event):
        return len(dataset) >= event['value']
        pass

    def __time_event(self, dataset, event):
        pass

    def __bool_event(self, dataset, event):
        pass

    def mount_mongo_filter(self, service_names, service_ids, time):
        #TODO
        return {}



    def run(self):
        while(True):
            formulas = self.__get_formulas()
            results = self.__pool.map(self.__check_event, formulas)
            print(results)

            # if self.__frequency == 0:
            # 	break
            time.sleep(self.__frequency)

Monitor().run()