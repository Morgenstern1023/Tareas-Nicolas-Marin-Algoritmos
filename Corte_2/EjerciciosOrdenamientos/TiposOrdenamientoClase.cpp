#include <iostream>
#include <vector>
#include <chrono>

using namespace std;    

void bubble_sort(vector<int>& arr, int& intercambios, int& comparaciones) {
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

void selection_sort(vector<int>& arr, int& intercambios, int& comparaciones) {
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

void insertion_sort(vector<int>& arr, int& intercambios, int& comparaciones) {
    int n = arr.size();
    intercambios = 0;
    comparaciones = 0;
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && key < arr[j]) {
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

int main() {
    vector<int> datos = {64, 25, 12, 22, 11, 90, 45, 33};
    vector<int> datos_original = datos;
    int intercambios;
    int comparaciones = 0;
    auto start_time = chrono::high_resolution_clock::now();
    bubble_sort(datos, intercambios, comparaciones);
    datos = datos_original; // Reset the array before the next sort
    auto end_time = chrono::high_resolution_clock::now();
    cout << "Bubble Sort intercambios: " << intercambios << endl;
    cout << "Bubble Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    start_time = chrono::high_resolution_clock::now();
    selection_sort(datos, intercambios, comparaciones);
    datos = datos_original; // Reset the array before the next sort
    end_time = chrono::high_resolution_clock::now();
    cout << "Selection Sort intercambios: " << intercambios << endl;
    cout << "Selection Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    start_time = chrono::high_resolution_clock::now();
    insertion_sort(datos, intercambios, comparaciones);
    datos = datos_original; // Reset the array after insertion sort
    end_time = chrono::high_resolution_clock::now();
    cout << "Insertion Sort intercambios: " << intercambios << endl;
    cout << "Insertion Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    return 0;
}