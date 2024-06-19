class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
    
    def esta_vacia(self):
        return self.tope is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        nodo_nuevo.siguiente = self.tope
        self.tope = nodo_nuevo
    
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente
            return valor_eliminado
    
    def ver_tope(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.valor
    
    def recorrer(self):
        if self.esta_vacia():
            print("La pila está vacía")
        else:
            self._recorrer_aux(self.tope)
    
    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print(nodo.valor.nombre)
            self._recorrer_aux(nodo.siguiente)

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
    
    def esta_vacia(self):
        return self.frente is None
    
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
    
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.frente.valor
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            return valor_eliminado
    
    def ver_frente(self):
        if self.esta_vacia():
            return None
        else:
            return self.frente.valor
    
    def recorrer(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            actual = self.frente
            while actual:
                print(actual.valor)
                actual = actual.siguiente

