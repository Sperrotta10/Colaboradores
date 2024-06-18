
from datetime import datetime
import json, pilas

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

    def insertar_tareas(self,tareas,posicion):
        self.tareas.insert(posicion,tareas)


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


# modulo de importacion y exportacion de datos
class Archivo:

    def __init__ (self):
        self.jason = ""
        self.respaldo = ""

    def leer_ruta_archivos(self):

        with open("Algoritmos y Estructuras 2\\config.txt", "r") as archivo:
            # Leemos todo el contenido del archivo y lo guardamos en una lista
            lineas = []
            for linea in archivo:
                lineas.append(linea.strip())

        self.jason = lineas[0]
        self.respaldo = lineas[1]
    
    def cargar_datos_desde_json(self):
        proyectos = []

        self.leer_ruta_archivos()

        with open(self.jason + ".json", "r") as archivo:
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
                    proyecto.agregar_tareas(tarea)
                proyectos.append(proyecto)

        # escribimos el respaldo de los datos que se leyeron el .json y lo guardamos en respaldo
        self.escribir_datos(proyectos)
        return proyectos
    

    def escribir_datos(self,lista_proyectos):

        with open(self.respaldo + ".txt", 'w') as archivo:

            for i in lista_proyectos:

                archivo.write("Id Proyecto: " + str(i.id) + " ")
                archivo.write("Nombre Proyecto: " + i.nombre + " ")
                archivo.write("Descripcion Proyecto: " + i.descripcion + " ")
                archivo.write("Inicio Proyecto: " + str(i.fecha_de_inicio) + " ")
                archivo.write("Vencimiento Proyecto: " + str(i.fecha_de_vencimiento) + " ")
                archivo.write("Estado Proyecto: " + i.estado_actual + " ")
                archivo.write("Empresa Proyecto: " + i.empresa + " ")
                archivo.write("Gerente Proyecto: " + i.gerente + " ")
                archivo.write("Equipo Proyecto: " + str(i.equipo))
                archivo.write("\n")

                for j in i.tareas:
                    archivo.write("Id Tarea: " + str(j.id) + " ")
                    archivo.write("Nombre Tarea: " + j.nombre + " ")
                    archivo.write("Cliente Tarea: " + j.cliente + " ")
                    archivo.write("Descripcion Tarea: " + j.descripcion + " ")
                    archivo.write("Inicio Tarea: " + str(j.fecha_de_inicio) + " ")
                    archivo.write("Vencimiento Tarea: " + str(j.fecha_de_vencimiento) + " ")
                    archivo.write("Estado Tarea: " + j.estado_actual + " ")
                    archivo.write("Porcentaje Tarea: " + str(j.porcentaje))
                    archivo.write("\n")

                    for k in j.subtareas:
                        archivo.write("Id subTarea: " + str(k.identificador) + " ")
                        archivo.write("Nombre subTarea: " + k.titulo + " ")
                        archivo.write("Descripcion subTarea: " + k.descripcion + " ")
                        archivo.write("Condicion subTarea: " + str(k.condicion))
                        archivo.write("\n")



