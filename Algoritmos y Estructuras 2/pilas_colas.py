class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
        self.tamano = 0
    
    def esta_vacia(self):
        return self.tope is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        nodo_nuevo.siguiente = self.tope
        self.tope = nodo_nuevo
        self.tamano += 1
    
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente
            self.tamano -= 1
            return valor_eliminado
    
    def eliminar_en_posicion(self, posicion):
        if posicion < 0 or posicion >= self.tamano:
            print("Posición fuera de rango")
            return None

        nodo_actual = self.tope
        
        if posicion == 0:
            nodo_a_eliminar = nodo_actual
            self.tope = nodo_actual.siguiente
        else:
            for i in range(posicion - 1):
                nodo_actual = nodo_actual.siguiente
                if nodo_actual.siguiente is None:
                    print("Posición fuera de rango")
                    return None

            nodo_a_eliminar = nodo_actual.siguiente
            if nodo_a_eliminar is not None:
                nodo_actual.siguiente = nodo_a_eliminar.siguiente
            else:
                nodo_actual.siguiente = None

        self.tamano -= 1
        return nodo_a_eliminar.valor

    
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
            print(nodo.valor)
            self._recorrer_aux(nodo.siguiente)
    
    def obtener_valor_en_indice(self, indice):
        nodo_actual = self.tope
        contador = 0
        
        while nodo_actual is not None:
            if contador == indice:
                return nodo_actual.valor
            nodo_actual = nodo_actual.siguiente
            contador += 1
        
        print(f"El índice {indice} está fuera del rango de la pila.")
        return None
    
    def get_largo(self):
        return self.tamano
    
    def insertar_en_posicion(self, valor, posicion):
        if posicion < 0 or posicion > self.tamano:
            print("Posición fuera de rango")
            return
        
        nodo_nuevo = Nodo(valor)
        
        if posicion == 0:
            nodo_nuevo.siguiente = self.tope
            self.tope = nodo_nuevo
        else:
            nodo_actual = self.tope
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.siguiente
            nodo_nuevo.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_nuevo
        
        self.tamano += 1



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

