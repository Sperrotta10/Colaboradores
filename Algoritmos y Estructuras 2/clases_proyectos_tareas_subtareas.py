# Clase de los proyectos
import pilas_colas
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
        self.tareas = pilas_colas.Pila()

    def agregar_tareas(self,tareas):
        self.tareas.agregar(tareas)

    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nFecha de Inicio: {self.fecha_de_inicio.strftime('%Y-%m-%d')}\nFecha de Vencimiento: {self.fecha_de_vencimiento.strftime('%Y-%m-%d')}\nEstado Actual: {self.estado_actual}\nEmpresa: {self.empresa}\nGerente: {self.gerente}\nEquipo: {', '.join(self.equipo)}"


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
        self.subtareas = pilas_colas.Cola()

    def agregar_subtarea(self,subtarea):
        self.subtareas.agregar(subtarea)

# Clase de las subtareas de las tareas del proyecto
class Subtarea:
    def __init__(self,identificador,titulo,descripcion,condicion) -> None:
        self.identificador =identificador
        self.titulo =titulo
        self.descripcion=descripcion
        self.condicion=condicion