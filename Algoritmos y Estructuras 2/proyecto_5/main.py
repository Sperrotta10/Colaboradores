import configparser
from datetime import datetime
from modulos.empresa import GestionEmpresas, Empresa
from modulos.proyecto import GestionProyectos
from modulos.tareas import GestionTareas
from modulos.sprint import GestionSprints
from modulos.reporte import Reporte

def cargar_configuracion(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
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
        print("5. Listar Proyectos de una Empresa")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

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
                fecha_creacion = datetime(year_c, mes_c, dia_c)
                direccion = input("Ingrese la direccion de la empresa: ")
                telefono = input("Ingrese el numero de telefono de la empresa: ")
                correo = input("Ingre el correo de la empresa: ")
                gerente = input("Ingrese el gerente de la empresa: ")
                numero_integrantes = int("Ingrese el numero de integrantes del equipo: ")
                equipo = []

                for i in range(numero_integrantes):
                    nombre = input(f"Ingrese el nombre del integrante {i+1} del equipo")
                    equipo.append(nombre)

                empresa = Empresa(id,nombre,descripcion,fecha_creacion,direccion,telefono,correo,gerente)

                gestion_empresas.agregar_empresa(empresa)

            except Exception as e :
                print(f"Ocurrio un error al agregar una empresa: {e}")

            
        elif opcion == '3':
            # Código para modificar una empresa
            pass
        elif opcion == '4':
            # Código para eliminar una empresa
            pass
        elif opcion == '5':
            empresa_id = input("Ingrese el ID de la empresa: ")
            gestion_empresas.listar_proyectos_de_empresa(empresa_id)
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

        if opcion == '1':
            gestion_proyectos.listar_proyectos()
        elif opcion == '2':
            # Código para agregar un proyecto
            pass
        elif opcion == '3':
            # Código para modificar un proyecto
            pass
        elif opcion == '4':
            # Código para eliminar un proyecto
            pass
        elif opcion == '5':
            # Código para buscar proyectos por criterios
            pass
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

        if opcion == '1':
            gestion_tareas.listar_tareas()
        elif opcion == '2':
            # Código para agregar una tarea
            pass
        elif opcion == '3':
            # Código para modificar una tarea
            pass
        elif opcion == '4':
            # Código para eliminar una tarea
            pass
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")



def menu_gestion_sprints():
    while True:
        print("\nMenu de Gestión de Sprints")
        print("1. Listar Sprints")
        print("2. Agregar Sprint")
        print("3. Modificar Sprint")
        print("4. Eliminar Sprint")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_sprints.listar_sprints()
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


def menu_generar_reporte():
    while True:
        print("\nMenu de Gestión de Sprints")
        print("1. Identificar y mostrar las tareas criticas")
        print("2. Listar todos los sprite de un proyecto específico y en un nivel del árbol indicado")
        print("3. Listar todas las tareas asignadas a un determinado empleado")
        print("4. Recorrer en postorden las tares de un proyecto indicado por el usuario")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

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



if __name__ == "__main__":
    config = cargar_configuracion('config/config.txt')
    empresas_file = config['paths']['empresas']
    proyectos_file = config['paths']['proyectos']
    tareas_file = config['paths']['tareas']
    sprints_file = config['paths']['sprints']

    gestion_empresas = GestionEmpresas(empresas_file)

    gestion_proyectos = GestionProyectos(proyectos_file)

    gestion_tareas = GestionTareas(tareas_file)

    gestion_sprints = GestionSprints(sprints_file)

    reporte = Reporte(empresas_file, proyectos_file, tareas_file, sprints_file)

    menu_principal()