//Este codigo implementa la busqueda binaria de manera recursiva en C++

#include <iostream>
#include <array>
using namespace std;

//Funcion de busqueda binaria recursiva
int busquedaBinariaRecursiva(int arr[], int izquierda, int derecha, int objetivo) {
    // Caso base: si el subarreglo está vacío, el elemento no esta
    if (izquierda > derecha) {
        return -1;
    }
    // Calcular el índice del elemento medio del subarreglo
    int medio = izquierda + (derecha - izquierda) / 2;
    // Verificar si el elemento medio es el objetivo
    if (arr[medio] == objetivo) {
        return medio;
        // Si el elemento medio no es el objetivo, se decide en qué subarreglo continuar la búsqueda
    } else if (arr[medio] > objetivo) {
        return busquedaBinariaRecursiva(arr, izquierda, medio - 1, objetivo);
    } else {
        return busquedaBinariaRecursiva(arr, medio + 1, derecha, objetivo);
    }
}

// Función para que si un elemento no esta se diga en que indice deberia ir
int busquedaBinariaConInsercion(int arr[], int izquierda, int derecha, int objetivo) {
    int resultado = busquedaBinariaRecursiva(arr, izquierda, derecha, objetivo);
    if (resultado != -1) {
        return resultado;
    } else {
        // Si no se encuentra, se determina el índice donde debería insertarse
        int medio;
        while (izquierda <= derecha) {
            medio = izquierda + (derecha - izquierda) / 2;
            if (arr[medio] < objetivo) {
                izquierda = medio + 1;
            } else {
                derecha = medio - 1;
            }
        }
        return izquierda;
    }
}

//Función para que si hay dos elementos iguales, se devuelva el índice del primero
int busquedaBinariaPrimerElemento(int arr[], int izquierda, int derecha, int objetivo) {
    int resultado = busquedaBinariaRecursiva(arr, izquierda, derecha, objetivo);
    if (resultado == -1) {
        return -1;
    }
    // Retroceder hasta encontrar el primer elemento igual al objetivo
    while (resultado > 0 && arr[resultado - 1] == objetivo) {
        resultado--;
    }
    return resultado;
}
int main() {
    // Se pregunta los datos del arreglo al usuario
    int izquierda = 0;
    int n;
    cout << "Ingrese el tamaño del arreglo: ";
    cin >> n;
    int arr[n];
    cout << "Ingrese los elementos del arreglo: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int derecha = n - 1;

    int objetivo;
    cout << "Ingrese el objetivo a buscar: ";
    cin >> objetivo;

    int resultado = busquedaBinariaConInsercion(arr, izquierda, derecha, objetivo);
    if (resultado != -1 && resultado < n && arr[resultado] == objetivo) {
        cout << "Elemento encontrado en el índice: " << resultado << endl;
    } else {
        cout << "Elemento no encontrado. Debería insertarse en el índice: " << resultado << endl;
    }
    // Buscar el primer elemento si hay duplicados
    int primerElemento = busquedaBinariaPrimerElemento(arr, izquierda, derecha, objetivo);
    if (primerElemento != -1 && primerElemento < n && arr[primerElemento] == objetivo) {
        cout << "Primer elemento encontrado en el índice: " << primerElemento << endl;
    }

    return 0;
}

