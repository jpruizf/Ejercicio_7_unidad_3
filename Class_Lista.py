from Clase_nodo import Nodo

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_datos()
            self.__actual = self.__actual.get_siguiente()
            return dato
    def agregar_persona(self, persona):
        nodo = Nodo(persona)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    def insetar_persona(self, persona, posicion):

        if posicion < 0 or posicion > self.__tope:
            raise ValueError("Posicion de insercion no valida")
        nuevo_nodo = Nodo(persona)

        if posicion == 0:
            nuevo_nodo.set_siguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
        else:
            nodo_anterior = self.__comienzo
            for _ in range(posicion - 1):
                nodo_anterior = nodo_anterior.__get_siguiente__()
            
            nuevo_nodo.set_siguiente(nodo_anterior.set_siguiente())
            nodo_anterior.__get_siguiente__(nuevo_nodo)
        self.__tope += 1
    def mostrar_persona_por_posicion(self, posicion):
        if posicion < 0 or posicion > self.__tope:
            raise ValueError("Posicion de insercion no valida")
        aux = self.__comienzo
        nuevo = Nodo(posicion)
        if posicion is not None:
            print(f"Persona almacenada en la posicion ingresada >> {aux.__get_datos__()}")
            nuevo.__get_siguiente__()
    def listar_datos_docente_investigadores(self, carrera):
        aux = self.__comienzo
        while aux is not None:
            if aux.__get_datos__().__get_carrera__().lower() == carrera.lower():
                if aux.__get_datos__().__get_cargo__().lower() == 'docente investigador':
                    print(aux.__get_datos__().__get_apellido_nombre__())
                    aux = aux.__get_siguiente__()
    def contar_docentes_investidor_por_area(self, area):
        aux = self.__comienzo
        cant = 0
        while aux is not None:
            if aux.__get_datos__().__get_area_investigacion__().lower() == area.lowe():
                cant += 1
                aux = aux.__get_siguiente__()
        if cant > 0 :
            print(f"Total investigadores que trabajan en el area ingresada >> {cant}")
    def listado_persona(self):
        aux = self.__comienzo
        while aux is not None:
            print(f"Tipo de agente >> {aux.__get_datos__().__get_cargo__()}")
            print(f"Nombre >> {aux.__get_datos__().__get_apellido_nombre__()}")
            print(f"Sueldo >> {aux.__get_datos__().__get_sueldo__()}")
            aux = aux.__get_siguiente__()
    def listado_investigadores(self, categoria):
        aux = self.__comienzo
        total = 0.0
        while aux is not None:
            if categoria == str(aux.__get_datos__().__get_categoria__()):
                total += aux.__get_datos__().__get_importe__()
                print(f"Nombre >> {aux.__get_datos__().__get_apellido_nombre__()}")
                print(f"Importe extra >> {aux.__get_datos__().__get_importe__()}")
                print(f"Importe total >> {total}")
    def cartel(self):
        print("< Archivo json registrado satisfactoriamente >")
