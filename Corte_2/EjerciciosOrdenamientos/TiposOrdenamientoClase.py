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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        L, left_intercambios, left_comparaciones = merge_sort(L)
        R, right_intercambios, right_comparaciones = merge_sort(R)

        intercambios = left_intercambios + right_intercambios
        comparaciones = left_comparaciones + right_comparaciones

        i = j = k = 0

        while i < len(L) and j < len(R):
            comparaciones += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            intercambios += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            intercambios += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            intercambios += 1

        return arr, intercambios, comparaciones
    else:
        return arr, 0, 0

def quick_sort(arr):
    intercambios = 0
    comparaciones = 0

    def _quick_sort(arr, low, high):
        nonlocal intercambios, comparaciones
        if low < high:
            pi, pi_intercambios, pi_comparaciones = partition(arr, low, high)
            intercambios += pi_intercambios
            comparaciones += pi_comparaciones
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    def partition(arr, low, high):
        intercambios_local = 0
        comparaciones_local = 0
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparaciones_local += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                intercambios_local += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        intercambios_local += 1
        return i + 1, intercambios_local, comparaciones_local

    _quick_sort(arr, 0, len(arr) - 1)
    return arr, intercambios, comparaciones

def heap_sort(arr):
    intercambios = 0
    comparaciones = 0

    def heapify(arr, n, i):
        nonlocal intercambios, comparaciones
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n:
            comparaciones += 1
            if arr[l] > arr[largest]:
                largest = l

        if r < n:
            comparaciones += 1
            if arr[r] > arr[largest]:
                largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            intercambios += 1
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        intercambios += 1
        heapify(arr, i, 0)

    return arr, intercambios, comparaciones

def bucket_sort(arr):
    intercambios = 0
    comparaciones = 0

    if len(arr) == 0:
        return arr, intercambios, comparaciones

    bucket_count = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = (num - min_value) * (bucket_count - 1) // (max_value - min_value)
        buckets[index].append(num)
        intercambios += 1

    sorted_arr = []
    for bucket in buckets:
        bucket.sort()
        comparaciones += len(bucket) * (len(bucket) - 1) // 2
        sorted_arr.extend(bucket)

    return sorted_arr, intercambios, comparaciones

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

start_time = time.time()
print("Quick Sort:", quick_sort(datos.copy()))
print("Numero de intercambios:", quick_sort(datos.copy())[1])
print("Numero de comparaciones:", quick_sort(datos.copy())[2])
end_time = time.time()
print("Tiempo transcurrido:", end_time - start_time)

start_time = time.time()
print("Heap Sort:", heap_sort(datos.copy()))
print("Numero de intercambios:", heap_sort(datos.copy())[1])
print("Numero de comparaciones:", heap_sort(datos.copy())[2])
end_time = time.time()
print("Tiempo transcurrido:", end_time - start_time)

start_time = time.time()
print("Bucket Sort:", bucket_sort(datos.copy()))
print("Numero de intercambios:", bucket_sort(datos.copy())[1])
print("Numero de comparaciones:", bucket_sort(datos.copy())[2])
end_time = time.time()
print("Tiempo transcurrido:", end_time - start_time)

start_time = time.time()
print("Merge Sort:", merge_sort(datos.copy()))
print("Numero de intercambios:", merge_sort(datos.copy())[1])
print("Numero de comparaciones:", merge_sort(datos.copy())[2])
end_time = time.time()
print("Tiempo transcurrido:", end_time - start_time)
