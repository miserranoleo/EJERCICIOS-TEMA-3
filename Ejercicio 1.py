def invertir_secuencia(secuencia):
    if len(secuencia) == 0:
        return secuencia
    else:
        return secuencia[-1] + invertir_secuencia(secuencia[:-1])

# Ejemplo de uso:
secuencia_original = "Hola mundo"
secuencia_invertida = invertir_secuencia(secuencia_original)
print("Secuencia original:", secuencia_original)
print("Secuencia invertida:", secuencia_invertida)
