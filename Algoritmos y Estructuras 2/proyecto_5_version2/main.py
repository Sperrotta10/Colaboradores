import datetime as datetime
from modulos.empresa import GestionEmpresas, Empresa
from modulos.proyecto import GestionProyectos, Proyecto
from modulos.tareas import GestionTareas, Tarea
from modulos.sprint import GestionSprints, Sprint
from modulos.reporte import Reporte
import os

def cargar_configuracion(config_file):
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"El archivo {config_file} no existe.")
    if os.path.getsize(config_file) == 0:
        raise ValueError(f"El archivo {config_file} está vacío.")
    config = {}
    base_dir = os.path.dirname(config_file)
    
    with open(config_file, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=')
                config[key.strip()] = os.path.join(base_dir, value.strip())
    
    return config

def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Gestionar Empresas")
        print("2. Gestionar Proyectos")
        print("3. Gestionar Tareas")
        print("4. Gestionar Sprints")
        print("5. Generar Reporte")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        print("\n")
        
        if opcion == '1':
            menu_gestion_empresas()
        elif opcion == '2':
            menu_gestion_proyectos()
        elif opcion == '3':
            menu_gestion_tareas()
        elif opcion == '4':
            menu_gestion_sprints()
        elif opcion == '5':
            menu_generar_reporte()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")



def menu_gestion_empresas():
    while True:
        print("\nMenu de Gestión de Empresas")
        print("1. Listar Empresas")
        print("2. Agregar Empresa")
        print("3. Modificar Empresa")
        print("4. Eliminar Empresa")
        print("5. Consultar una Empresa")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        print("\n")

        if opcion == '1':
            gestion_empresas.listar_empresas()
        elif opcion == '2':

            try:
                id = int(input("Ingresa el id de la empresa: "))
                nombre = input("Ingresar el nombre de la empresa: ")
                descripcion = input("Descripcion de la empresa: ")
                dia_c = int(input("Ingresa el dia de creacion de la empresa: "))
                mes_c = int(input("Ingresa el mes de creacion de la empresa: "))
                year_c = int(input("Ingresa el mes de creacion de la empresa: "))
                fecha_creacion = datetime.date(year_c, mes_c, dia_c)
                direccion = input("Ingrese la direccion de la empresa: ")
                telefono = input("Ingrese el numero de telefono de la empresa: ")
                correo = input("Ingrese el correo de la empresa: ")
                gerente = input("Ingrese el gerente de la empresa: ")
                numero_integrantes = int(input("Ingrese el numero de integrantes del equipo: "))
                equipo = []

                for i in range(numero_integrantes):
                    integrante = input(f"Ingrese el nombre del integrante {i+1} del equipo: ")
                    equipo.append(integrante)

                fecha_creacion_str = fecha_creacion.isoformat()
                empresa = Empresa(id,nombre,descripcion,fecha_creacion_str,direccion,telefono,correo,gerente,equipo)

                gestion_empresas.agregar_empresa(empresa)

            except Exception as e :
                print(f"Ocurrio un error al agregar una empresa: {e}")

            
        elif opcion == '3':

            try:

                id = int(input("Ingresa el id de la empresa que deseas modificar: "))
                nombre = input("Ingresar el nombre de la empresa: ")
                descripcion = input("Descripcion de la empresa: ")
                dia_c = int(input("Ingresa el dia de creacion de la empresa: "))
                mes_c = int(input("Ingresa el mes de creacion de la empresa: "))
                year_c = int(input("Ingresa el mes de creacion de la empresa: "))
                fecha_creacion = datetime.date(year_c, mes_c, dia_c)
                direccion = input("Ingrese la direccion de la empresa: ")
                telefono = input("Ingrese el numero de telefono de la empresa: ")
                correo = input("Ingrese el correo de la empresa: ")
                gerente = input("Ingrese el gerente de la empresa: ")
                numero_integrantes = int(input("Ingrese el numero de integrantes del equipo: "))
                equipo = []

                for i in range(numero_integrantes):
                    integrante = input(f"Ingrese el nombre del integrante {i+1} del equipo: ")
                    equipo.append(integrante)

                fecha_creacion_str = fecha_creacion.isoformat()

                gestion_empresas.modificar_empresa(id,nombre = nombre, descripcion = descripcion, fecha_creacion = fecha_creacion_str, direccion = direccion, telefono = telefono, correo = correo, gerente = gerente, equipo = equipo)

            except Exception as e :
                print(f"Ocurrio un error al modificar una empresa: {e}")

        elif opcion == '4':
           
            try:
               id = int(input("Ingresa el id de la empresa que deseas eliminar: "))
               gestion_empresas.eliminar_empresa(id)
            except Exception as e:
                print(f"Ocurrio un error al eliminar una empresa: {e}")

        elif opcion == '5':
            try:
                empresa_id = int(input("Ingresa el id de la empresa que deseas consultar: "))
                gestion_empresas.consultar_empresa(empresa_id)
            except Exception as e:
                print(f"Ocurrio un error al consultar una empresa: {e}")


        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")



def menu_gestion_proyectos():
    while True:
        print("\nMenu de Gestión de Proyectos")
        print("1. Listar Proyectos")
        print("2. Agregar Proyecto")
        print("3. Modificar Proyecto")
        print("4. Eliminar Proyecto")
        print("5. Buscar Proyecto por Criterios")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        print("\n")

        if opcion == '1':
            gestion_proyectos.listar_proyectos()
        elif opcion == '2':
            try:
                id = int(input("Ingresa el id del proyecto: "))
                nombre = input("Ingresar el nombre del proyecto: ")
                descripcion = input("Descripcion del proyecto: ")
                dia_c = int(input("Ingresa el dia de creacion del proyecto: "))
                mes_c = int(input("Ingresa el mes de creacion del proyecto: "))
                year_c = int(input("Ingresa el mes de creacion del proyecto: "))
                fecha_inicio = datetime.date(year_c, mes_c, dia_c)
                dia_v = int(input("Ingresa el dia de vencimiento del proyecto: "))
                mes_v = int(input("Ingresa el mes de vencimiento del proyecto: "))
                year_v = int(input("Ingresa el mes de vencimiento del proyecto: "))
                fecha_vencimiento = datetime.date(year_v, mes_v, dia_v)
                estado_actual = input("Ingrese el estado actual del proyecto: ")
                empresa = input("Ingrese el id de la empresa: ")
                gerente = input("Ingrese el gerente del proyecto: ")
                numero_integrantes = int(input("Ingrese el numero de integrantes del equipo: "))
                equipo = []

                for i in range(numero_integrantes):
                    integrante = input(f"Ingrese el nombre del integrante {i+1} del equipo: ")
                    equipo.append(integrante)

                fecha_inicio_str = fecha_inicio.isoformat()
                fecha_vencimiento_str = fecha_vencimiento.isoformat()
                proyecto = Proyecto(id,nombre,descripcion,fecha_inicio_str,fecha_vencimiento_str,estado_actual,empresa,gerente,equipo)

                gestion_proyectos.agregar_proyecto(proyecto)

            except Exception as e :
                print(f"Ocurrio un error al agregar un proyecto: {e}")

        elif opcion == '3':
            try:
                id = int(input("Ingresa el id del proyecto: "))
                nombre = input("Ingresar el nombre del proyecto: ")
                descripcion = input("Descripcion del proyecto: ")
                dia_c = int(input("Ingresa el dia de creacion del proyecto: "))
                mes_c = int(input("Ingresa el mes de creacion del proyecto: "))
                year_c = int(input("Ingresa el mes de creacion del proyecto: "))
                fecha_inicio = datetime.date(year_c, mes_c, dia_c)
                dia_v = int(input("Ingresa el dia de vencimiento del proyecto: "))
                mes_v = int(input("Ingresa el mes de vencimiento del proyecto: "))
                year_v = int(input("Ingresa el mes de vencimiento del proyecto: "))
                fecha_vencimiento = datetime.date(year_v, mes_v, dia_v)
                estado_actual = input("Ingrese el estado actual del proyecto: ")
                empresa_id = input("Ingrese el id de la empresa: ")
                gerente = input("Ingrese el gerente del proyecto: ")
                numero_integrantes = int(input("Ingrese el numero de integrantes del equipo: "))
                equipo = []

                for i in range(numero_integrantes):
                    integrante = input(f"Ingrese el nombre del integrante {i+1} del equipo: ")
                    equipo.append(integrante)

                fecha_inicio_str = fecha_inicio.isoformat()
                fecha_vencimiento_str = fecha_vencimiento.isoformat()

                gestion_proyectos.modificar_proyecto(id,nombre = nombre, descripcion = descripcion, fecha_inicio = fecha_inicio_str,fecha_vencimiento = fecha_vencimiento_str, estado_actual = estado_actual, empresa = empresa_id, gerente = gerente, equipo = equipo)

            except Exception as e :
                print(f"Ocurrio un error al modificar un proyecto: {e}")

        elif opcion == '4':
            print("1- eliminar por id")
            print("2- eliminar por nombre")
            print("3- eliminar por id empresa")
            print("4- eliminar por gerente")
            print("5- eliminar por fecha de inicio")
            print("6- eliminar por fecha de vencimiento")
            print("7- eliminar por estado actual")
            opc = int(input("Ingrese la opcion que desea para eliminar: "))

            if (opc == 1):
                try:
                    id = int(input("Ingresa el id del proyecto: "))
                    print(gestion_proyectos.eliminar(id = id))
                except Exception as e:
                    print(f"Ocurrio un error al eliminar un proyecto: {e}")

            elif (opc == 2):
                try:
                    nombre = input("Ingresar el nombre del proyecto: ")
                    print(gestion_proyectos.eliminar(nombre = nombre))
                except Exception as e:
                    print(f"Ocurrio un error al eliminar un proyecto: {e}")
            elif (opc == 3):
                try:
                    empresa_id = input("Ingrese el id de la empresa: ")
                    print(gestion_proyectos.eliminar(empresa = empresa_id))
                except Exception as e:
                    print(f"Ocurrio un error al eliminar un proyecto: {e}")
            elif (opc == 4):
                try:
                    gerente = input("Ingrese el gerente del proyecto: ")
                    print(gestion_proyectos.eliminar(gerente = gerente))
                except Exception as e:
                    print(f"Ocurrio un error al eliminar un proyecto: {e}")
            elif (opc == 5):
                try:
                    dia_c = int(input("Ingresa el dia de creacion del proyecto: "))
                    mes_c = int(input("Ingresa el mes de creacion del proyecto: "))
                    year_c = int(input("Ingresa el mes de creacion del proyecto: "))
                    fecha_inicio = datetime.date(year_c, mes_c, dia_c)

                    fecha_inicio_str = fecha_inicio.isoformat()
                    print(gestion_proyectos.eliminar(fecha_inicio = fecha_inicio_str))
                except Exception as e:
                    print(f"Ocurrio un error al eliminar un proyecto: {e}")
            elif (opc == 6):
                try:
                    dia_v = int(input("Ingresa el dia de vencimiento del proyecto: "))
                    mes_v = int(input("Ingresa el mes de vencimiento del proyecto: "))
                    year_v = int(input("Ingresa el mes de vencimiento del proyecto: "))
                    fecha_vencimiento = datetime.date(year_v, mes_v, dia_v)

                    fecha_vencimiento_str = fecha_vencimiento.isoformat()
                    print(gestion_proyectos.eliminar(fecha_vencimiento = fecha_vencimiento_str))
                except Exception as e:
                    print(f"Ocurrio un error al eliminar un proyecto: {e}")
            elif (opc == 7):
                try:
                    estado_actual = input("Ingrese el estado actual del proyecto: ")

                    print(gestion_proyectos.eliminar(estado_actual = estado_actual))
                except Exception as e:
                    print(f"Ocurrio un error al eliminar un proyecto: {e}")
                    
        elif opcion == '5':
            
            print("1- consultar por id")
            print("2- consultar por nombre")
            print("3- consultar por id empresa")
            print("4- consultar por gerente")
            print("5- consultar por fecha de inicio")
            print("6- consultar por fecha de vencimiento")
            print("7- consultar por estado actual")
            opc = int(input("Ingrese la opcion que desea para consultar: "))

            if (opc == 1):
                try:
                    id = int(input("Ingresa el id del proyecto: "))
                    consulta = gestion_proyectos.consultar(id = id)
                    if consulta:
                        print(f"ID: {consulta.id}")
                        print(f"Nombre: {consulta.nombre}")
                        print(f"Descripción: {consulta.descripcion}")
                        print(f"Fecha de inicio: {consulta.fecha_inicio.strftime('%Y-%m-%d')}")
                        print(f"Fecha de vencimiento: {consulta.fecha_vencimiento.strftime('%Y-%m-%d')}")
                        print(f"Estado actual: {consulta.estado_actual}")
                        print(f"Empresa: {consulta.empresa}")
                        print(f"Gerente: {consulta.gerente}")
                        print(f"Equipo: {', '.join(consulta.equipo)}")

                    else:
                        print("Vacio")
                except Exception as e:
                    print(f"Ocurrio un error al consultar un proyecto: {e}")

            elif (opc == 2):
                try:
                    nombre = input("Ingresar el nombre del proyecto: ")
                    consulta = gestion_proyectos.consultar(nombre = nombre)
                    if consulta:
                        print(f"ID: {consulta.id}")
                        print(f"Nombre: {consulta.nombre}")
                        print(f"Descripción: {consulta.descripcion}")
                        print(f"Fecha de inicio: {consulta.fecha_inicio.strftime('%Y-%m-%d')}")
                        print(f"Fecha de vencimiento: {consulta.fecha_vencimiento.strftime('%Y-%m-%d')}")
                        print(f"Estado actual: {consulta.estado_actual}")
                        print(f"Empresa: {consulta.empresa}")
                        print(f"Gerente: {consulta.gerente}")
                        print(f"Equipo: {', '.join(consulta.equipo)}")

                    else:
                        print("Vacio")
                except Exception as e:
                    print(f"Ocurrio un error al consultar un proyecto: {e}")
            elif (opc == 3):
                try:
                    empresa_id = input("Ingrese el id de la empresa: ")
                    consulta = gestion_proyectos.consultar(empresa = empresa_id)
                    if consulta:
                        print(f"ID: {consulta.id}")
                        print(f"Nombre: {consulta.nombre}")
                        print(f"Descripción: {consulta.descripcion}")
                        print(f"Fecha de inicio: {consulta.fecha_inicio.strftime('%Y-%m-%d')}")
                        print(f"Fecha de vencimiento: {consulta.fecha_vencimiento.strftime('%Y-%m-%d')}")
                        print(f"Estado actual: {consulta.estado_actual}")
                        print(f"Empresa: {consulta.empresa}")
                        print(f"Gerente: {consulta.gerente}")
                        print(f"Equipo: {', '.join(consulta.equipo)}")

                    else:
                        print("Vacio")
                except Exception as e:
                    print(f"Ocurrio un error al consultar un proyecto: {e}")
            elif (opc == 4):
                try:
                    gerente = input("Ingrese el gerente del proyecto: ")
                    consulta = gestion_proyectos.consultar(gerente = gerente)
                    if consulta:
                        print(f"ID: {consulta.id}")
                        print(f"Nombre: {consulta.nombre}")
                        print(f"Descripción: {consulta.descripcion}")
                        print(f"Fecha de inicio: {consulta.fecha_inicio.strftime('%Y-%m-%d')}")
                        print(f"Fecha de vencimiento: {consulta.fecha_vencimiento.strftime('%Y-%m-%d')}")
                        print(f"Estado actual: {consulta.estado_actual}")
                        print(f"Empresa: {consulta.empresa}")
                        print(f"Gerente: {consulta.gerente}")
                        print(f"Equipo: {', '.join(consulta.equipo)}")

                    else:
                        print("Vacio")
                except Exception as e:
                    print(f"Ocurrio un error al consultar un proyecto: {e}")
            elif (opc == 5):
                try:
                    dia_c = int(input("Ingresa el dia de creacion del proyecto: "))
                    mes_c = int(input("Ingresa el mes de creacion del proyecto: "))
                    year_c = int(input("Ingresa el mes de creacion del proyecto: "))
                    fecha_inicio = datetime.date(year_c, mes_c, dia_c)

                    fecha_inicio_str = fecha_inicio.isoformat()
                    consulta = gestion_proyectos.consultar(fecha_inicio = fecha_inicio_str)
                    if consulta:
                        print(f"ID: {consulta.id}")
                        print(f"Nombre: {consulta.nombre}")
                        print(f"Descripción: {consulta.descripcion}")
                        print(f"Fecha de inicio: {consulta.fecha_inicio.strftime('%Y-%m-%d')}")
                        print(f"Fecha de vencimiento: {consulta.fecha_vencimiento.strftime('%Y-%m-%d')}")
                        print(f"Estado actual: {consulta.estado_actual}")
                        print(f"Empresa: {consulta.empresa}")
                        print(f"Gerente: {consulta.gerente}")
                        print(f"Equipo: {', '.join(consulta.equipo)}")

                    else:
                        print("Vacio")
                except Exception as e:
                    print(f"Ocurrio un error al consultar un proyecto: {e}")
            elif (opc == 6):
                try:
                    dia_v = int(input("Ingresa el dia de vencimiento del proyecto: "))
                    mes_v = int(input("Ingresa el mes de vencimiento del proyecto: "))
                    year_v = int(input("Ingresa el mes de vencimiento del proyecto: "))
                    fecha_vencimiento = datetime.date(year_v, mes_v, dia_v)

                    fecha_vencimiento_str = fecha_vencimiento.isoformat()
                    consulta = gestion_proyectos.consultar(fecha_vencimiento = fecha_vencimiento_str)
                    if consulta:
                        print(f"ID: {consulta.id}")
                        print(f"Nombre: {consulta.nombre}")
                        print(f"Descripción: {consulta.descripcion}")
                        print(f"Fecha de inicio: {consulta.fecha_inicio.strftime('%Y-%m-%d')}")
                        print(f"Fecha de vencimiento: {consulta.fecha_vencimiento.strftime('%Y-%m-%d')}")
                        print(f"Estado actual: {consulta.estado_actual}")
                        print(f"Empresa: {consulta.empresa}")
                        print(f"Gerente: {consulta.gerente}")
                        print(f"Equipo: {', '.join(consulta.equipo)}")

                    else:
                        print("Vacio")
                except Exception as e:
                    print(f"Ocurrio un error al consultar un proyecto: {e}")
            elif (opc == 7):
                try:
                    estado_actual = input("Ingrese el estado actual del proyecto: ")

                    consulta = gestion_proyectos.consultar(estado_actual = estado_actual)

                    if consulta:
                        print(f"ID: {consulta.id}")
                        print(f"Nombre: {consulta.nombre}")
                        print(f"Descripción: {consulta.descripcion}")
                        print(f"Fecha de inicio: {consulta.fecha_inicio.strftime('%Y-%m-%d')}")
                        print(f"Fecha de vencimiento: {consulta.fecha_vencimiento.strftime('%Y-%m-%d')}")
                        print(f"Estado actual: {consulta.estado_actual}")
                        print(f"Empresa: {consulta.empresa}")
                        print(f"Gerente: {consulta.gerente}")
                        print(f"Equipo: {', '.join(consulta.equipo)}")

                    else:
                        print("Vacio")
                except Exception as e:
                    print(f"Ocurrio un error al consultar un proyecto: {e}")


        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")



def menu_gestion_tareas():
    while True:
        print("\nMenu de Gestión de Tareas")
        print("1. Listar Tareas")
        print("2. Agregar Tarea")
        print("3. Modificar Tarea")
        print("4. Eliminar Tarea")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        print("\n")

        if opcion == '1':
            gestion_tareas.listar_tareas_del_proyecto()
        elif opcion == '2':
            try:
                id_proyecto = int(input("Ingresa el id del proyecto: "))
                id_tarea_padre = int(input("Ingresa el id de la tarea padre: ")) or None
                id = int(input("Ingresa el id de la tarea: "))
                nombre = input("Ingresar el nombre de la tarea: ")
                empresa_cliente = input("Ingresar el nombre de la empresa del cliente de la tarea: ")
                descripcion = input("Descripcion de la tarea: ")
                dia_c = int(input("Ingresa el dia de creacion de la tarea: "))
                mes_c = int(input("Ingresa el mes de creacion de la tarea: "))
                year_c = int(input("Ingresa el mes de creacion de la tarea: "))
                fecha_inicio = datetime.date(year_c, mes_c, dia_c)
                dia_v = int(input("Ingresa el dia de vencimiento de la tarea: "))
                mes_v = int(input("Ingresa el mes de vencimiento de la tarea: "))
                year_v = int(input("Ingresa el mes de vencimiento de la tarea: "))
                fecha_vencimiento = datetime.date(year_v, mes_v, dia_v)
                estado_actual = input("Ingrese el estado actual de la tarea: ")
                porcentaje = int(input("Ingrese el procentaje de la tarea: "))
                numero_integrantes = int(input("Ingrese el numero de integrantes del equipo: "))
                equipo = []

                for i in range(numero_integrantes):
                    integrante = input(f"Ingrese el nombre del integrante {i+1} del equipo: ")
                    equipo.append(integrante)

                fecha_inicio_str = fecha_inicio.isoformat()
                fecha_vencimiento_str = fecha_vencimiento.isoformat()

                tarea = Tarea(id,nombre,empresa_cliente, descripcion, fecha_inicio_str,fecha_vencimiento_str, estado_actual, porcentaje, equipo)

                gestion_tareas.agregar_tarea_a_proyecto(id_proyecto,tarea, id_tarea_padre)

            except Exception as e :
                print(f"Ocurrio un error al agregar una tarea al proyecto: {e}")
        elif opcion == '3':
            try:
                id_proyecto = int(input("Ingresa el id del proyecto: "))
                id = int(input("Ingresa el id de la tarea: "))
                nombre = input("Ingresar el nombre de la tarea: ")
                empresa_cliente = input("Ingresar el nombre de la empresa del cliente de la tarea: ")
                descripcion = input("Descripcion de la tarea: ")
                dia_c = int(input("Ingresa el dia de creacion de la tarea: "))
                mes_c = int(input("Ingresa el mes de creacion de la tarea: "))
                year_c = int(input("Ingresa el mes de creacion de la tarea: "))
                fecha_inicio = datetime.date(year_c, mes_c, dia_c)
                dia_v = int(input("Ingresa el dia de vencimiento de la tarea: "))
                mes_v = int(input("Ingresa el mes de vencimiento de la tarea: "))
                year_v = int(input("Ingresa el mes de vencimiento de la tarea: "))
                fecha_vencimiento = datetime.date(year_v, mes_v, dia_v)
                estado_actual = input("Ingrese el estado actual de la tarea: ")
                porcentaje = int(input("Ingrese el procentaje de la tarea: "))
                numero_integrantes = int(input("Ingrese el numero de integrantes del equipo: "))
                equipo = []

                for i in range(numero_integrantes):
                    integrante = input(f"Ingrese el nombre del integrante {i+1} del equipo: ")
                    equipo.append(integrante)

                fecha_inicio_str = fecha_inicio.isoformat()
                fecha_vencimiento_str = fecha_vencimiento.isoformat()

                tarea = Tarea(id,nombre,empresa_cliente, descripcion, fecha_inicio_str,fecha_vencimiento_str, estado_actual, porcentaje, equipo)

                gestion_tareas.modificar_tarea_en_proyecto(id_proyecto,id, nombre = nombre, empresa_cliente = empresa_cliente, descripcion = descripcion, fecha_inicio = fecha_inicio_str, fecha_vencimiento = fecha_vencimiento_str, estado_actual = estado_actual, porcentaje = porcentaje, equipo = equipo)

            except Exception as e :
                print(f"Ocurrio un error al modificar una tarea al proyecto: {e}")
        elif opcion == '4':
            try:
                id_proyecto = int(input("Ingresa el id del proyecto: "))
                id = int(input("Ingresa el id de la tarea: "))

                gestion_tareas.eliminar_tarea_en_proyecto(id_proyecto,id)

            except Exception as e :
                print(f"Ocurrio un error al eliminar una tarea al proyecto: {e}")
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")



def menu_gestion_sprints():
    while True:
        print("\nMenu de Gestión de Sprints")
        print("1. Listar Sprints")
        print("2. Agregar Sprint")
        print("3. Agregar tarea al Sprint")
        print("4. Mostrar tareas en un nivel determinado")
        print("5. Mostrar subtareas de una tarea")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        print("\n")

        if opcion == '1':
            gestion_sprints.listar_sprints()
        elif opcion == '2':
            try:
                id_proyecto = int(input("Ingresa el id del proyecto: "))
                id = int(input("Ingresa el id de la tarea: "))
                dia_c = int(input("Ingresa el dia de creacion del sprint: "))
                mes_c = int(input("Ingresa el mes de creacion del sprint: "))
                year_c = int(input("Ingresa el mes de creacion del sprint: "))
                fecha_inicio = datetime.date(year_c, mes_c, dia_c)
                dia_v = int(input("Ingresa el dia de fin del sprint: "))
                mes_v = int(input("Ingresa el mes de fin del sprint: "))
                year_v = int(input("Ingresa el mes de fin del sprint: "))
                fecha_fin = datetime.date(year_v, mes_v, dia_v)

                fecha_inicio_str = fecha_inicio.isoformat()
                fecha_fin_str = fecha_fin.isoformat()

                sprint = Sprint(id,id_proyecto,fecha_inicio_str, fecha_fin_str)

                gestion_sprints.agregar_sprint(sprint)

            except Exception as e :
                print(f"Ocurrio un error al agregar una sprint al proyecto: {e}")
        elif opcion == '3':
            try:
                id_sprint = int(input("Ingresa el id del sprint: "))
                id = int(input("Ingresa el id de la tarea: "))
                nombre = input("Ingresar el nombre de la tarea: ")
                empresa_cliente = input("Ingresar el nombre de la empresa del cliente de la tarea: ")
                descripcion = input("Descripcion de la tarea: ")
                dia_c = int(input("Ingresa el dia de creacion de la tarea: "))
                mes_c = int(input("Ingresa el mes de creacion de la tarea: "))
                year_c = int(input("Ingresa el mes de creacion de la tarea: "))
                fecha_inicio = datetime.date(year_c, mes_c, dia_c)
                dia_v = int(input("Ingresa el dia de vencimiento de la tarea: "))
                mes_v = int(input("Ingresa el mes de vencimiento de la tarea: "))
                year_v = int(input("Ingresa el mes de vencimiento de la tarea: "))
                fecha_vencimiento = datetime.date(year_v, mes_v, dia_v)
                estado_actual = input("Ingrese el estado actual de la tarea: ")
                porcentaje = int(input("Ingrese el procentaje de la tarea: "))
                numero_integrantes = int(input("Ingrese el numero de integrantes del equipo: "))
                equipo = []

                for i in range(numero_integrantes):
                    integrante = input(f"Ingrese el nombre del integrante {i+1} del equipo: ")
                    equipo.append(integrante)

                fecha_inicio_str = fecha_inicio.isoformat()
                fecha_vencimiento_str = fecha_vencimiento.isoformat()

                tarea = Tarea(id,nombre,empresa_cliente, descripcion, fecha_inicio_str,fecha_vencimiento_str, estado_actual, porcentaje, equipo)

                gestion_sprints.agregar_tarea_a_sprint(id_sprint, tarea)

            except Exception as e :
                print(f"Ocurrio un error al agregar una sprint al proyecto: {e}")
        elif opcion == '4':
            try:
                nivel = int(input("Ingresa el nivel de la tarea que desea: "))

                gestion_sprints.mostrar_tareas_en_nivel(nivel)
            except Exception as e:
                print(f"Ocurrio un error al consultar el nivel de una tarea del sprint: {e}")
        elif opcion == '5':
            try:
                id_sprint = int(input("Ingresa el id del sprint: "))
                id_tarea = int(input("Ingresa el id de la tarea del sprint: "))

                gestion_sprints.mostrar_subtareas_de_tarea(id_sprint,id_tarea)
            except Exception as e:
                print(f"Ocurrio un error al mostrar las subtareas de una tarea del sprint: {e}")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_generar_reporte():
    while True:
        print("\nMenu de Gestión de Sprints")
        print("1. Identificar y mostrar las tareas criticas")
        print("2. Listar todos los sprite de un proyecto específico y en un nivel del árbol indicado")
        print("3. Listar todas las tareas asignadas a un determinado empleado")
        print("4. Recorrer en postorden las tares de un proyecto indicado por el usuario")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        print("\n")

        if opcion == '1':
           pass
        elif opcion == '2':
            # Código para agregar un sprint
            pass
        elif opcion == '3':
            # Código para modificar un sprint
            pass
        elif opcion == '4':
            # Código para eliminar un sprint
            pass
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")



# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas de los archivos
empresas_path = os.path.join(current_dir, 'data', 'empresas.json')
proyectos_path = os.path.join(current_dir, 'data', 'proyectos.json')
tareas_path = os.path.join(current_dir, 'data', 'tareas.json')
sprints_path = os.path.join(current_dir, 'data', 'sprints.json')


gestion_empresas = GestionEmpresas(empresas_path)

gestion_proyectos = GestionProyectos(proyectos_path)

gestion_tareas = GestionTareas(proyectos_path)

gestion_sprints = GestionSprints(sprints_path)

reporte = Reporte(empresas_path, proyectos_path, tareas_path, sprints_path)

menu_principal()