class Cola:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def encolar(self, elemento):
        self.items.append(elemento)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, elemento):
        self.items.append(elemento)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

def eliminar_vocales(cola):
    pila = Pila()

    # Procesar la cola y almacenar las letras que no son vocales en una pila
    while not cola.esta_vacia():
        caracter = cola.desencolar()
        if caracter.lower() not in "aeiou":
            pila.apilar(caracter)

    # Volver a poner las letras en la cola
    while not pila.esta_vacia():
        cola.encolar(pila.desapilar())

# Ejemplo de uso:
cola = Cola()
cola.encolar('h')
cola.encolar('o')
cola.encolar('l')
cola.encolar('a')

print("Cola original:", end=" ")
while not cola.esta_vacia():
    print(cola.desencolar(), end=" ")

print()

cola.encolar('h')
cola.encolar('o')
cola.encolar('l')
cola.encolar('a')

eliminar_vocales(cola)

print("Cola sin vocales:", end=" ")
while not cola.esta_vacia():
    print(cola.desencolar(), end=" ")
