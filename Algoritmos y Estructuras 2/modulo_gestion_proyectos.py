"""
Parcial IV. TDA. Listas Enlazadas, Pilas y Colas

Elaborado por:

- Jesús Araujo. C.I: 31.200.562
- Lai Chang. C.I: 31.335.078
- Santiago Perrotta. C.I: 31.014.123
"""


from datetime import datetime
import json, pilas_colas, os
from clases_proyectos_tareas_subtareas import *

# Primero Modulo del proyecto
class Gestion_proyectos:

    def __init__ (self):
        self.lista_proyectos = []
        self.menu_opciones()
    
    def menu_opciones(self):
        while True:
            print('-' * 40)
            print('           Menú de Opciones')
            print('-' * 40)
            print("1- Crear Proyectos")
            print("2- Modificar Proyectos")
            print("3- Consultar Proyectos")
            print("4- Eliminar Proyectos")
            print("5- Listar Proyectos")
            print("6- Salir del menú")
            print("")

            opc = input("Escoja la opción que desea ejecutar: ")

            self.cargar_proyectos_desde_archivo()
                
            if opc == "1":
                self.crear_proyecto()
            elif opc == "2":
                self.modificar_proyecto()
            elif opc == "3":
                self.consultar_proyectos()
            elif opc == "4":
                self.eliminar_proyecto()
            elif opc == "5":
                self.listar_proyectos()
            elif opc == "6":
                break
            else:
                print("Opción no es válida. Por favor, elija una opción del 1 al 6.")
    
    def cargar_proyectos_desde_archivo(self):
        #se verifica si el archivo existe
        if not os.path.exists("proyectos.txt"):
            print("El archivo 'proyectos.txt' no existe.")
            return

        with open("proyectos.txt", "r") as archivo:
            contenido = archivo.read().strip()

        if not contenido:
            print("El archivo 'proyectos.txt' está vacío.")
            return

        proyectos_datos = contenido.split("\n\n")  #se divide por bloques de proyectos

        for proyecto_str in proyectos_datos:
            lineas = proyecto_str.split("\n")
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
            self.lista_proyectos.append(proyecto)

    def crear_proyecto(self):
        pregunta = input("Desea ingresar los datos manualmente o de forma automática? (M/A) ")

        with open("proyectos.txt", "a") as archivo:  #abrir archivo en modo de anexado
            if pregunta.lower() == "m":
                cant_proyectos = int(input("Cuantos proyectos deseas crear: "))

                for i in range(cant_proyectos):
                    #se pide el ingreso de datos de forma manual
                    id = int(input("Indique el id del proyecto: "))
                    nombre = input("Indique el nombre del proyecto: ")
                    descripcion = input("Indique los detalles del proyecto: ")
                    dia1 = int(input("Introduce el día de inicio del proyecto: "))
                    mes1 = int(input("Introduce el mes de inicio del proyecto: "))
                    anio1 = int(input("Introduce el año de inicio del proyecto: "))
                    fecha_de_inicio = datetime(anio1, mes1, dia1)
                    dia2 = int(input("Introduce el día de vencimiento del proyecto: "))
                    mes2 = int(input("Introduce el mes de vencimiento del proyecto: "))
                    anio2 = int(input("Introduce el año de vencimiento del proyecto: "))
                    fecha_de_vencimiento = datetime(anio2, mes2, dia2)
                    estado_actual = input("Estado actual del proyecto: ")
                    empresa = input("Nombre de la empresa del proyecto: ")
                    gerente = input("Gerente del proyecto: ")
                    cantidad = int(input("Número de integrantes del equipo: "))
                    equipo = []

                    for j in range(cantidad):
                        integrante = input(f"Escribe el {j+1} integrante del equipo: ")
                        equipo.append(integrante)

                    # Creamos un objeto de tipo proyecto
                    proyecto = Proyectos(id, nombre, descripcion, fecha_de_inicio, fecha_de_vencimiento, estado_actual, empresa, gerente, equipo)
                    # Agregar proyecto a la lista de proyectos
                    self.lista_proyectos.append(proyecto)

                    # Escribir detalles del proyecto en el archivo
                    archivo.write(f"{proyecto}\n\n")

                print("\nProyectos Creados")
            else:
                # Ingresar los datos de forma automática de un archivo .json
                with open("datos_prueba_proyecto.json", "r") as json_file:
                    datos = json.load(json_file)
                    for proyecto_data in datos["proyectos"]:
                        proyecto = Proyectos(
                            proyecto_data["identificador"],
                            proyecto_data["titulo"],
                            proyecto_data["detalles"],
                            datetime.strptime(proyecto_data["inicio"], "%Y-%m-%d"),
                            datetime.strptime(proyecto_data["vencimiento"], "%Y-%m-%d"),
                            proyecto_data["condicion"],
                            proyecto_data["organizacion"],
                            proyecto_data["responsable"],
                            proyecto_data["grupo"]
                        )
                        self.lista_proyectos.append(proyecto)

                        # Escribir detalles del proyecto en el archivo
                        archivo.write(f"{proyecto}\n\n")

                print("\nProyectos Creados")
        

    def modificar_proyecto(self):
        if len(self.lista_proyectos) == 0:
            print("No hay proyectos disponibles para modificar")
        else:
            pedir_id = int(input("Ingresar el id del proyecto que desea modificar: "))
            bandera = False  # esta bandera es para verificar si el id de ese proyecto existe

            for i in self.lista_proyectos:
                if i.id == pedir_id:
                    # ingreso de datos para modificar el proyecto
                    i.id = int(input("Indique el id del proyecto: "))
                    i.nombre = input("Indique el nombre del proyecto: ")
                    i.descripcion = input("Indique los detalles del proyecto: ")
                    dia1 = int(input("Introduce el día de inicio del proyecto: "))
                    mes1 = int(input("Introduce el mes de inicio del proyecto: "))
                    anio1 = int(input("Introduce el año de inicio del proyecto: "))
                    i.fecha_de_inicio = datetime(anio1, mes1, dia1)
                    dia2 = int(input("Introduce el día de vencimiento del proyecto: "))
                    mes2 = int(input("Introduce el mes de vencimiento del proyecto: "))
                    anio2 = int(input("Introduce el año de vencimiento del proyecto: "))
                    i.fecha_de_vencimiento = datetime(anio2, mes2, dia2)
                    i.estado_actual = input("Estado actual del proyecto: ")
                    i.empresa = input("Nombre de la empresa del proyecto: ")
                    i.gerente = input("Gerente del proyecto: ")
                    cantidad = int(input("Número de integrantes del equipo: "))
                    equipo = []

                    for j in range(cantidad):
                        integrante = input(f"Escribe el {j+1} integrante del equipo: ")
                        equipo.append(integrante)

                    i.equipo = equipo
                    bandera = True

            # Reescribir el archivo con los proyectos actualizados
            with open("proyectos.txt", "w") as archivo:
                for proyecto in self.lista_proyectos:
                    archivo.write(f"{proyecto}\n\n")

            # Condición para indicar que no existe ese proyecto que seleccionó el usuario
            if not bandera:
                print("Ese proyecto no existe por lo tanto no se puede modificar")
            else:
                print("\nProyecto Modificado")
        
    
    def consultar_proyectos(self):
        if len(self.lista_proyectos) == 0:
            print("No hay proyectos para consultar")
        else:
            pedir_id = int(input("Ingresar el id del proyecto que desea consultar: "))
            bandera = False # esta bandera es para verificar si el id de ese proyecto existe

            for i in self.lista_proyectos:
                if i.id == pedir_id:
                    print("id del proyecto: " + str(i.id))
                    print("nombre del proyecto: " + str(i.nombre))
                    print("descripcion del proyecto: " + str(i.descripcion))
                    print("fecha de inicio del proyecto: " + str(i.fecha_de_inicio))
                    print("fecha de vencimiento del proyecto: " + str(i.fecha_de_vencimiento))
                    print("estado actual del proyecto: " + str(i.estado_actual))
                    print("empresa del proyecto: " + str(i.empresa))
                    print("gerente del proyecto: " + str(i.gerente))
                    print("equipo del proyecto: " + str(i.equipo))
                    bandera = True

            # condicion para indicar que no existe ese proyecto que seleccione el usuario
            if bandera is not True:
                print("Ese proyecto no existe por lo tanto no se puede consultar")
            else:
                print("Proyecto Consultado")


    def eliminar_proyecto(self):
        if len(self.lista_proyectos) == 0:
            print("No hay proyectos para eliminar")
            return

        pedir_id = int(input("Ingresar el id del proyecto que desea eliminar: "))
        proyecto_eliminado = None

        for proyecto in self.lista_proyectos:
            if proyecto.id == pedir_id:
                proyecto_eliminado = proyecto
                self.lista_proyectos.remove(proyecto)
                print("Proyecto Eliminado")
                break
        
        if proyecto_eliminado:
            self.actualizar_archivo_proyectos()
        
    def listar_proyectos(self):
        if len(self.lista_proyectos) == 0:
            print("No hay proyectos para listar")
        else:

            for i in self.lista_proyectos:
                print("id del proyecto: " + str(i.id))
                print("nombre del proyecto: " + str(i.nombre))
                print("descripcion del proyecto: " + str(i.descripcion))
                print("fecha de inicio del proyecto: " + str(i.fecha_de_inicio))
                print("fecha de vencimiento del proyecto: " + str(i.fecha_de_vencimiento))
                print("estado actual del proyecto: " + str(i.estado_actual))
                print("empresa del proyecto: " + str(i.empresa))
                print("gerente del proyecto: " + str(i.gerente))
                print("equipo del proyecto: " + str(i.equipo))
                print("")

    def actualizar_archivo_proyectos(self):
        with open("proyectos.txt", "w") as archivo:
            for proyecto in self.lista_proyectos:
                archivo.write(f"ID: {proyecto.id}\n")
                archivo.write(f"Nombre: {proyecto.nombre}\n")
                archivo.write(f"Descripción: {proyecto.descripcion}\n")
                archivo.write(f"Fecha de Inicio: {proyecto.fecha_de_inicio.strftime('%Y-%m-%d')}\n")
                archivo.write(f"Fecha de Vencimiento: {proyecto.fecha_de_vencimiento.strftime('%Y-%m-%d')}\n")
                archivo.write(f"Estado Actual: {proyecto.estado_actual}\n")
                archivo.write(f"Empresa: {proyecto.empresa}\n")
                archivo.write(f"Gerente: {proyecto.gerente}\n")
                archivo.write(f"Equipo: {', '.join(proyecto.equipo)}\n\n")
    
    def get_lista_proyectos(self):
        return self.lista_proyectos

#Gestion_proyectos()

# ================================== TAREAS PENDIENTES A REALIZAR ==========================================

"""

1- falta la parte de pilas y colas de segundo modulo
2- Modulo de Reportes
3- Probar Funcionamiento
4- ver si se puede automatizar mejor como por ejemplo en los metodos de:

    (Insertar, Actualizar. Modificar)
    nota: en esos metodo mencionados use la entrada de datos de forma manual, pero hay otros metodo donde
    si esta de fomra automatica, leyendo un archivo .json 

    info extra: no se hacer una forma automatizada de esos metodos al menos de que se creen mas archivos .json,
    pero es bastante tedioso

5- Ver lo del modulo de importacion y exportacion de datos (aunque basicamente creo que se refiere al archivp .json y todo eso)

"""