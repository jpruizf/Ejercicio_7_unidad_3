from Clase_persona import Persona

class Docente(Persona):
    __carrera: str
    __materia: str
    __cargo: str
    __catedra: str
    def __init__(self):
        super().__init__()
        self.__carrera = ""
        self.__materia = ""
        self.__cargo = ""
        self.__catedra = ""
    def __get_carrera__(self):
        return self.__carrera
    def __get_materia__(self):
        return self.__materia
    def __get_cargo__(self):
        return self.__cargo
    def __get_catedra__(self):
        return self.__catedra