#include <iostream>
#include <vector>
#include <algorithm>
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
void merge_sort(vector<int>& arr, int left, int right, int& intercambios, int& comparaciones) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort(arr, left, mid, intercambios, comparaciones);
        merge_sort(arr, mid + 1, right, intercambios, comparaciones);

        int n1 = mid - left + 1;
        int n2 = right - mid;
        vector<int> L(n1);
        vector<int> R(n2);
        for (int i = 0; i < n1; i++)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; j++)
            R[j] = arr[mid + 1 + j];

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            comparaciones++;
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            intercambios++;
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
            intercambios++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
            intercambios++;
        }
    }
}

void quick_sort(vector<int>& arr, int low, int high, int& intercambios, int& comparaciones) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            comparaciones++;
            if (arr[j] <= pivot) {
                i++;
                swap(arr[i], arr[j]);
                intercambios++;
            }
        }
        swap(arr[i + 1], arr[high]);
        intercambios++;
        int pi = i + 1;
        quick_sort(arr, low, pi - 1, intercambios, comparaciones);
        quick_sort(arr, pi + 1, high, intercambios, comparaciones);
    }
}

void heapify(vector<int>& arr, int n, int i, int& intercambios, int& comparaciones) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    if (largest != i) {
        swap(arr[i], arr[largest]);
        intercambios++;
        heapify(arr, n, largest, intercambios, comparaciones);
    }
}

void heap_sort(vector<int>& arr, int& intercambios, int& comparaciones) {
    int n = arr.size();
    intercambios = 0;
    comparaciones = 0;
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i, intercambios, comparaciones);
    }
    for (int i = n - 1; i > 0; i--) {
        swap(arr[i], arr[0]);
        intercambios++;
        heapify(arr, i, 0, intercambios, comparaciones);
    }
}

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
            intercambios++;
        }
    }
}   

int main() {
    vector<int> datos = {64, 25, 12, 22, 11, 90, 45, 33};
    vector<int> datos_original = datos;
    int intercambios = 0;
    int comparaciones = 0;
    auto start_time = chrono::high_resolution_clock::now();
    bubble_sort(datos, intercambios, comparaciones);
    datos = datos_original; // Reset the array before the next sort
    auto end_time = chrono::high_resolution_clock::now();
    cout << "Bubble Sort intercambios: " << intercambios << endl;
    cout << "Bubble Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    start_time = chrono::high_resolution_clock::now();
    intercambios = 0;
    comparaciones = 0;
    selection_sort(datos, intercambios, comparaciones);
    datos = datos_original; // Reset the array before the next sort
    end_time = chrono::high_resolution_clock::now();
    cout << "Selection Sort intercambios: " << intercambios << endl;
    cout << "Selection Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    start_time = chrono::high_resolution_clock::now();
    intercambios = 0;
    comparaciones = 0;
    insertion_sort(datos, intercambios, comparaciones);
    datos = datos_original; // Reset the array after insertion sort
    end_time = chrono::high_resolution_clock::now();
    cout << "Insertion Sort intercambios: " << intercambios << endl;
    cout << "Insertion Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    start_time = chrono::high_resolution_clock::now();
    intercambios = 0;
    comparaciones = 0;
    merge_sort(datos, 0, datos.size() - 1, intercambios, comparaciones);
    datos = datos_original; // Reset the array before the next sort
    end_time = chrono::high_resolution_clock::now();
    cout << "Merge Sort intercambios: " << intercambios << endl;
    cout << "Merge Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    start_time = chrono::high_resolution_clock::now();
    intercambios = 0;
    comparaciones = 0;
    quick_sort(datos, 0, datos.size() - 1, intercambios, comparaciones);
    datos = datos_original; // Reset the array before the next sort
    end_time = chrono::high_resolution_clock::now();
    cout << "Quick Sort intercambios: " << intercambios << endl;
    cout << "Quick Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    start_time = chrono::high_resolution_clock::now();
    intercambios = 0;
    comparaciones = 0;
    heap_sort(datos, intercambios, comparaciones);
    datos = datos_original; // Reset the array before the next sort
    end_time = chrono::high_resolution_clock::now();
    cout << "Heap Sort intercambios: " << intercambios << endl;
    cout << "Heap Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;

    start_time = chrono::high_resolution_clock::now();
    intercambios = 0;
    comparaciones = 0;
    bucket_sort(datos, intercambios, comparaciones);
    datos = datos_original; // Reset the array before the next sort
    end_time = chrono::high_resolution_clock::now();
    cout << "Bucket Sort intercambios: " << intercambios << endl;
    cout << "Bucket Sort comparaciones: " << comparaciones << endl;
    cout << "Tiempo transcurrido: " << chrono::duration<double>(end_time - start_time).count() << " segundos" << endl;
    return 0;
}