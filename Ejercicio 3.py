def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr

# Ejemplo de uso:
arr = [3, 6, 8, 1, 4, 2, 9, 5, 7]
sorted_arr = shell_sort(arr)
print("Arreglo ordenado por Shell Sort:", sorted_arr)
