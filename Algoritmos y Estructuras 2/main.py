from modulo_gestion_proyectos import *

while True:
    print("\nMenu de Opciones")
    print("1- Menu 1")
    print("2- Menu 2")
    print("3- Menu 3")
    print("4- Salir del Menu\n")

    opc = input("Escoja la opción que desea ejecutar: ")



    # Verificación de que la entrada es un entero válido
    try:
        opc = int(opc)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue  

    if opc == 1:
        #Gestion_proyectos()
        proyecto = Gestion_proyectos()
        lista_proyectos = proyecto.get_lista_proyectos()

    elif opc == 2:
        Gestion_Tareas_prioridades()
        print("Hola 2")
    elif opc == 3:
        print("Hola 3")
    elif opc == 4:
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 6.")