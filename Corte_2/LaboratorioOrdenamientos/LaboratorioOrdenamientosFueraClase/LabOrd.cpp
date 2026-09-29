

#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <chrono>
using namespace std;

// Función que le pide al usuario que registre n datos y los guarda en un array que se pasa como argumento
void registrarDatos(vector<int>& arr, int n) {
    for (int i = 0; i < n; i++) {
        cout << "Ingrese el dato " << i + 1 << ": ";
        cin >> arr[i];
        
    }
}

// Función busqueda binaria recursiva, se toma de retos de busqueda binaria, se agrega cantidad de busquedas usando makepair

pair<int, int> busquedaBinariaRecursiva(vector<int>& arr, int izquierda, int derecha, int objetivo) {
    // Caso base: si el subarreglo está vacío, el elemento no esta
    if (izquierda > derecha) {
    
        return make_pair(-1, 0);
    }
    // Calcular el índice del elemento medio del subarreglo
    int medio = izquierda + (derecha - izquierda) / 2;
    int busquedas = 0;
    // Verificar si el elemento medio es el objetivo
    if (arr[medio] == objetivo) {
        busquedas++;
        return make_pair(medio, busquedas);
        // Si el elemento medio no es el objetivo, se decide en qué subarreglo continuar la búsqueda
    } else if (arr[medio] > objetivo) {
        busquedas++;
        auto result = busquedaBinariaRecursiva(arr, izquierda, medio - 1, objetivo);
        result.second += busquedas;
        return result;
    } else {
        busquedas++;
        auto result = busquedaBinariaRecursiva(arr, medio + 1, derecha, objetivo);
        result.second += busquedas;
        return result;
    }
}   

// Función busqueda secuencial
pair<int, int> busquedaSecuencial(vector<int>& arr, int n, int objetivo) {
    int busquedas = 0;
    for (int i = 0; i < n; i++) {
        busquedas++;
        if (arr[i] == objetivo) {
            return make_pair(i, busquedas);
        }
    }
    return make_pair(-1, busquedas);
}

// Función bubble, insertion y selection sort se toman de ejercicios ordenamientos

void bubbleSort(vector<int>& arr, int& intercambios, int& comparaciones) {
    int n = arr.size();
    intercambios = 0;
    comparaciones = 0;
    for (int i = 0; i < n; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++;
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
                intercambios++;
            }
        }
        if (!swapped) {
            break;
        }
    }
}

void insertionSort(vector<int>& arr, int& intercambios, int& comparaciones) {
    int n = arr.size();
    intercambios = 0;
    comparaciones = 0;
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            comparaciones++;
            arr[j + 1] = arr[j];
            j--;
            intercambios++;
        }
        if (j >= 0) {
            comparaciones++;
        }
        arr[j + 1] = key;
    }
}


void selectionSort(vector<int>& arr, int& intercambios, int& comparaciones) {
    int n = arr.size();
    intercambios = 0;
    comparaciones = 0;
    for (int i = 0; i < n; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++;
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        if (min_idx != i) {
            swap(arr[i], arr[min_idx]);
            intercambios++;
        }
    }
}

//Función Bucket sort se toma de ejercicios ordenamientos
void bucket_sort(vector<int>& arr, int& intercambios, int& comparaciones) {
    int n = arr.size();
    if (n <= 0)
        return;

    int max_val = *max_element(arr.begin(), arr.end());
    int bucket_count = max_val / 10 + 1;
    vector<vector<int>> buckets(bucket_count);

    for (int i = 0; i < n; i++) {
        int idx = arr[i] / 10;
        buckets[idx].push_back(arr[i]);
        intercambios++;
    }

    arr.clear();
    for (int i = 0; i < bucket_count; i++) {
        sort(buckets[i].begin(), buckets[i].end());
        for (int j = 0; j < buckets[i].size(); j++) {
            arr.push_back(buckets[i][j]);
            comparaciones++;
        }
        intercambios++;
    }
}

// En el main se hace lo mismo que en el .py de comparaciones

int main() {
    //Comparación de busqueda binaria y busqueda secuencial dando tiempos y cantidad de busquedas
    //Se le pide al usuario que ingrese el tamaño del arreglo y los elementos a buscar usando la función registrarDatos

    int n;

    cout << "Ingrese el tamaño del arreglo: ";
    cin >> n;
    vector<int> arr(n);
    registrarDatos(arr, n);
    int objetivo;
    cout << "Ingrese el elemento a buscar: ";
    cin >> objetivo;
    auto tiempoInicio = chrono::high_resolution_clock::now();
    busquedaSecuencial(arr, n, objetivo);
    auto tiempoFin = chrono::high_resolution_clock::now();
    auto duracion = chrono::duration_cast<chrono::microseconds>(tiempoFin - tiempoInicio).count();
    cout << "Tiempo de busqueda secuencial: " << duracion << " microsegundos" << endl;

    tiempoInicio = chrono::high_resolution_clock::now();
    busquedaBinariaRecursiva(arr, 0, n-1, objetivo);
    tiempoFin = chrono::high_resolution_clock::now();
    duracion = chrono::duration_cast<chrono::microseconds>(tiempoFin - tiempoInicio).count();
    cout << "Tiempo de busqueda binaria: " << duracion << " microsegundos" << endl;

    // Nuevo array que se le pide al usuario para comparar ordenamientos
    int m;
    cout << "Ingrese el tamaño del nuevo arreglo: ";
    cin >> m;
    vector<int> arr2(m);
    registrarDatos(arr2, m);

    int intercambios, comparaciones;
    
    //Se guarda un arreglo original para poder reutilizarlo en cada ordenamiento y se aprovecha a medir tiempos en  los dos ultimos para reducir codigo
    vector<int> arrOriginal = arr2;

    cout << "Ordenando con Selection Sort..." << endl;
    arr2 = arrOriginal;
    selectionSort(arr2, intercambios, comparaciones);
    cout << "Intercambios: " << intercambios << ", Comparaciones: " << comparaciones << endl;

    cout << "Ordenando con Insertion Sort..." << endl;
    arr2 = arrOriginal;
    insertionSort(arr2, intercambios, comparaciones);
    cout << "Intercambios: " << intercambios << ", Comparaciones: " << comparaciones << endl;

    cout << "Ordenando con Bubble Sort..." << endl;
    arr2 = arrOriginal;
    auto tiempoInicio = chrono::high_resolution_clock::now();
    bubbleSort(arr2, intercambios, comparaciones);
    auto tiempoFin = chrono::high_resolution_clock::now();
    auto duracion = chrono::duration_cast<chrono::microseconds>(tiempoFin - tiempoInicio).count();
    cout << "Intercambios: " << intercambios << ", Comparaciones: " << comparaciones << endl;
    cout << "Tiempo de Bubble Sort: " << duracion << " microsegundos" << endl;

    cout << "Ordenando con Bucket Sort..." << endl;
    arr2 = arrOriginal;
    arr2 = arrOriginal;
    auto tiempoInicio = chrono::high_resolution_clock::now();
    bucket_sort(arr2, intercambios, comparaciones);
    auto tiempoFin = chrono::high_resolution_clock::now();
    auto duracion = chrono::duration_cast<chrono::microseconds>(tiempoFin - tiempoInicio).count();
    cout << "Intercambios: " << intercambios << ", Comparaciones: " << comparaciones << endl;
    cout << "Tiempo de Bucket Sort: " << duracion << " microsegundos" << endl;

}
