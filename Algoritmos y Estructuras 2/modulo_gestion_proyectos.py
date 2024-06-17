
from datetime import datetime
import json

# Clase de los proyectos
class Proyectos:
    def __init__ (self, id, nombre, descripcion, fecha_de_inicio,fecha_de_vencimiento, estado_actual, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre 
        self.descripcion = descripcion
        self.fecha_de_inicio = fecha_de_inicio
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.estado_actual = estado_actual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas = []

    def agregar_tareas(self,tareas):
        self.tareas.append(tareas)


# Clase de las tareas de los proyectos
class Tareas:
    def __init__ (self,id, nombre,cliente,descripcion, fecha_de_inicio, fecha_de_vencimiento,estado_actual,porcentaje):
        self.id = id
        self.nombre = nombre
        self.cliente = cliente
        self.descripcion = descripcion
        self.fecha_de_inicio = fecha_de_inicio
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.subtareas = [] 

    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)

# Clase de las subtareas de las tareas del proyecto
class Subtarea:
    def __init__(self,identificador,titulo,descripcion,condicion) -> None:
        self.identificador =identificador
        self.titulo =titulo
        self.descripcion=descripcion
        self.condicion=condicion


# Primero Modulo del proyecto
class Gestion_proyectos:

    def __init__ (self):
        self.lista_proyectos = []
    
    def menu_opciones(self):

        while True:

            print("\nMenu de Opciones")
            print("1- Crear Proyectos")
            print("2- Modificar Proyectos")
            print("3- Consultar Proyectos")
            print("4- Eliminar Proyectos")
            print("5- Listar Proyectos")
            print("6- Salir del Menu\n")
            opc = int(input("Escoje la opcion que desea ejecutar: "))

            if opc == 1:
                self.crear_proyecto()
                
            elif opc == 2:
                self.modificar_proyecto()

            elif opc == 3:
                self.consultar_proyectos()

            elif opc == 4:
                self.eliminar_proyecto()

            elif opc == 5:
                self.listar_proyectos()

            elif opc == 6:
                break

    def crear_proyecto(self):
        pregunta = input("Desea ingresar los datos manualmente o de forma automatica? (M/A)")

        if pregunta.lower() == "m":


            cant_proyectos = int(input("Cuantos proyectos deseas crear: "))

            for i in range(cant_proyectos):
            
                # pedimos el ingreso de datos de forma manual
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
                cantidad = int(input("numero de integrantes del equipo: "))
                equipo = []

                for i in range(cantidad):
                    integrante = input("Escribe el " + str(i+1) + " integrante del equipo: ")
                    equipo.append(integrante)

                # creamos un objeto de tipo proyecto
                proyecto = Proyectos(id,nombre,descripcion,fecha_de_inicio,fecha_de_vencimiento,estado_actual,empresa,gerente,equipo)
                # agregar proyecto a la lista de proyectos
                self.lista_proyectos.append(proyecto)

            print("\nProyectos Creados")

        else:
            
            # ingresar los datos de forma automatica de un archivo .json
            with open("datos_prueba1.json", "r") as archivo:
                datos = json.load(archivo)
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

            print("\nProyectos Creados")
        
        self.menu_opciones()

    def modificar_proyecto(self):
        if len(self.lista_proyectos) == 0:
            print("No hay proyectos disponibles para modificar")
        else:
            pedir_id = int(input("Ingresar el id del proyecto que desea modificar: "))
            bandera = False # esta bandera es para verificar si el id de ese proyecto existe

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
                    cantidad = int(input("numero de integrantes del equipo: "))
                    equipo = []

                    for i in range(cantidad):
                        integrante = input("Escribe el " + str(i+1) + " integrante del equipo: ")
                        equipo.append(integrante)

                    i.equipo = equipo
                    bandera = True

            # condicion para indicar que no existe ese proyecto que seleccione el usuario
            if bandera is not True:
                print("Ese proyecto no existe por lo tanto no se puede modificar")
            else:
                print("\nProyecto Modificado")
        
        self.menu_opciones()
    
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

        self.menu_opciones()

    def eliminar_proyecto(self):
        if len(self.lista_proyectos) == 0:
            print("No hay proyectos para eliminar")
        else:

            pedir_id = int(input("Ingresar el id del proyecto que desea eliminar: "))
            bandera = False # esta bandera es para verificar si el id de ese proyecto existe

            for i in self.lista_proyectos:
                if i.id == pedir_id:
                    self.lista_proyectos.remove(i)
                    bandera = True

            if bandera is not True:
                print("Ese proyecto no existe por lo tanto no se puede eliminar")
            else:
                print("Proyecto Eliminado")
        
        self.menu_opciones()

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
        
        self.menu_opciones()

# segundo modulo
class Gestion_Tareas_prioridades:
    def __init__ (self,lista_proyectos):
        self.lista_proyectos = lista_proyectos

    def agregar_tareas_al_final(self):

        if len(self.lista_proyectos) != 0:
            i = 0
            with open("datos_prueba_proyecto.json", "r") as archivo:
                datos = json.load(archivo)
                for proyecto_data in datos["proyectos"]:
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
                        for subtarea_data in tarea_data.get("subtareas", []):
                            subtarea = Subtarea(
                                subtarea_data["identificador"],
                                subtarea_data["titulo"],
                                subtarea_data["detalles"],
                                subtarea_data["condicion"]
                            )
                            tarea.agregar_subtarea(subtarea)
                        self.lista_proyectos[i].agregar_tareas(tarea)
                    i += 1
        else:
            print("No hay proyectos disponibles")

    def insertar_tareas_posicion(self):

        if len(self.lista_proyectos) != 0:
            posicion = int(input("Indique la posicion donde desea insertar la tarea: "))
            id_proyecto = int(input("Indique el id del proyecto donde desea ingresar laa tarea"))
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
                        j.id = int(input("Indique el id de la tarea: "))
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