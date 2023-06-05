from Clase_docente import Docente

class Investigador_docente(Docente):
    __incent_investigacion: str
    __importe_extra: float
    def __init__(self):
        super().__init__()
        self.__incent_investigacion = ""
        self.__importe_extra = 0.0
    def __get_incentivos_investigacion__(self):
        return self.__incent_investigacion
    def __get_importe__(self):
        return self.__importe_extra