from datetime import datetime
import json
from clases_proyectos_tareas_subtareas import *

# segundo modulo
class Gestion_Tareas_prioridades:
    def __init__ (self,lista_proyectos):
        self.lista_proyectos = lista_proyectos
        
        if self.verificar_proyecto(lista_proyectos):
            print("No hay proyectos para consultar tareas... Cree un proyecto!!")
            print("Dirigiendo al menú principal....")
            print("...................................")
        else:
            self.menu_opciones()

    def menu_opciones(self):
        while True:
            print("De que proyecto quiere investigar?: ")
            num = int(input("Escoja el id del proyecto: "))


            print("\nMenu de Opciones")
            print("1- Agregar nueva tarea")
            print("2- Insertar la posición de una tarea a otra posición")
            print("3- Eliminar tarea")
            print("4- Modificar tarea")
            print("5- Listar tareas")
            print("6- Salir del Menu\n")
            opc = input("Escoje la opcion que desea ejecutar: ")

            if opc == "1":
                self.agregar_tareas_al_final(num)
                
            elif opc == "2":
                self.insertar_tareas_posicion(num)

            elif opc == "3":
                self.eliminar_tareas(num)

            elif opc == "4":
                self.actualizar_tareas()

            elif opc == "5":
                self.listar_tareas()

            else:
                break

    def verificar_proyecto(self, lista_proyectos):
        if len(lista_proyectos) == 0:
            return True
        else:
            return False            

    def agregar_tareas_al_final(self, id):
        print(self.lista_proyectos[id - 1].nombre)
        pregunta = input("Desea ingresar los datos manualmente o de forma automática? (M/A) ")
        
        if pregunta.lower() == "m":
            titulo = input("Indique el titulo de la tarea: ")
            cliente = input("Indique el cliente de la tarea: ")
            detalles = input("Indique detalles de la tarea: ")
            dia1 = int(input("Indique el dia de inicio: "))
            mes1 = int(input("Indique el mes de inicio: "))
            anio1 = int(input("Indique el año de inicio: "))
            fecha_inicio = datetime(anio1, mes1, dia1)
            dia2 = int(input("Indique el dia de vencimiento: "))
            mes2 = int(input("Indique el mes de vencimiento: "))
            anio2 = int(input("Indique el año de vencimiento: "))
            fecha_vencimiento = datetime(anio2, mes2, dia2)
            condicion = input("Indique su condición: ")
            avance = int(input("Indique su avance: "))

            tarea = Tareas(titulo, cliente, detalles, fecha_inicio, fecha_vencimiento, condicion, avance)
            self.lista_proyectos[id - 1].agregar_tareas(tarea)

        else:
            if len(self.lista_proyectos) != 0:
                with open("datos_prueba_proyecto.json", "r") as archivo_json:
                    datos = json.load(archivo_json)
                    proyecto_data = datos["proyectos"][id - 1]  
                    for tarea_data in proyecto_data["tareas"]:
                        tarea = Tareas(
                            tarea_data["identificador"],
                            tarea_data["titulo"],
                            tarea_data["cliente"],
                            tarea_data["detalles"],
                            datetime.strptime(tarea_data["inicio"], "%Y-%m-%d"),
                            datetime.strptime(tarea_data["vencimiento"], "%Y-%m-%d"),
                            tarea_data["condicion"],
                            tarea_data["avance"]
                        )
                        self.lista_proyectos[id - 1].agregar_tareas(tarea)
            else:
                print("No hay proyectos disponibles")

    def insertar_tareas_posicion(self, id_proyecto):
        if len(self.lista_proyectos) == 0:
            print("No hay proyectos disponibles")
            return

        id_proyecto = int(id_proyecto) - 1  
        if id_proyecto < 0 or id_proyecto >= len(self.lista_proyectos):
            print("El ID del proyecto seleccionado no existe")
            return

        proyecto = self.lista_proyectos[id_proyecto]
        tareas_pila = proyecto.tareas

        if tareas_pila.esta_vacia():
            print("No hay tareas disponibles en el proyecto.")
            return

        print("Tareas disponibles:")
        nodo_actual = tareas_pila.tope
        indice = 0
        while nodo_actual is not None:
            print(f"{indice}: {nodo_actual.valor.nombre}")
            nodo_actual = nodo_actual.siguiente
            indice += 1

        indice_tarea = int(input("Indique el índice de la tarea que desea mover: "))
        if indice_tarea < 0 or indice_tarea >= tareas_pila.get_largo():
            print("El índice de la tarea está fuera de rango.")
            return

        nueva_posicion = int(input("Indique la nueva posición de la tarea: "))
        if nueva_posicion < 0 or nueva_posicion >= tareas_pila.get_largo():
            print("La nueva posición está fuera del rango de las tareas del proyecto.")
            return

        if indice_tarea == nueva_posicion:
            print("La tarea ya está en esa posición.")
            return

        tarea_a_mover = tareas_pila.eliminar_en_posicion(indice_tarea)

        if nueva_posicion < tareas_pila.get_largo():
            tarea_a_intercambiar = tareas_pila.eliminar_en_posicion(nueva_posicion)
            tareas_pila.insertar_en_posicion(tarea_a_intercambiar, indice_tarea)
            print(f"Tarea '{tarea_a_intercambiar.nombre}' movida a la posición {indice_tarea}.")
        else:
            print("No hay tarea en la posición nueva, solo se insertará la tarea en la nueva posición.")

        tareas_pila.insertar_en_posicion(tarea_a_mover, nueva_posicion)
        print(f"Tarea '{tarea_a_mover.nombre}' movida a la posición {nueva_posicion}.")
    
    def eliminar_tareas(self, id_proyecto):
        id_tarea = int(input("Indica el ID de la tarea que desea eliminar: "))
        id_proyecto = id_proyecto - 1

        proyecto_encontrado = self.lista_proyectos[id_proyecto]
        tarea_encontrada = False

        tareas_pila = proyecto_encontrado.tareas
        nodo_actual = tareas_pila.tope
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.valor.id == id_tarea:
                tarea_encontrada = True
                if nodo_anterior is None:
                    tareas_pila.tope = nodo_actual.siguiente
                else:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                break
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        if not tarea_encontrada:
            print("La tarea no existe en el proyecto seleccionado.")
        else:
            print("Tarea eliminada.")



    def listar_tareas(self, id_tarea):
        proyecto = self.lista_proyectos[id_tarea - 1]
        for j in proyecto.tareas:
            if j.id == id_tarea:
                print("Id de la Tarea" + str(j.id))
                print("Titulo de la Tarea" + str(j.nombre))
                print("Cliente de la Tarea" + str(j.cliente))
                print("Detalles de la Tarea" + str(j.descripcion))
                print("Inicio de la Tarea" + str(j.fecha_de_inicio))
                print("Vencimiento de la Tarea" + str(j.fecha_de_vencimiento))
                print("condicion de la Tarea" + str(j.estado_actual))
                print("Avance de la Tarea" + str(j.porcentaje))
                for k in j.subtareas:
                    print("Id de la subTarea" + str(j.identificador))
                    print("Nombre de la Tsubarea" + str(j.titulos))
                    print("Detalles de la subTarea" + str(j.descripcion))
                    print("Condicion de la subTarea" + str(j.condicion))
                    print("")

                bandera = True

        
        if bandera is not True:
            print("No se pueda encontrar la tarea porque el id no existe")
        else:
            print("Tarea encontrada")

    def actualizar_tareas(self):

        if len(self.lista_proyectos) != 0:

            id_tarea = int(input("Indique el id de la tarea que desea actualizar la informacion: "))
            bandera = False # indica si el id de la tarea es valido

            for i in self.lista_proyectos:
                for j in i.tareas:
                    if j.id == id_tarea:

                        # actualizar datos de las tareas
                        #j.id = int(input("Indique el id de la tarea: "))
                        j.nombre = input("Indique el nombre de la tarea: ")
                        j.cliente = input("Indique el cliente de la tarea: ")
                        j.descripcion = input("Indique los detalles de la tarea: ")
                        dia1 = int(input("Introduce el día de inicio de la tarea: "))
                        mes1 = int(input("Introduce el mes de inicio de la tarea: "))
                        anio1 = int(input("Introduce el año de inicio de la tarea: "))
                        j.fecha_de_inicio = datetime(anio1, mes1, dia1)
                        dia2 = int(input("Introduce el día de vencimiento de la tarea: "))
                        mes2 = int(input("Introduce el mes de vencimiento de la tarea: "))
                        anio2 = int(input("Introduce el año de vencimiento de la tarea: "))
                        j.fecha_de_vencimiento = datetime(anio2, mes2, dia2)
                        j.estado_actual = input("Indique el estado actual de la tarea: ")
                        j.porcentaje = int(input("Indique el porcentaje de la tarea: "))
                        
                        bandera = True

            if bandera is not True:
                print("No se puede actualizar la tarea porque el id no existe")
            else:
                print("Tarea Actualizada")

        else:
            print("No hay proyectos disponibles")