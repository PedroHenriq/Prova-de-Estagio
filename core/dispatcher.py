from interfaces.uiot_service import UIoTService


class Dispatcher():

	def __init__(self):
        self.__interfaces = {
            'UIoTService': UIoTServices
        }

	def send(self, data):
        interface = self.__interfaces[data['interface_type']]
        params = data['params']
        return interface().send(params)

