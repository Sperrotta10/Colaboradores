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
