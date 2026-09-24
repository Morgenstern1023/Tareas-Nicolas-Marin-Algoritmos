#Función Bucket Sort con 5 cubos, mide comparaciones e intercambios
def bucket_sort(arr):
    intercambios = 0
    n = len(arr)
    if n <= 0:
        return

    max_val = max(arr)
    bucket_count = 5
    buckets = [[] for _ in range(bucket_count)]

    for i in range(n):
        idx = arr[i] * bucket_count // (max_val + 1)
        buckets[idx].append(arr[i])
        intercambios += 1

    arr.clear()
    for i in range(bucket_count):
        buckets[i].sort()
        for j in range(len(buckets[i])):
            arr.append(buckets[i][j])
            intercambios += 1
    return arr, intercambios

#Ejemplo de uso con 50 elementos (Hecho por copilot)
import random
import time

datos = [random.randint(0, 100) for _ in range(50)]
print("Datos originales:", datos)
start_time = time.time()
datos, intercambios = bucket_sort(datos)
end_time = time.time()
print("Datos ordenados:", datos)
print("Intercambios:", intercambios)
print("Tiempo transcurrido: {:.6f} segundos".format(end_time - start_time))
#El numero de intercambios dio 100 mas de una vez
