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




class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo, tareas = []):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
        self.estado_actual = estado_actual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas = tareas

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
                for item in data['proyectos']:
                    proyecto = Proyecto(**item)
                    self.root = self.arbol_avl.insert(self.root, proyecto.tiempo_restante(), proyecto)
        except FileNotFoundError:
            print(f"No se encontró el archivo de datos del proyecto: {self.file_path}")

    def listar_proyectos(self):
        proyectos = self.arbol_avl.pre_order(self.root)
        for proyecto in proyectos:
            print(f"ID: {proyecto.id}")
            print(f"Nombre: {proyecto.nombre}")
            print(f"Descripción: {proyecto.descripcion}")
            print(f"Fecha de inicio: {proyecto.fecha_inicio.strftime('%Y-%m-%d')}")
            print(f"Fecha de vencimiento: {proyecto.fecha_vencimiento.strftime('%Y-%m-%d')}")
            print(f"Estado actual: {proyecto.estado_actual}")
            print(f"Empresa: {proyecto.empresa}")
            print(f"Gerente: {proyecto.gerente}")
            print(f"Equipo: {', '.join(proyecto.equipo)}")

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


    def eliminar(self, **criterios):
        proyectos = self.arbol_avl.pre_order(self.root)
        eliminados = []
        for proyecto in proyectos:
            match = True
            for key, value in criterios.items():
                if getattr(proyecto, key) != value:
                    match = False
                    break
            if match:
                self.root = self.arbol_avl.delete(self.root, proyecto.tiempo_restante(), proyecto)
                eliminados.append(proyecto)
        if eliminados:
            self.guardar_proyectos()
        return eliminados

    def guardar_proyectos(self):
        data = {'proyectos': []}
        proyectos = self.arbol_avl.pre_order(self.root)
        for proyecto in proyectos:
            proyecto_data = {
                'id': proyecto.id,
                'nombre': proyecto.nombre,
                'descripcion': proyecto.descripcion,
                'fecha_inicio': proyecto.fecha_inicio.strftime('%Y-%m-%d'),
                'fecha_vencimiento': proyecto.fecha_vencimiento.strftime('%Y-%m-%d'),
                'estado_actual': proyecto.estado_actual,
                'empresa': proyecto.empresa,
                'gerente': proyecto.gerente,
                'equipo': proyecto.equipo
            }
            data['proyectos'].append(proyecto_data)

        try:
            with open(self.file_path, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=2)
        except IOError:
            print(f"Error al guardar el archivo JSON: {self.file_path}")



gestion_proyectos = GestionProyectos('../data/proyectos.json')
#gestion_proyectos.listar_proyectos()
gestion_proyectos.consultar(gerente='gerente1')