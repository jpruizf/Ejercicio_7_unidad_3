from Class_Lista import Lista

def menu():
    clase_lista = Lista()
    print("1. Insertar a agentes a la colección.")
    print("2. Agregar agentes a la colección.")
    print("3. Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
    print("4. Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
    print("5. Dada un área de investigación, contar la cantidad de agentes que son docente investigador, y la cantidad de investigadores que trabajen en ese área.")
    print("6. Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
    print("7. Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.")
    print("8. Almacenar los datos de todos los agentes en el archivo “personal.json”")
    print("9. Salir")
    opcion = input("Seleccione una de las opciones dadas >> ")
    while opcion != 0:
        if opcion == '1':
            persona = input("Ingrese nombre y apellido del docente ha registrar >>")
            posicion = int(input("Ingrese la posicion de la lista >> "))
            clase_lista.insetar_persona(persona,posicion)
        elif opcion == '2':
            persona = None
            persona = input("Ingrese nombre y apellido del docente ha registrar >>")
            clase_lista.agregar_persona(persona)
        elif opcion == '3':
            posicion = int(input("Ingrese la posicion de la lista >> "))
            clase_lista.mostrar_persona_por_posicion(posicion)
        elif opcion == '4':
            carrera = input("Ingrese carrera del docente >>")
            clase_lista.listado_investigadores(carrera)
        elif opcion == '5':
            area = input("Ingrese el area de investigacion >> ")
            clase_lista.contar_docentes_investidor_por_area(area)
        elif opcion == '6':
            clase_lista.listado_persona()
        elif opcion == '7':
            categoria = str(input("Ingrese la categoria del docente >> "))
            clase_lista.listado_investigadores(categoria)
        elif opcion == '8':
            clase_lista.cartel()
        elif opcion == '9':
            return 0
        print("1. Insertar a agentes a la colección.")
        print("2. Agregar agentes a la colección.")
        print("3. Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
        print("4. Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print("5. Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.")
        print("6. Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print("7. Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.")
        print("8. Almacenar los datos de todos los agentes en el archivo “personal.json”")
        opcion = input("Seleccione una de las opciones dadas >> ")

if __name__ == '__main__':
    menu()