# Primero Modulo del proyecto
class Gestion_proyectos:

    def __init__ (self,archivo,proyectos):
        self.lista_proyectos = proyectos
        self.archivo = archivo
        self.menu_opciones()
    
    
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
                self.archivo.escribir_datos(self.lista_proyectos)  # respaldamos los datos nuevos y anteriores en el txt
                
            elif opc == 2:
                self.modificar_proyecto()

            elif opc == 3:
                self.consultar_proyectos()

            elif opc == 4:
                self.eliminar_proyecto()

            elif opc == 5:
                self.listar_proyectos()

            else:
                break


    def crear_proyecto(self):
        
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

            for j in range(cantidad):
                integrante = input("Escribe el " + str(j+1) + " integrante del equipo: ")
                equipo.append(integrante)

            # creamos un objeto de tipo proyecto
            proyecto = Proyectos(id,nombre,descripcion,fecha_de_inicio,fecha_de_vencimiento,estado_actual,empresa,gerente,equipo)
            # agregar proyecto a la lista de proyectos
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

                    for j in range(cantidad):
                        integrante = input("Escribe el " + str(j+1) + " integrante del equipo: ")
                        equipo.append(integrante)

                    i.equipo = equipo
                    bandera = True

            # condicion para indicar que no existe ese proyecto que seleccione el usuario
            if bandera is not True:
                print("Ese proyecto no existe por lo tanto no se puede modificar")
            else:
                print("\nProyecto Modificado")
                self.archivo.escribir_datos(self.lista_proyectos) # respaldamos los datos nuevos y anteriores en el txt
        
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
                self.archivo.escribir_datos(self.lista_proyectos) # respaldamos los datos nuevos y anteriores en el txt
        
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
    def __init__ (self,lista_proyectos,archivo):
        self.lista_proyectos = lista_proyectos
        self.archivo = archivo
        self.menu_opciones()


    def menu_opciones(self):
        while True:

            print("\nMenu de Opciones")
            print("1- Agregar nueva tarea")
            print("2- Insertar tarea")
            print("3- Eliminar tarea")
            print("4- Buscar tarea")
            print("5- Actualizar tareas")
            print("6- Salir del Menu\n")
            opc = int(input("Escoje la opcion que desea ejecutar: "))

            if opc == 1:
                self.agregar_tareas_al_final()
                
            elif opc == 2:
                self.insertar_tareas_posicion()

            elif opc == 3:
                self.eliminar_tareas()

            elif opc == 4:
                self.buscar_Tareas()

            elif opc == 5:
                self.actualizar_tareas()

            else:
                break


    def agregar_tareas_al_final(self):
        
        if len(self.lista_proyectos) != 0:

            pila_tareas = pilas.Pila()
            id_proyecto = int(input("Indique el id del proyecto donde desea ingresar laa tarea: "))
            bandera = False # indica si la puede ser ingresada en esa posicion o el proyecto seleccionado existe

            for i in self.lista_proyectos:
                if i.id == id_proyecto:

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
                print("No se puede agregar una tarea en ese proyecto porque el index esta fuera de rango, o el id del proyecto seleccionado no existe")
            else:
                print("Tarea Agregada")
                self.archivo.escribir_datos(self.lista_proyectos) # respaldamos los datos nuevos y anteriores en el txt

        else:
            print("No hay proyectos disponibles")

        self.menu_opciones()


    def insertar_tareas_posicion(self):

        if len(self.lista_proyectos) != 0:
            posicion = int(input("Indique la posicion donde desea insertar la tarea: "))
            id_proyecto = int(input("Indique el id del proyecto donde desea ingresar laa tarea: "))
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
                        i.insertar_tareas(posicion,tarea)
                        bandera = True

            if bandera is not True:
                print("No se puede insertar una tarea en ese proyecto porque el index esta fuera de rango, o el id del proyecto seleccionado no existe")
            else:
                print("Tarea Insertada")
                self.archivo.escribir_datos(self.lista_proyectos) # respaldamos los datos nuevos y anteriores en el txt

        
        else:
            print("No hay proyectos disponibles")

        self.menu_opciones()
    

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
                self.archivo.escribir_datos(self.lista_proyectos) # respaldamos los datos nuevos y anteriores en el txt


        else:
            print("No hay proyectos disponibles")


        self.menu_opciones()


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
                            print("Id de la subTarea" + str(k.identificador))
                            print("Nombre de la Tsubarea" + str(k.titulos))
                            print("Detalles de la subTarea" + str(k.descripcion))
                            print("Condicion de la subTarea" + str(k.condicion))
                            print("")

                        bandera = True

            
            if bandera is not True:
                print("No se pueda encontrar la tarea porque el id no existe")
            else:
                print("Tarea encontrada")

        else:
            print("No hay proyectos disponibles")

        self.menu_opciones()


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
                self.archivo.escribir_datos(self.lista_proyectos) # respaldamos los datos nuevos y anteriores en el txt


        else:
            print("No hay proyectos disponibles")


        self.menu_opciones()



# Modulo de Reportes
class Reportes:
    
    def __init__ (self,lista_proyectos):
        self.lista_proyectos = lista_proyectos

    def menu_opciones(self):
        while True:

            print("\nMenu de Opciones")
            print("1- Agregar nueva tarea")
            print("2- Insertar tarea")
            print("3- Eliminar tarea")
            print("4- Buscar tarea")
            print("5- Actualizar tareas")
            print("6- Salir del Menu\n")
            opc = int(input("Escoje la opcion que desea ejecutar: "))

            if opc == 1:
                self.agregar_tareas_al_final()
                
            elif opc == 2:
                self.insertar_tareas_posicion()

            elif opc == 3:
                self.eliminar_tareas()

            elif opc == 4:
                self.buscar_Tareas()

            elif opc == 5:
                self.actualizar_tareas()

            else:
                break


archivo = Archivo()
lista_de_los_proyectos = archivo.cargar_datos_desde_json()
modulo1 = Gestion_proyectos(archivo,lista_de_los_proyectos)
lista_de_los_proyectos = modulo1.lista_proyectos

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