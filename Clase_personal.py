from Clase_persona import Persona

class Personal_apoyo(Persona):
    __categoria: str
    def __init__(self):
        super().__init__()
        self.__categoria = ""
    def __get_categoria__(self):
        return self.__categoria