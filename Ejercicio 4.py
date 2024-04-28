import shelve

class ManejadorArchivos:
    def __init__(self):
        self.archivo = None
    
    def abrir(self, ruta):
        """
        Abre el archivo en la ruta especificada.
        """
        self.archivo = shelve.open(ruta, writeback=True)
    
    def cerrar(self):
        """
        Cierra el archivo.
        """
        if self.archivo is not None:
            self.archivo.close()
            self.archivo = None
    
    def leer(self, posicion):
        """
        Lee el dato en la posición especificada del archivo.
        """
        if self.archivo is not None:
            return self.archivo[str(posicion)]
        else:
            raise Exception("El archivo no está abierto.")
    
    def guardar(self, dato):
        """
        Guarda el dato en el archivo.
        """
        if self.archivo is not None:
            posicion = len(self.archivo)
            self.archivo[str(posicion)] = dato
        else:
            raise Exception("El archivo no está abierto.")
    
    def modificar(self, posicion, dato):
        """
        Modifica el dato en la posición especificada del archivo.
        """
        if self.archivo is not None:
            self.archivo[str(posicion)] = dato
        else:
            raise Exception("El archivo no está abierto.")

# Ejemplo de uso:
manejador = ManejadorArchivos()

# Abrir un archivo
manejador.abrir("datos.db")

# Guardar algunos datos
manejador.guardar("Dato 1")
manejador.guardar("Dato 2")
manejador.guardar("Dato 3")

# Leer un dato
dato_leido = manejador.leer(1)
print("Dato leído:", dato_leido)

# Modificar un dato
manejador.modificar(0, "Nuevo dato")

# Cerrar el archivo
manejador.cerrar()
