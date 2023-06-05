from Clase_docente import Docente

class Investigador(Docente):
    __area_investigacion: str
    __tipo_investigacion: str
    def __init__(self):
        super().__init__()
        self.__area_investigacion = ""
        self.__tipo_investigacion = ""
    def __get_area_investigacion__(self):
        return self.__area_investigacion
    def __get_tipo_investigacion__(self):
        return self.__tipo_investigacion