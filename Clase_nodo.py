from Clase_persona import Persona

class Nodo:
    __persona: Persona()
    __siguiente: object
    def __init__(self, persona):
        self.__persona = persona
        self.__siguiente = None
    def set_siguiente(self,siguiente):
        '''Asigna el nodo siguiente que va ha ser insertado en la lista'''
        self.__siguiente = siguiente
    def __get_siguiente__(self):
        return self.__siguiente
    def __get_datos__(self):
        '''Muestra datos de la clase persona'''
        return self.__persona