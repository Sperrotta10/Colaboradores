import datetime, json
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

            #if self.verificar_proyecto()

            print("\nMenu de Opciones")
            print("1- Agregar nueva tarea")
            print("2- Insertar tarea")
            print("3- Eliminar tarea")
            print("4- Modificar tarea")
            print("5- Listar tareas")
            print("6- Salir del Menu\n")
            opc = input("Escoje la opcion que desea ejecutar: ")

            if int(opc) == 1:
                self.agregar_tareas_al_final(num)
                
            elif int(opc) == 2:
                self.insertar_tareas_posicion(num)

            elif int(opc) == 3:
                self.consultar_proyectos()

            elif int(opc) == 4:
                self.eliminar_proyecto()

            elif int(opc) == 5:
                self.listar_proyectos()

            else:
                break

    def verificar_proyecto(self, lista_proyectos):
        if len(lista_proyectos) == 0:
            return True
        else:
            return False            

    def agregar_tareas_al_final(self, id):
        print(self.lista_proyectos[id].nombre)
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
            self.lista_proyectos[id].agregar_tareas(tarea)

        else:
            if len(self.lista_proyectos) != 0:
                with open("datos_prueba_proyecto.json", "r") as archivo_json:
                    datos = json.load(archivo_json)
                    proyecto_data = datos["proyectos"][id - 1]  # Restamos 1 para ajustarnos al índice de Python (comienza en 0)
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
                        self.lista_proyectos[id].agregar_tareas(tarea)
            else:
                print("No hay proyectos disponibles")




    def insertar_tareas_posicion(self, id_proyecto):

        if len(self.lista_proyectos) != 0:
            posicion = int(input("Indique la posicion donde desea insertar la tarea: "))
            #id_proyecto = int(input("Indique el id del proyecto donde desea ingresar laa tarea"))
            bandera = False # indica si la puede ser ingresada en esa posicion o el proyecto seleccionado existe

            for i in self.lista_proyectos:
                if i.id == id_proyecto:
                    if len(i.tareas)-1 >= posicion and posicion >= 0:

                        # ingresar datos de las tareas
                        id = int(input("Indique el id de la tarea: "))
                        nombre = input("Indique el nombre de la tarea: ")
                        cliente = input("Indique el cliente de la tarea: ")
                        descripcion = input("Indique los detalles de la tarea: ")
                        dia1 = int(input("Introduce el día de inicio de la tarea: "))
                        mes1 = int(input("Introduce el mes de inicio de la tarea: "))
                        anio1 = int(input("Introduce el año de inicio de la tarea: "))
                        fecha_de_inicio = datetime(anio1, mes1, dia1)
                        dia2 = int(input("Introduce el día de vencimiento de la tarea: "))
                        mes2 = int(input("Introduce el mes de vencimiento de la tarea: "))
                        anio2 = int(input("Introduce el año de vencimiento de la tarea: "))
                        fecha_de_vencimiento = datetime(anio2, mes2, dia2)
                        estado_actual = input("Indique el estado actual de la tarea: ")
                        porcentaje = int(input("Indique el porcentaje de la tarea: "))

                        # ingresar datos de las subtareas
                        identificador = int(input("Indique el id de la subtarea: "))
                        titulo = input("Indique el nombre de la subtarea: ")
                        detalles = input("Indique los detalles de la subtarea: ")
                        condicion = input("Indique la condicion de la subtarea: ")

                        subtareas = Subtarea(identificador,titulo,detalles,condicion)

                        tarea = Tareas(id,nombre,cliente,descripcion,fecha_de_inicio,fecha_de_vencimiento,estado_actual,porcentaje)
                        tarea.agregar_subtarea(subtareas)
                        i.agregar_tareas(tarea)
                        bandera = True

            if bandera is not True:
                print("No se puede insertar una tarea en ese proyecto porque el index esta fuera de rango, o el id del proyecto seleccionado no existe")
            else:
                print("Tarea Insertada")
        
        else:
            print("No hay proyectos disponibles")
    
    def eliminar_tareas(self):

        if len(self.lista_proyectos) != 0:

            id_proyecto = int(input("Indica el id del proyecto el cual desea eliminar una tarea: "))
            id_tarea = int(input("Indica el id de la tarea que desea eliminar: "))
            bandera = False # indica si el id del proyecto es valido o el id de la tarea es valido

            for i in self.lista_proyectos:
                if i.id == id_proyecto:
                    for j in i.tareas:
                        if j.id == id_tarea:
                            i.tareas.remove(j)
                            bandera = True

            if bandera is not True:
                print("No se puede eliminar la tarea porque el proyecto no existe o la tarea no existe")
            else:
                print("Tarea Eliminada")

        else:
            print("No hay proyectos disponibles")

    def buscar_Tareas(self):

        if len(self.lista_proyectos) != 0:
            id_tarea = int(input("Indique el id de la tarea que desea buscar: "))
            bandera = False # inidca si el id de la tarea es valido

            for i in self.lista_proyectos:
                for j in i.tareas:
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

        else:
            print("No hay proyectos disponibles")

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