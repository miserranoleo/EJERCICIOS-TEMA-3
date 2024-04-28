class PersonajeStarWars:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class TablaHashStarWars:
    def __init__(self, tamano_inicial=20):
        self.tamano = tamano_inicial
        self.cantidad_elementos = 0
        self.tabla = [None] * tamano_inicial

    def hash(self, clave):
        return hash(clave) % self.tamano

    def agregar(self, personaje):
        if self.cantidad_elementos >= 0.75 * self.tamano:
            self._rehashing()
        indice = self.hash(personaje.nombre)
        if self.tabla[indice] is None:
            self.tabla[indice] = personaje
            self.cantidad_elementos += 1
        else:
            # Manejo de colisiones con lista enlazada
            if not isinstance(self.tabla[indice], list):
                self.tabla[indice] = [self.tabla[indice]]
            self.tabla[indice].append(personaje)
            self.cantidad_elementos += 1

    def buscar(self, nombre_personaje):
        indice = self.hash(nombre_personaje)
        if self.tabla[indice] is None:
            return None
        elif isinstance(self.tabla[indice], list):
            for personaje in self.tabla[indice]:
                if personaje.nombre == nombre_personaje:
                    return personaje
            return None
        else:
            return self.tabla[indice] if self.tabla[indice].nombre == nombre_personaje else None

    def _rehashing(self):
        nuevo_tamano = self.tamano * 2
        nueva_tabla = [None] * nuevo_tamano
        for elemento in self.tabla:
            if elemento is not None:
                if isinstance(elemento, list):
                    for personaje in elemento:
                        indice = self.hash(personaje.nombre)
                        if nueva_tabla[indice] is None:
                            nueva_tabla[indice] = personaje
                        else:
                            # Manejo de colisiones con lista enlazada
                            if not isinstance(nueva_tabla[indice], list):
                                nueva_tabla[indice] = [nueva_tabla[indice]]
                            nueva_tabla[indice].append(personaje)
                else:
                    indice = self.hash(elemento.nombre)
                    if nueva_tabla[indice] is None:
                        nueva_tabla[indice] = elemento
                    else:
                        # Manejo de colisiones con lista enlazada
                        if not isinstance(nueva_tabla[indice], list):
                            nueva_tabla[indice] = [nueva_tabla[indice]]
                        nueva_tabla[indice].append(elemento)
        self.tabla = nueva_tabla
        self.tamano = nuevo_tamano

# Ejemplo de uso:
tabla_star_wars = TablaHashStarWars()

# Agregar personajes
tabla_star_wars.agregar(PersonajeStarWars("Luke Skywalker", "Jedi que lucha contra el Imperio"))
tabla_star_wars.agregar(PersonajeStarWars("Darth Vader", "Lord Sith y líder del Imperio"))
tabla_star_wars.agregar(PersonajeStarWars("Leia Organa", "Princesa rebelde y líder de la Alianza Rebelde"))
tabla_star_wars.agregar(PersonajeStarWars("Han Solo", "Contrabandista y piloto del Halcón Milenario"))
tabla_star_wars.agregar(PersonajeStarWars("Yoda", "Maestro Jedi y sabio anciano"))

# Buscar personajes
print("Buscar 'Darth Vader':", tabla_star_wars.buscar("Darth Vader").descripcion)
print("Buscar 'Yoda':", tabla_star_wars.buscar("Yoda").descripcion)
print("Buscar 'Leia Organa':", tabla_star_wars.buscar("Leia Organa").descripcion)
print("Buscar 'C-3PO':", tabla_star_wars.buscar("C-3PO"))

# Agregar más personajes para provocar un rehashing
tabla_star_wars.agregar(PersonajeStarWars("Chewbacca", "Leal compañero de Han Solo"))
tabla_star_wars.agregar(PersonajeStarWars("Obi-Wan Kenobi", "Maestro Jedi y mentor de Luke Skywalker"))

# Buscar personajes nuevamente
print("Buscar 'Chewbacca':", tabla_star_wars.buscar("Chewbacca").descripcion)
print("Buscar 'Obi-Wan Kenobi':", tabla_star_wars.buscar("Obi-Wan Kenobi").descripcion)
