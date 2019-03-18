import os
import glob
import importlib
import inspect
from interfaces.uiot_service import UIoTService



class Dispatcher():

        def __init__(self):
                kf = self.get_known_formulas()
                print(kf)
                

        def send(self, data):
                        interface = self.__interfaces[data['interface_type']]
                        params = data['params']
                        return interface().send(params)



        def get_known_formulas(self):
                known_formulas = {}
                current_dir = os.path.join(os.path.dirname(os.path.abspath('interfaces/*.py')))
                current_module_name = os.path.splitext(os.path.basename(current_dir))[0]
                print (current_module_name)
                for file in glob.glob(current_dir + "/*.py"):
                        name = os.path.splitext(os.path.basename(file))[0]
                        # Ignore __ files
                        if name.startswith("__"):
                                continue
                        module = importlib.import_module("." + name,package=current_module_name)
                        print(module)
                        for member in dir(module):
                                handler_class = getattr(module, member)
                                print (name)
                                if handler_class and inspect.isclass(handler_class):
                                        known_formulas[member] = handler_class
                return known_formulas
        

Dispatcher()