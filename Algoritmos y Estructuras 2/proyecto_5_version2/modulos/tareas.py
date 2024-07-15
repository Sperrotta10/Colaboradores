import json
from datetime import datetime
from modulos.proyecto import Proyecto


class NarioNodo:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.hijos = []



class NarioArbol:
    def __init__(self):
        self.root = None

    def agregar(self, padre_key, key, data=None):
        nuevo_nodo = NarioNodo(key, data)
        if self.root is None:
            self.root = nuevo_nodo
        else:
            padre = self.buscar(self.root, padre_key)
            if padre:
                padre.hijos.append(nuevo_nodo)

    def buscar(self, nodo, key):
        if nodo is None:
            return None
        if nodo.key == key:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar(hijo, key)
            if resultado:
                return resultado
        return None

    def listar(self, nodo):
        resultado = []
        if nodo:
            resultado.append(nodo.data)
            for hijo in nodo.hijos:
                resultado.extend(self.listar(hijo))
        return resultado

    def eliminar(self, key):
        if self.root is None:
            return False
        if self.root.key == key:
            self.root = None
            return True
        return self._eliminar(self.root, key)

    def _eliminar(self, nodo, key):
        for i, hijo in enumerate(nodo.hijos):
            if hijo.key == key:
                nodo.hijos.pop(i)
                return True
            elif self._eliminar(hijo, key):
                return True
        return False



class Tarea:
    def __init__(self, id, nombre, empresa_cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.subtareas = []

    def agregar_subtareas(self,subtarea):
        self.subtareas.append(subtarea)

    def listar_subtareas(self):
        return self.subtareas

    def eliminar_subtarea(self, id):
        self.subtareas = [sub for sub in self.subtareas if sub.id != id]



class GestionTareas:
    def __init__(self, file_path):
        self.file_path = file_path
        self.arbol_nario = NarioArbol()
        self.cargar_tareas()


    def cargar_tareas(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            for item in data['proyectos']:
                proyecto = Proyecto(**item)
                if 'padre_id' in item:
                    self.arbol_nario.agregar(item['padre_id'], proyecto.id, proyecto)
                else:
                    self.arbol_nario.agregar(None, proyecto.id, proyecto)


    def agregar_tarea_a_proyecto(self, proyecto_id, tarea, padre_id=None):
        proyecto = self.arbol_nario.buscar(self.arbol_nario.root, proyecto_id)
        if proyecto:
            if padre_id:
                tarea_padre = proyecto.data.buscar_tarea(padre_id)
                if tarea_padre:
                    tarea_padre.agregar_subtarea(tarea)
                else:
                    print("Tarea padre no encontrada")
            else:
                proyecto.data.agregar_tarea(tarea)
            self.guardar_proyectos()
        else:
            print("Proyecto no encontrado")


    def modificar_tarea_en_proyecto(self, proyecto_id, tarea_id, **kwargs):
        proyecto = self.arbol_nario.buscar(self.arbol_nario.root, proyecto_id)
        if proyecto:
            tarea = proyecto.data.buscar_tarea(tarea_id)
            if tarea:
                for key, value in kwargs.items():
                    if key in ['fecha_inicio', 'fecha_vencimiento']:
                        value = datetime.strptime(value, '%Y-%m-%d')
                    setattr(tarea, key, value)
                self.guardar_proyectos()
            else:
                print("Tarea no encontrada")
        else:
            print("Proyecto no encontrado")


    def eliminar_tarea_en_proyecto(self, proyecto_id, tarea_id):
        proyecto = self.arbol_nario.buscar(self.arbol_nario.root, proyecto_id)
        if proyecto:
            tarea = proyecto.data.buscar_tarea(tarea_id)
            if tarea:
                proyecto.data.eliminar_tarea(tarea_id)
                self.guardar_proyectos()
            else:
                print("Tarea no encontrada")
        else:
            print("Proyecto no encontrado")


    def consultar_una_tarea_del_proyecto(self, proyecto_id, tarea_id):
        proyecto = self.arbol_nario.buscar(self.arbol_nario.root, proyecto_id)
        if proyecto:
            tarea = proyecto.data.buscar_tarea(tarea_id)
            if tarea:
                print(vars(tarea))
            else:
                print("Tarea no encontrada en el proyecto especificado.")
        else:
            print("Proyecto no encontrado.")


    def listar_tareas_del_proyecto(self, proyecto_id):
        proyecto = self.arbol_nario.buscar(self.arbol_nario.root, proyecto_id)
        if proyecto:
            print(f"Tareas del proyecto '{proyecto.data.nombre}':")
            self._listar_tareas_recursivo(proyecto.data.tareas, nivel=0)
        else:
            print("Proyecto no encontrado.")


    def _listar_tareas_recursivo(self, tareas, nivel):
        for tarea in tareas:
            print(f"{'  ' * nivel}{tarea.nombre}")
            if tarea.subtareas:
                self._listar_tareas_recursivo(tarea.subtareas, nivel + 1)


    def guardar_proyectos(self):
        proyectos = self.arbol_nario.listar(self.arbol_nario.root)
        data = [vars(proyecto) for proyecto in proyectos]
        for proyecto in data:
            proyecto['tareas'] = [vars(tarea) for tarea in proyecto['tareas']]
            for tarea in proyecto['tareas']:
                tarea['subtareas'] = [vars(subtarea) for subtarea in tarea['subtareas']]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, default=str)


