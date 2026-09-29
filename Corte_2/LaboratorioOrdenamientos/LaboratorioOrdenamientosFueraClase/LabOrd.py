import time

""""
Parte A

1. Insertion sort es el que hace menos trabajo en un conjunto de datos ya ordenados debido a que es el 
que hace menos comparaciones respecto a bubble sort y selection sort

2. Conjunto de datos en el que quicksort se comporta pesimo con el primer elemento como pivote
un arreglo que ya este ordenado, se usa ejemplo de retos
arrayOrdenado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

3. Ordenar y luego Binario debido a que se tardaria 100 veces logaritmo natural de los datos mas el ordenamiento
mientras que una busqueda secuencial se tardaria 100 veces el numero de datos

"""

"""
Parte B, se va a hacer la función de registrar los datos y luego se van a utilizar unos registros que 
tengan 100 datos y se va a hacer la busqueda secuencial y binaria
"""
#Función que le pida al usuario que ingrese los datos
def registros():
    registros = []
    cantidadDatos = int(input("Ingrese la cantidad de datos: "))
    print("Ingrese los datos de los registros:")
    for i in range(cantidadDatos):
        dato = input(f"Ingrese el dato {i+1}: ")
        registros.append(dato)
    return registros

registros = registros()

def binaria(v,x):
    inicio = time.perf_counter()
    cantidadPasos = 0
    izq=0
    der=len(v)-1
    while izq<=der:
        medio=(izq+der)//2
        if v[medio]==x:
            fin = time.perf_counter()
            cantidadPasos += 1
            print(f"Cantidad de pasos: {cantidadPasos}")
            print(f"Tiempo de ejecución: {fin - inicio} segundos")
            return medio
        elif v[medio]<x:
            izq=medio+1
            cantidadPasos += 1
        else:
            der=medio-1
            cantidadPasos += 1
    fin = time.perf_counter()
    print(f"Cantidad de pasos: {cantidadPasos}")
    print(f"Tiempo de ejecución: {fin - inicio} segundos")

    return -1
#A[0,n-1] xEA, si no lo hace devuelve -1

def secuencial(v,x):
    inicio = time.perf_counter()
    cantidadPasos = 0
    for i in range(len(v)):
        cantidadPasos += 1
        if v[i]==x:
            fin = time.perf_counter()
            print(f"Cantidad de pasos: {cantidadPasos}")
            print(f"Tiempo de ejecución: {fin - inicio} segundos")
            return i
    fin = time.perf_counter()
    print(f"Cantidad de pasos: {cantidadPasos}")
    print(f"Tiempo de ejecución: {fin - inicio} segundos")
    return -1

# Uso con primer dato

print("Busqueda binaria del primer dato:")
binaria(sorted(registros), registros[0])
print("Busqueda secuencial del primer dato:")
secuencial(registros, registros[0])

