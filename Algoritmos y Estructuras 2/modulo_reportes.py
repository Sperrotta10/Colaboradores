from datetime import datetime
import json, pilas_colas, os
from clases_proyectos_tareas_subtareas import *

# Modulo de Reportes
class Reportes:

    def __init__ (self,lista_proyectos):
        self.lista_proyectos = lista_proyectos
        self.menu_opciones()

        if self.verificar_proyecto(lista_proyectos):
            print("No hay proyectos para consultar tareas... Cree un proyecto!!")
            print("Dirigiendo al menú principal....")
            print("-" * 40) 
        else:
            self.menu_opciones()

    def menu_opciones(self):
        while True:
            print('-' * 40)
            print("De que proyecto quiere investigar? ")
            num = int(input("Escoja el id del proyecto: "))

            if self.verificar_id_proyecto(num):
                print("El id del proyecto a trabajar no existe!!")
                opc = input("Quiere volver al menú prinicipal para agregar proyectos? (S/N)")
                if opc.lower == "s":
                    break
                else:
                    continue
            
            print("Con que tarea va a trabajar?")
            if self.verificar_id_proyecto(num):
                print("El id del proyecto a trabajar no existe!!")
                opc = input("¿Quiere volver al menú principal para agregar proyectos? (S/N)")
                if opc.lower() == "s":  # Corregido: llamada a lower()
                    break
                else:
                    continue

            print("Listando los ID's de las tareas actuales:")

            self.listar_tareas_id(num)

            print("")
            print('-' * 40)
            print('           Menú de Opciones')
            print('-' * 40)
            print("1- Consulta de Tareas por Estado")
            print("2- Filtrado por Fecha")
            print("3- Filtrado de proyectos")
            print("4- Listar sub tareas")
            print("5- Salir")
            opc = int(input("Escoje la opcion que desea ejecutar: "))

            if opc == 1:
                self.consultar_tareas()

            elif opc == 2:
                self.filtrado_fecha()

            elif opc == 3:
                self.filtrado_proyectos()

            elif opc == 4:
                self.listar_subtareas()

            else:
                break

    def verificar_proyecto(self, lista_proyectos):
        if len(lista_proyectos) == 0:
            return True
        else:
            return False 
        
    def verificar_id_proyecto(self, id_proyecto):
        if id_proyecto > len(self.lista_proyectos):
            return True
        else:
            return False
    
    def verificar_tareas_proyecto(self, id_proyecto):
        if self.lista_proyectos[id_proyecto - 1].tareas.get_largo() == 0:
            return True
        else:
            return False

    def consultar_tareas(self):

        lista_tareas_por_estado = []

        estado = input("Indique el estado de la tarea que desea consultar: ")

        for i in self.lista_proyectos:
            for j in i.tareas:
                if j.estado_actual == estado.capitalize():
                    lista_tareas_por_estado.append(j)


        if len(lista_tareas_por_estado) != 0:

            for j in lista_tareas_por_estado:
                print("Id de la Tarea" + str(j.id))
                print("Titulo de la Tarea" + str(j.nombre))
                print("Cliente de la Tarea" + str(j.cliente))
                print("Detalles de la Tarea" + str(j.descripcion))
                print("Inicio de la Tarea" + str(j.fecha_de_inicio))
                print("Vencimiento de la Tarea" + str(j.fecha_de_vencimiento))
                print("condicion de la Tarea" + str(j.estado_actual))
                print("Avance de la Tarea" + str(j.porcentaje))

        else:
            print("No se puede consultar tareas por estado porque no existe ninguna tarea con el estado que seleccion el usuario")


    def filtrado_fecha(self):

        filtrar_tareas = []
        fecha = input("Desea filtar fechas por incio o vencimiento? (I/V): ")

        # filtramos tareas por fecha de inicio
        if fecha.lower() == "i":

            # ingresamos datos de la fecha de inicio
            dia1 = int(input("Introduce el día de inicio de la tarea: "))
            mes1 = int(input("Introduce el mes de inicio de la tarea: "))
            anio1 = int(input("Introduce el año de inicio de la tarea: "))

            fecha_de_inicio = datetime(anio1, mes1, dia1)

            # le pedimos al usuario que indique si quiere buscar antes o despues de la fecha que selecciono
            encontrar = input("Desea encontrar una tarea antes o despues de esa fecha seleccionada? (A/D): ")

            # filtramos tareas antes de la fecha que selecciono el usuario
            if encontrar.lower() == "a":

                for i in self.lista_proyectos:
                    for j in i.tareas:
                        if j.fecha_de_inicio < fecha_de_inicio:
                            filtrar_tareas.append(j)

            # filtramos tareas despues de la fecha que selecciono el usuario
            elif encontrar.lower() == "d":

                for i in self.lista_proyectos:
                    for j in i.tareas:
                        if j.fecha_de_inicio > fecha_de_inicio:
                            filtrar_tareas.append(j)


        # filtramos tareas por fecha de vencimiento
        elif fecha.lower() == "v":

             # ingresamos datos de la fecha de vencimiento
            dia1 = int(input("Introduce el día de vencimiento de la tarea: "))
            mes1 = int(input("Introduce el mes de vencimiento de la tarea: "))
            anio1 = int(input("Introduce el año de vencimiento de la tarea: "))

            fecha_de_vencimiento = datetime(anio1, mes1, dia1)

            # le pedimos al usuario que indique si quiere buscar antes o despues de la fecha que selecciono
            encontrar = input("Desea encontrar una tarea antes o despues de esa fecha seleccionada? (A/D): ")

            # filtramos tareas antes de la fecha que selecciono el usuario
            if encontrar.lower() == "a":

                for i in self.lista_proyectos:
                    for j in i.tareas:
                        if j.fecha_de_vencimiento < fecha_de_vencimiento:
                            filtrar_tareas.append(j)

            # filtramos tareas despues de la fecha que selecciono el usuario
            elif encontrar.lower() == "d":

                for i in self.lista_proyectos:
                    for j in i.tareas:
                        if j.fecha_de_vencimiento > fecha_de_vencimiento:
                            filtrar_tareas.append(j)


        if len(filtrar_tareas) != 0:

            for i in filtrar_tareas:
                print("Id de la Tarea" + str(j.id))
                print("Titulo de la Tarea" + str(j.nombre))
                print("Cliente de la Tarea" + str(j.cliente))
                print("Detalles de la Tarea" + str(j.descripcion))
                print("Inicio de la Tarea" + str(j.fecha_de_inicio))
                print("Vencimiento de la Tarea" + str(j.fecha_de_vencimiento))
                print("condicion de la Tarea" + str(j.estado_actual))
                print("Avance de la Tarea" + str(j.porcentaje))

        else:
            print("No se puede filtrar ninguna tarea por fecha porque el rango de la fechas seleccionadas por el usuario no existe")

    def listar_tareas_id(self, id_proyecto):
        proyecto = self.lista_proyectos[id_proyecto - 1]
        tareas = proyecto.tareas
        if (tareas.get_largo()) == 0:
            print("No hay tareas para trabajar...")
            return
        
        print("ID's de las tareas existentes: ")
        for j in range(tareas.get_largo()):
            tarea_actual = tareas.obtener_valor_en_indice(j)
            
            print("")
            print(f'ID de la tarea "{tarea_actual.nombre}": {tarea_actual.id}')
