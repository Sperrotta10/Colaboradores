"""
Parcial IV. TDA. Listas Enlazadas, Pilas y Colas

Elaborado por:

- Jesús Araujo. C.I: 31.200.562
- Lai Chang. C.I: 31.335.078
- Santiago Perrotta. C.I: 31.014.123
"""

from modulo_gestion_proyectos import *
from modulo_gestion_tareas import *

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

while True:
    print("\nMenu de Opciones")
    print("1- Gestionar proyectos")
    print("2- Gestionar Tareas")
    print("3- Gestionar ")
    print("4- Salir del Menu\n")

    opc = input("Escoja la opción que desea ejecutar: ")

    lista_proyectos = cargar_proyectos_desde_archivo()

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
        print("Hola 2")
    elif opc == 3:
        print("Hola 3")
    elif opc == 4:
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 6.")