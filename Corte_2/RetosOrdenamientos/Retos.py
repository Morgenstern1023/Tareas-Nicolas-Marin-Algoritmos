#Función de bubble como ordenamiento con flag si en una pasada no intercambia
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

#Quicksort en el sitio, sin listas nuevas, indices que se cruzan
def quicksort_inplace(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

#Caso en el que se comporta pesimo, arreglo ordenado
arr_ordenado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Heapsort de maximos
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

#Heapsort de minimos

def heapify_min(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, n, smallest)

def heap_sort_min(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_min(arr, i, 0)
    return arr

#La diferencia es que se invierte el orden de los elementos, mientras que en heap maximos se coloca el mayor elemento al final, 
# en heap minimos se coloca el menor elemento al final.

