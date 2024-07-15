import json


class Nodo:
    def __init__(self, data=None):
        self.data = data
        self.next = None



class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, data):
        new_node = Nodo(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def listar(self):
        empresas = []
        current = self.head
        while current:
            empresas.append(current.data)
            current = current.next
        return empresas

    def buscar(self, id):
        current = self.head
        while current:
            if current.data.id == id:
                return current.data
            current = current.next
        return None

    def eliminar(self, id):
        current = self.head
        prev = None
        while current:
            if current.data.id == id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False




class Empresa:
    def __init__(self, id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipo_contacto = equipo_contacto
        self.proyectos = []

    def agregar_proyectos(self, proyecto):
        self.proyectos.append(proyecto) 



class GestionEmpresas:
    def __init__(self, file_path):
        self.file_path = file_path
        self.empresas = ListaEnlazada()
        self.cargar_empresas()

    def cargar_empresas(self):
        try:
            with open(self.file_path, 'r') as jsonfile:
                data = json.load(jsonfile)
                for empresa_data in data['empresas']:
                    empresa = Empresa(**empresa_data)
                    self.empresas.agregar(empresa)
        except FileNotFoundError:
            print(f"No se encontró el archivo de datos de empresas: {self.file_path}")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON: {self.file_path}")

    def listar_empresas(self):
        try:
            for empresa in self.empresas.listar():
                print(vars(empresa))
        except:
            print("Ocurrio un error al listar las empresa o no existe ninguna empresa")

    def agregar_empresa(self, empresa):
        self.empresas.agregar(empresa)
        self.guardar_empresas()

    def modificar_empresa(self, id, **kwargs):
        empresa = self.empresas.buscar(id)
        if empresa:
            for key, value in kwargs.items():
                setattr(empresa, key, value)
            self.guardar_empresas()
        else:
            print("Empresa no encontrada")

    def eliminar_empresa(self, id):
        if self.empresas.eliminar(id):
            self.guardar_empresas()
        else:
            print("Empresa no encontrada")

    def consultar_empresa(self, id):
        empresa = self.empresas.buscar(id)
        if empresa:
            print(f"Detalles de la empresa con ID {id}:")
            print(f"Nombre: {empresa.nombre}")
            print(f"Descripción: {empresa.descripcion}")
            print(f"Fecha de creación: {empresa.fecha_creacion}")
            print(f"Dirección: {empresa.direccion}")
            print(f"Teléfono: {empresa.telefono}")
            print(f"Correo: {empresa.correo}")
            print(f"Gerente: {empresa.gerente}")
            print(f"Equipo de contacto: {empresa.equipo_contacto}")
            try:
                print(f"Proyectos: {[p.nombre for p in empresa.proyectos]}")
            except Exception as e:
                print(f"Ocurrio un error: {e}")
        else:
            print(f"No se encontró una empresa con el ID {id}")

    def guardar_empresas(self):
        data = {'empresas': []}
        for empresa in self.empresas.listar():
            empresa_data = {
                'id': empresa.id,
                'nombre': empresa.nombre,
                'descripcion': empresa.descripcion,
                'fecha_creacion': empresa.fecha_creacion,
                'direccion': empresa.direccion,
                'telefono': empresa.telefono,
                'correo': empresa.correo,
                'gerente': empresa.gerente,
                'equipo_contacto': empresa.equipo_contacto
            }
            data['empresas'].append(empresa_data)
    
        try:
            with open(self.file_path, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=2)
        except IOError:
            print(f"Error al guardar el archivo JSON: {self.file_path}")