# Uso con dato del medio
print("Busqueda binaria del dato del medio:")
binaria(sorted(registros), registros[len(registros)//2])
print("Busqueda secuencial del dato del medio:")
secuencial(registros, registros[len(registros)//2])

# Uso con último dato
print("Busqueda binaria del último dato:")
binaria(sorted(registros), registros[-1])
print("Busqueda secuencial del último dato:")
secuencial(registros, registros[-1])

# Uso con dato que no existe
print("Busqueda binaria de un dato que no existe:")
binaria(sorted(registros), "dato_que_no_existe")
print("Busqueda secuencial de un dato que no existe:")
secuencial(registros, "dato_que_no_existe")

"""
Parte C 
Se implementan bubble sort, insertion sort y selection sort de actividades previas y se
compara su comportamiento con datos ordenados y desordenados, se usa la función registros() para generar los datos.
"""

def registrarArray():
    registrarArray = []
    cantidadDatos = int(input("Ingrese la cantidad de datos: "))
    print("Ingrese los datos de los registros:")
    for i in range(cantidadDatos):
        dato = input(f"Ingrese el dato {i+1}: ")
        registrarArray.append(dato)
    return registrarArray

arrayOrdenado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arrayDesordenado = [5, 2, 9, 1, 5, 6, 7, 3, 8, 4]


def bubbleSort(arr):
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

def selectionSort(arr):
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

def insertionSort(arr):
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

# Pruebas con array ordenado

registrosOrdenados = registrarArray()

print("Bubble sort con array ordenado:")
print(bubbleSort(registrosOrdenados.copy()))
print("Selection sort con array ordenado:")
print(selectionSort(registrosOrdenados.copy()))
print("Insertion sort con array ordenado:")
print(insertionSort(registrosOrdenados.copy()))

registrosDesordenados = registrarArray()
# Pruebas con array desordenado
print("Bubble sort con array desordenado:")
print(bubbleSort(registrosDesordenados.copy()))
print("Selection sort con array desordenado:")
print(selectionSort(registrosDesordenados.copy()))
print("Insertion sort con array desordenado:")
print(insertionSort(registrosDesordenados.copy()))


"""

Parte D

Comparación Bubble contra Bucket Sort con tres diferentes tamaños de entrada

"""

def bucketSort(arr):
    if len(arr) == 0:
        return arr, 0, 0
    min_value = min(arr)
    max_value = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = (num - min_value) * (bucket_count - 1) // (max_value - min_value)
        buckets[index].append(num)
    sorted_array = []
    intercambios = 0
    comparaciones = 0
    for bucket in buckets:
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and key < bucket[j]:
                comparaciones += 1
                bucket[j + 1] = bucket[j]
                j -= 1
                intercambios += 1
            if j >= 0:
                comparaciones += 1
            bucket[j + 1] = key
        sorted_array.extend(bucket)
    return sorted_array, intercambios, comparaciones


#Ejemplo a usar con 20 40 60 datos

#array de 20 datos al azar

array1 = [34, 7, 23, 32, 5, 62, 32, 7, 4, 12, 45, 67, 89, 21, 43, 56, 78, 90, 11, 3]

#array 40 datos al azar

array2 = [34, 7, 23, 32, 5, 62, 32, 7, 4, 12, 45, 67, 89, 21, 43, 56, 78, 90, 11, 3,
          25, 36, 47, 58, 69, 70, 81, 92, 13, 24, 35, 46, 57, 68, 79, 80, 91, 12, 23, 34]

#array 60 datos al azar

array3 = [34, 7, 23, 32, 5, 62, 32, 7, 4, 12, 45, 67, 89, 21, 43, 56, 78, 90, 11, 3,
          25, 36, 47, 58, 69, 70, 81, 92, 13, 24, 35, 46, 57, 68, 79, 80, 91, 12, 23, 34,
          14, 26, 37, 48, 59, 60, 71, 82, 93, 15, 27, 38, 49, 61, 72, 83, 94, 16, 28, 39]

# Se le solicita al usuario que ingrese los datos para los arrays de prueba
n = int(input(f"Ingrese la cantidad de datos para el array 1: "))
for i in range(n):
    array1[i] = int(input(f"Ingrese el dato {i+1} para el array de {n} datos: "))

n = int(input(f"Ingrese la cantidad de datos para el array 2: "))
for i in range(n):
    array2[i] = int(input(f"Ingrese el dato {i+1} para el array de {n} datos: "))
    
n = int(input(f"Ingrese la cantidad de datos para el array 3: "))
for i in range(n):
    array3[i] = int(input(f"Ingrese el dato {i+1} para el array de {n} datos: "))


print("Bubble sort con tamaño 1:")
tiempo_inicial = time.time()
print(bubbleSort(array1.copy()))
print("Tiempo bubble sort tamaño 1:", time.time() - tiempo_inicial)
print("Bucket sort con tamaño 1:")
tiempo_inicial = time.time()
print(bucketSort(array1.copy()))
print("Tiempo bucket sort tamaño 1:", time.time() - tiempo_inicial)

print("Bubble sort con tamaño 2:")
tiempo_inicial = time.time()
print(bubbleSort(array2.copy()))
print("Tiempo bubble sort tamaño 2:", time.time() - tiempo_inicial)
print("Bucket sort con tamaño 2:")
tiempo_inicial = time.time()
print(bucketSort(array2.copy()))
print("Tiempo bucket sort tamaño 2:", time.time() - tiempo_inicial)

print("Bubble sort con tamaño 3:")
tiempo_inicial = time.time()
print(bubbleSort(array3.copy()))
print("Tiempo bubble sort tamaño 3:", time.time() - tiempo_inicial)
print("Bucket sort con tamaño 3:")
tiempo_inicial = time.time()
print(bucketSort(array3.copy()))
print("Tiempo bucket sort tamaño 3:", time.time() - tiempo_inicial)

