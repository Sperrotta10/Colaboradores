import json
from datetime import datetime
from modulos.avl_tree import AVLTree, Node

class Sprint:
    def __init__(self, id, proyecto_id, fecha_inicio, fecha_fin, tareas):
        self.id = id
        self.proyecto_id = proyecto_id
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        self.tareas = tareas

    def duracion(self):
        return (self.fecha_fin - self.fecha_inicio).days



class GestionSprints:
    def __init__(self, file_path):
        self.file_path = file_path
        self.arbol_avl = AVLTree()
        self.root = None
        self.cargar_sprints()


    def cargar_sprints(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                sprint = Sprint(**item)
                self.root = self.arbol_avl.insert(self.root, sprint.duracion(), sprint)


    def listar_sprints(self):
        sprints = self.arbol_avl.pre_order(self.root)
        for sprint in sprints:
            print(vars(sprint))


    def agregar_sprint(self, sprint):
        self.root = self.arbol_avl.insert(self.root, sprint.duracion(), sprint)
        self.guardar_sprints()


    def agregar_tarea_a_sprint(self, sprint_id, tarea):
        sprint = self.arbol_avl.buscar(self.root, sprint_id)
        if sprint:
            # Lógica para verificar si la tarea está disponible para ser agregada
            # y agregarla al sprint si cumple con los criterios
            if tarea.estado_actual != "completada":  # Verificar que la tarea no esté completada
                sprint.data.agregar_tarea(tarea)
                self.guardar_sprints()
                print(f"Tarea '{tarea.nombre}' agregada al sprint '{sprint.data.nombre}'.")
            else:
                print("La tarea ya está completada y no puede ser agregada a un sprint.")
        else:
            print("Sprint no encontrado")


    def mostrar_tareas_en_nivel(self, nivel):
        sprints = self.arbol_avl.pre_order(self.root)
        for sprint in sprints:
            print(f"Tareas en el nivel {nivel} del sprint '{sprint.nombre}':")
            self._mostrar_tareas_en_nivel_recursivo(sprint.tareas, nivel, current_level=1)

    def _mostrar_tareas_en_nivel_recursivo(self, tareas, nivel, current_level):
        for tarea in tareas:
            if current_level == nivel:
                print(vars(tarea))
            elif tarea.subtareas:
                self._mostrar_tareas_en_nivel_recursivo(tarea.subtareas, nivel, current_level + 1)


    def mostrar_subtareas_de_tarea(self, sprint_id, tarea_id):
        sprint = self.arbol_avl.buscar(self.root, sprint_id)
        if sprint:
            tarea = sprint.data.buscar_tarea(tarea_id)
            if tarea:
                sprint.data.mostrar_subtareas(tarea_id)
            else:
                print("Tarea no encontrada en el sprint.")
        else:
            print("Sprint no encontrado")


    def guardar_sprints(self):
        sprints = self.arbol_avl.pre_order(self.root)
        data = [vars(sprint) for sprint in sprints]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, default=str)


