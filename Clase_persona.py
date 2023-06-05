class Persona:
    __cuil: int
    __apellido: str
    __nombre: str
    __sueldo_basico: float
    __antiguedad: int
    def __init__(self):
        self.__cuil = 0
        self.__apellido = ""
        self.__nombre = ""
        self.__sueldo_basico = 0.0
        self.__antiguedad = 0
    def __get_cuil__(self):
        return self.__cuil
    def __get_apellido_nombre__(self):
        return self.__apellido,self.__nombre
    def __get_sueldo__(self):
        return self.__sueldo_basico
    def __get_antiguedad__(self):
        return self.__antiguedad