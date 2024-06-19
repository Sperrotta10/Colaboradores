from datetime import datetime
import json, pilas_colas, os
from clases_proyectos_tareas_subtareas import *

# Modulo de Reportes
class Reportes:

    def __init__ (self,lista_proyectos):
        self.lista_proyectos = lista_proyectos
        self.bandera = False
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
            
            if self.verificar_tareas_proyecto(num):
                print("El proyecto no tiene tareas para trabajar!!")
                opc = input("¿Quiere volver al menú principal para agregar proyectos? (S/N)")
                if opc.lower() == "s":  # Corregido: llamada a lower()
                    break
                else:
                    continue
                
            print("Con que tarea va a trabajar?")
            self.listar_tareas_id(num)
            if self.bandera == False:
                break

            print("Listando los ID's de las tareas actuales:")

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

            elif opc == 5:
                break
            else:
                print("Ingrese un dato dentro del rango del menú")

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

    def consultar_tareas(self, id_proyecto):
        contador = 0
        proyecto = self.lista_proyectos[id_proyecto - 1]
        tarea = proyecto.tareas

        print("Indique el estado de la tarea que desea consultar")
        estado = input("C para completado, E para en progreso, P para pendiente")

        print(f"Tareas en estado de {estado}")
        for i in range(tarea.get_largo()):
            
            tarea_actual = tarea.obtener_valor_en_indice(i)
            if tarea_actual.estado_actual == estado:
                contador += 1
                print(f'Tarea: {tarea_actual.nombre}| id: {tarea_actual.id}| estado: {tarea_actual.estado_actual}')
        
        if contador == 0:
            print("No se puede consultar tareas por estado porque no existe ninguna tarea con el estado que seleccion el usuario")

    def filtrado_fecha(self, id_proyecto):
        proyecto = self.lista_proyectos[id_proyecto - 1]
        tareas = proyecto.tareas
        contador = 0

        diccionario = {
            "i": "inicio",
            "v": "vencimiento",

        }

        lista_tareas = []

        fecha = input("Desea filtar fechas por incio o vencimiento? (I/V): ")

        # ingresamos datos de la fecha de inicio
        dia1 = int(input(f"Introduce el día de {diccionario[fecha]} de la tarea: "))
        mes1 = int(input(f"Introduce el mes de {diccionario[fecha]} de la tarea: "))
        anio1 = int(input(f"Introduce el año de {diccionario[fecha]} de la tarea: "))

        fecha = datetime(anio1, mes1, dia1)

        # le pedimos al usuario que indique si quiere buscar antes o despues de la fecha que selecciono
        encontrar = input("Desea encontrar una tarea antes o despues de esa fecha seleccionada? (A/D): ")

        # filtramos tareas antes de la fecha que selecciono el usuario
        if encontrar.lower() == "a":
            for i in range(tareas.get_largo()):
                tarea_actual = tareas.obtener_valor_en_indice(i)
                if fecha == "i":
                    if tarea_actual.fecha_de_inicio < fecha:
                        print(f'Tarea: {tarea_actual.nombre}| ID:{tarea_actual.id}| fecha de inicio: {tarea_actual.fecha_de_inicio}')
                        contador += 1
                else:
                    if tarea_actual.fecha_de_vencimiento < fecha:
                        print(f'Tarea: {tarea_actual.nombre}| ID:{tarea_actual.id}| fecha de inicio: {tarea_actual.fecha_de_inicio}')
                        contador += 1
        else:
            for i in range(tareas.get_largo()):
                tarea_actual = tareas.obtener_valor_en_indice(i)
                if fecha == "i":
                    if tarea_actual.fecha_de_inicio > fecha:
                        print(f'Tarea: {tarea_actual.nombre}| ID:{tarea_actual.id}| fecha de inicio: {tarea_actual.fecha_de_inicio}')
                        contador += 1
                else:
                    if tarea_actual.fecha_de_vencimiento > fecha:
                        print(f'Tarea: {tarea_actual.nombre}| ID:{tarea_actual.id}| fecha de inicio: {tarea_actual.fecha_de_inicio}')
                        contador += 1

        if contador == 0:
            print("No se encontraron tareas con la fecha establecida...")

    def filtrado_proyectos(self):
        contador = 0

        for i in self.lista_proyectos:
            tareas = i.tareas
            largo = tareas.get_largo()

            for j in range(largo):
                tarea_actual = tareas.obtener_valor_en_indice(j)
                
                if tarea_actual.estado == "Completada":
                    contador += 1

            print("id del proyecto: " + str(i.id))
            print("nombre del proyecto: " + str(i.nombre))
            print("descripcion del proyecto: " + str(i.descripcion))
            print("fecha de inicio del proyecto: " + str(i.fecha_de_inicio))
            print("fecha de vencimiento del proyecto: " + str(i.fecha_de_vencimiento))
            print("estado actual del proyecto: " + str(i.estado_actual))
            print("empresa del proyecto: " + str(i.empresa))
            print("gerente del proyecto: " + str(i.gerente))
            print("equipo del proyecto: " + str(i.equipo))
            if self.verificar_tareas_proyecto(i) == False:
                print(f"Porcentaje de completado de las tareas: {contador * 100 / largo}")
            print("")

    def listar_subtareas(self, id_proyecto, id_tarea):
        proyecto = self.lista_proyectos[id_proyecto - 1]
        tareas = proyecto.tareas
        tarea_actual = tareas.obtener_valor_por_id(id_tarea)

        if tarea_actual.subtareas.get_largo() == 0:
            print(f"No hay subtareas en la tarea {id_tarea}")
            return
        
        for i in range(tarea_actual.subtareas.get_largo()):
            subtarea_actual = tarea_actual.subtareas.obtener_valor_en_indice(i)

            print(f'Identificador: {subtarea_actual.identificador}')
            print(f'Titulo: {subtarea_actual.titulo}')
            print(f'Detalles: {subtarea_actual.descripcion}')
            print(f'Condicion: {subtarea_actual.condicion}')
            print("")

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
            self.bandera = True 

    def actualizar_archivo_tareas(lista_proyectos):
        with open("subtareas.txt", "w", encoding="utf-8") as archivo:
            for proyecto in lista_proyectos:
                archivo.write(f"Proyecto ID: {proyecto.id}\n")
                for tarea in proyecto.tareas:
                    archivo.write(f"    Tarea ID: {tarea.tarea_id}\n")
                    archivo.write(f"        Subtareas:\n")
                    for subtarea in tarea.subtareas:
                        archivo.write(f"            ID = {subtarea.subtarea_id}\n")
                        archivo.write(f"            Titulo = {subtarea.titulo}\n")
                        archivo.write(f"            Detalles = {subtarea.detalles}\n")
                        archivo.write(f"            Condicion = {subtarea.condicion}\n")
                    archivo.write("\n")
                archivo.write("\n")

