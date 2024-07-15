import json
from datetime import datetime

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key, data=None):
        if not root:
            return Node(key, data)
        elif key < root.key:
            root.left = self.insert(root.left, key, data)
        else:
            root.right = self.insert(root.right, key, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root

    def pre_order(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res

    def post_order(self, root):
        res = []
        if root:
            res = res + self.post_order(root.left)
            res = res + self.post_order(root.right)
            res.append(root.data)
        return res


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
            for item in data['sprints']:
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


