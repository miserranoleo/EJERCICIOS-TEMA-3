from collections import deque

class NodoListaEnlazada:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [None] * tamano

    def hash(self, clave):
        return hash(clave) % self.tamano

    def agregar(self, clave, valor):
        indice = self.hash(clave)
        if self.tabla[indice] is None:
            self.tabla[indice] = NodoListaEnlazada(clave, valor)
        else:
            nodo_actual = self.tabla[indice]
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = NodoListaEnlazada(clave, valor)

    def buscar(self, clave):
        indice = self.hash(clave)
        nodo_actual = self.tabla[indice]
        while nodo_actual is not None:
            if nodo_actual.clave == clave:
                return nodo_actual.valor
            nodo_actual = nodo_actual.siguiente
        return None

    def borrar(self, clave):
        indice = self.hash(clave)
        nodo_actual = self.tabla[indice]
        if nodo_actual is None:
            return False
        elif nodo_actual.clave == clave:
            self.tabla[indice] = nodo_actual.siguiente
            return True
        else:
            while nodo_actual.siguiente is not None:
                if nodo_actual.siguiente.clave == clave:
                    nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                    return True
                nodo_actual = nodo_actual.siguiente
            return False

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(clave, valor)
        else:
            self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        if clave < nodo.clave:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.derecha, clave, valor)
        else:
            nodo.valor = valor  # Si la clave ya existe, actualiza el valor

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierda, clave)
        else:
            return self._buscar_recursivo(nodo.derecha, clave)

    def borrar(self, clave):
        self.raiz = self._borrar_recursivo(self.raiz, clave)

    def _borrar_recursivo(self, nodo, clave):
        if nodo is None:
            return None
        if clave < nodo.clave:
            nodo.izquierda = self._borrar_recursivo(nodo.izquierda, clave)
        elif clave > nodo.clave:
            nodo.derecha = self._borrar_recursivo(nodo.derecha, clave)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            else:
                sucesor = self._encontrar_minimo(nodo.derecha)
                nodo.clave = sucesor.clave
                nodo.valor = sucesor.valor
                nodo.derecha = self._borrar_recursivo(nodo.derecha, sucesor.clave)
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Diccionario:
    def __init__(self):
        self.tabla_hash = TablaHash(28)
        self.arbol_binario = ArbolBinarioBusqueda()

    def agregar_palabra(self, palabra, significado):
        self.tabla_hash.agregar(palabra, significado)
        self.arbol_binario.insertar(palabra, significado)

    def buscar_palabra(self, palabra):
        significado = self.tabla_hash.buscar(palabra)
        if significado is not None:
            return significado
        else:
            return self.arbol_binario.buscar(palabra)

    def borrar_palabra(self, palabra):
        return self.tabla_hash.borrar(palabra)

# Ejemplo de uso:
diccionario = Diccionario()
diccionario.agregar_palabra("hola", "saludo")
diccionario.agregar_palabra("adios", "despedida")
diccionario.agregar_palabra("gato", "animal")

print("Buscar 'hola':", diccionario.buscar_palabra("hola"))
print("Buscar 'adios':", diccionario.buscar_palabra("adios"))
print("Buscar 'gato':", diccionario.buscar_palabra("gato"))

print("Borrar 'hola':", diccionario.borrar_palabra("hola"))
print("Buscar 'hola' después de borrar:", diccionario.buscar_palabra("hola"))
