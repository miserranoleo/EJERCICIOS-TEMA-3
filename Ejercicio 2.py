def bucket_sort(arr):
    # Encontrar el valor máximo y mínimo en el arreglo
    max_val = max(arr)
    min_val = min(arr)
    
    # Crear un arreglo de casilleros
    buckets = [[] for _ in range(max_val - min_val + 1)]
    
    # Colocar cada elemento en su respectivo casillero
    for num in arr:
        buckets[num - min_val].append(num)
    
    # Ordenar cada casillero y concatenar los resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Ejemplo de uso:
arr = [3, 6, 8, 1, 4, 2, 9, 5, 7]
sorted_arr = bucket_sort(arr)
print("Arreglo ordenado por casilleros:", sorted_arr)
