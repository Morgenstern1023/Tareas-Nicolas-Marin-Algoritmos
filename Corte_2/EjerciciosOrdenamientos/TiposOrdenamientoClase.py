import time
# En este codigo se van a escribir los distintos tipos de ordenamiento como funciones
#Tambien se va a agregar cuantos intercambios se realizan en cada ordenamiento, el tiempo que se demora y las comparaciones que hace

def bubble_sort(arr):
    n = len(arr)
    intercambios = 0
    comparaciones = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparaciones += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                intercambios += 1
        if not swapped:
            break
    return arr, intercambios, comparaciones

def selection_sort(arr):
    n = len(arr)
    intercambios = 0
    comparaciones = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            intercambios += 1
    return arr, intercambios, comparaciones

def insertion_sort(arr):
    n = len(arr)
    intercambios = 0
    comparaciones = 0
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            comparaciones += 1
            arr[j+1] = arr[j]
            j -= 1
            intercambios += 1
        if j >= 0:
            comparaciones += 1
        arr[j+1] = key
    return arr, intercambios, comparaciones

datos = [64, 25, 12, 22, 11, 90, 45, 33]

start_time = time.time()
print("Bubble Sort:", bubble_sort(datos.copy()))
print("Numero de intercambios:", bubble_sort(datos.copy())[1])
print("Numero de comparaciones:", bubble_sort(datos.copy())[2])
end_time = time.time()
print("Tiempo transcurrido:", end_time - start_time)

start_time = time.time()
print("Selection Sort:", selection_sort(datos.copy()))
print("Numero de intercambios:", selection_sort(datos.copy())[1])
print("Numero de comparaciones:", selection_sort(datos.copy())[2])
end_time = time.time()
print("Tiempo transcurrido:", end_time - start_time)

start_time = time.time()
print("Insertion Sort:", insertion_sort(datos.copy()))
print("Numero de intercambios:", insertion_sort(datos.copy())[1])
print("Numero de comparaciones:", insertion_sort(datos.copy())[2])
end_time = time.time()
print("Tiempo transcurrido:", end_time - start_time)
