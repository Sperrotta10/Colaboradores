"""
Parcial IV. TDA. Listas Enlazadas, Pilas y Colas

Elaborado por:

- Jesús Araujo. C.I: 31.200.562
- Lai Chang. C.I: 31.335.078
- Santiago Perrotta. C.I: 31.014.123
"""

from modulo_gestion_proyectos import *
from modulo_gestion_tareas import *
from modulo_reportes import *

def cargar_proyectos_desde_archivo():
        # Verifica si el archivo existe
        if not os.path.exists("proyectos.txt"):
            print("El archivo 'proyectos.txt' no existe.")
            return []

        with open("proyectos.txt", "r") as archivo:
            contenido = archivo.read().strip()

        if not contenido:
            print("El archivo 'proyectos.txt' está vacío.")
            return []

        proyectos_datos = contenido.split("\n\n")  # Divide por bloques de proyectos
        lista_proyectos_cargados = []

        for proyecto_str in proyectos_datos:
            lineas = proyecto_str.split("\n")
            try:
                id = int(lineas[0].split(": ")[1])
                nombre = lineas[1].split(": ")[1]
                descripcion = lineas[2].split(": ")[1]
                fecha_de_inicio = datetime.strptime(lineas[3].split(": ")[1], '%Y-%m-%d')
                fecha_de_vencimiento = datetime.strptime(lineas[4].split(": ")[1], '%Y-%m-%d')
                estado_actual = lineas[5].split(": ")[1]
                empresa = lineas[6].split(": ")[1]
                gerente = lineas[7].split(": ")[1]
                equipo = lineas[8].split(": ")[1].split(", ")

                proyecto = Proyectos(id, nombre, descripcion, fecha_de_inicio, fecha_de_vencimiento, estado_actual, empresa, gerente, equipo)
                lista_proyectos_cargados.append(proyecto)
            except IndexError:
                print(f"El formato del proyecto en '{proyecto_str}' no es correcto. Saltando este proyecto.")
            except ValueError as ve:
                print(f"Error al convertir datos para el proyecto en '{proyecto_str}': {ve}. Saltando este proyecto.")

        return lista_proyectos_cargados

def cargar_tareas_desde_archivo(id_proyecto):
    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
    except UnicodeDecodeError:
        try:
            with open("tareas.txt", "r", encoding="latin-1") as archivo:
                contenido = archivo.read().strip()
        except Exception as e:
            print(f"No se pudo abrir el archivo: {e}")
            return pilas_colas.Pila()

    if not contenido:
        print("El archivo 'tareas.txt' está vacío.")
        return pilas_colas.Pila()

    pila_tareas = pilas_colas.Pila()

    proyectos_datos = contenido.split("Proyecto ID: ")
    for proyecto_str in proyectos_datos:
        # Buscamos el proyecto con el ID correspondiente
        if f"{id_proyecto}" not in proyecto_str:
            continue

        lineas = proyecto_str.split("\n")
        tareas_inicio = -1

        for i, linea in enumerate(lineas):
            if linea.strip() == "Tareas:":
                tareas_inicio = i + 1
                break

        if tareas_inicio == -1:
            print(f"No se encontró la sección de tareas para el Proyecto ID {id_proyecto}.")
            return pilas_colas.Pila()  # Retorna una pila vacía si no se encontró la sección de tareas

        while tareas_inicio < len(lineas):
            if lineas[tareas_inicio].strip().startswith("ID ="):
                tarea_id = int(lineas[tareas_inicio].split("= ")[1].strip())
                titulo = lineas[tareas_inicio + 1].split("= ")[1].strip()
                cliente = lineas[tareas_inicio + 2].split("= ")[1].strip()
                detalles = lineas[tareas_inicio + 3].split("= ")[1].strip()
                fecha_inicio = datetime.strptime(lineas[tareas_inicio + 4].split("= ")[1].strip(), '%Y-%m-%d')
                fecha_vencimiento = datetime.strptime(lineas[tareas_inicio + 5].split("= ")[1].strip(), '%Y-%m-%d')
                condicion = lineas[tareas_inicio + 6].split("= ")[1].strip()
                avance = int(lineas[tareas_inicio + 7].split("= ")[1].strip().replace("%", ""))

                # Crear objeto Tareas y añadir a la pila
                tarea = Tareas(tarea_id, titulo, cliente, detalles, fecha_inicio, fecha_vencimiento, condicion, avance)
                pila_tareas.agregar(tarea)
                tareas_inicio += 8
            else:
                tareas_inicio += 1

        print(f"Tareas del Proyecto ID {id_proyecto} cargadas correctamente desde el archivo.")
        return pila_tareas  # Retornamos la pila con las tareas cargadas

    # Si no se encontró el proyecto con el ID dado
    print(f"No se encontró el Proyecto ID {id_proyecto} en el archivo.")
    return pilas_colas.Pila()  # Retorna una pila vacía si no se encontró el proyecto

while True:
    print('-' * 40)
    print('           Menú de Opciones')
    print('-' * 40)
    print("1- Gestionar proyectos")
    print("2- Gestionar Tareas")
    print("3- Gestionar Reportes")
    print("4- Salir del Menu\n")
    print('-' * 40)

    opc = input("Escoja la opción que desea ejecutar: ")

    lista_proyectos = cargar_proyectos_desde_archivo()
    for i in range(len(lista_proyectos)):
        pila_tareas = cargar_tareas_desde_archivo(i + 1)
        lista_proyectos[i].tareas = pila_tareas

    # Verificación de que la entrada es un entero válido
    try:
        opc = int(opc)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue  

    if opc == 1:
        #Gestion_proyectos()
        proyecto = Gestion_proyectos()
        #lista_proyectos = proyecto.get_lista_proyectos()

    elif opc == 2:
        Gestion_Tareas_prioridades(lista_proyectos)
    elif opc == 3:
        Reportes(lista_proyectos)
    elif opc == 4:
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 6.")