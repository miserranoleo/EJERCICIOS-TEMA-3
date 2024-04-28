class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None
    
    def agregar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def contar_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

# Ejemplo de uso:
lista = Lista()
lista.agregar_al_principio(3)
lista.agregar_al_principio(5)
lista.agregar_al_principio(7)

print("Cantidad de nodos en la lista:", lista.contar_nodos())
