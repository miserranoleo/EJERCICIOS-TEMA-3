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

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

def contar_ocurrencias(pila, elemento):
    contador = 0
    pila_aux = Pila()

    # Recorrer la pila principal y contar las ocurrencias
    while not pila.esta_vacia():
        valor = pila.desapilar()
        if valor == elemento:
            contador += 1
        pila_aux.apilar(valor)

    # Restaurar la pila principal
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return contador

def eliminar_impares(pila):
    pila_aux = Pila()

    # Filtrar los números pares y apilarlos en una pila auxiliar
    while not pila.esta_vacia():
        valor = pila.desapilar()
        if valor % 2 == 0:
            pila_aux.apilar(valor)

    # Restaurar la pila principal
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

# Ejemplo de uso:
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)

print("Número de ocurrencias de 2 en la pila:", contar_ocurrencias(pila, 2))

eliminar_impares(pila)
print("Pila después de eliminar los números impares:", end=" ")
while not pila.esta_vacia():
    print(pila.desapilar(), end=" ")

def eliminar_impares(pila):
    pila_aux = Pila()

    # Filtrar los números pares y apilarlos en una pila auxiliar
    while not pila.esta_vacia():
        valor = pila.desapilar()
        if valor % 2 == 0:
            pila_aux.apilar(valor)

    # Restaurar la pila principal
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
