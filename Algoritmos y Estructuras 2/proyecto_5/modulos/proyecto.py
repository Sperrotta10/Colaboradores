import json
from datetime import datetime
from avl_tree import AVLTree, Node


class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
        self.estado_actual = estado_actual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def listar_tareas(self):
        return self.tareas

    def eliminar_tarea(self, id):
        self.tareas = [tarea for tarea in self.tareas if tarea.id != id]

    def buscar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea
            subtarea = self.buscar_subtarea(tarea, id)
            if subtarea:
                return subtarea
        return None
    
    def buscar_subtarea(self, tarea, id):
        for subtarea in tarea.subtareas:
            if subtarea.id == id:
                return subtarea
            sub_subtarea = self.buscar_subtarea(subtarea, id)
            if sub_subtarea:
                return sub_subtarea
        return None

    def tiempo_restante(self):
        return (self.fecha_vencimiento - datetime.now()).days



class GestionProyectos:
    def __init__(self, file_path):
        self.file_path = file_path
        self.arbol_avl = AVLTree()
        self.root = None
        self.cargar_proyectos()

    def cargar_proyectos(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    proyecto = Proyecto(**item)
                    self.root = self.arbol_avl.insert(self.root, proyecto.tiempo_restante(), proyecto)
        except FileNotFoundError:
            print(f"No se encontró el archivo de datos del proyecto: {self.file_path}")

    def listar_proyectos(self):
        proyectos = self.arbol_avl.pre_order(self.root)
        for proyecto in proyectos:
            print(vars(proyecto))

    def agregar_proyecto(self, proyecto):
        self.root = self.arbol_avl.insert(self.root, proyecto.tiempo_restante(), proyecto)
        self.guardar_proyectos()

    def consultar(self, **criterios):
        proyectos = self.arbol_avl.pre_order(self.root)
        for proyecto in proyectos:
            match = True
            for key, value in criterios.items():
                if getattr(proyecto, key) != value:
                    match = False
                    break
            if match:
                return proyecto
        return None

    def modificar_proyecto(self, id, **kwargs):
        proyectos = self.arbol_avl.pre_order(self.root)
        for nodo in proyectos:
            proyecto = nodo.value
            if proyecto.id == id:
                # Eliminar el nodo antiguo basado en el tiempo restante antiguo
                self.root = self.arbol_avl.delete(self.root, proyecto.tiempo_restante())
                # Actualizar el proyecto con los nuevos valores
                for key, value in kwargs.items():
                    if key in ['fecha_inicio', 'fecha_vencimiento']:
                        value = datetime.strptime(value, '%Y-%m-%d')
                    setattr(proyecto, key, value)
                # Insertar el nodo actualizado con el nuevo tiempo restante
                self.root = self.arbol_avl.insert(self.root, proyecto.tiempo_restante(), proyecto)
                self.guardar_proyectos()
                return
        print("Proyecto no encontrado")

    def guardar_proyectos(self):
        proyectos = self.arbol_avl.pre_order(self.root)
        data = [vars(proyecto) for proyecto in proyectos]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, default=str)



gestion_proyectos = GestionProyectos('../data/proyectos.json')
#gestion_proyectos.listar_proyectos()
gestion_proyectos.consultar(gerente='gerente1')