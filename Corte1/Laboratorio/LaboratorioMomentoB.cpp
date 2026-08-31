#include <iostream>
using namespace std;

int main () {
    int puntosAcopioNuevos = 0;
    cout << "Ingrese la cantidad de puntos de acopio nuevos: ";
    cin >> puntosAcopioNuevos;

    if (puntosAcopioNuevos <= 0) {
        cout << "La cantidad de puntos de acopio debe ser mayor a cero." << endl;
        return 1; // Salir del programa con un código de error
    }
    // Guardar los pesos de los puntos de acopio en un arreglo dinámico (En double para calcular luego promedio)
    double* pesos = new double[puntosAcopioNuevos]; // Arreglo dinámico de double
    for (int i = 0; i < puntosAcopioNuevos; i++) {
        cout << "Ingrese el peso del punto de acopio " << (i + 1) << ": ";
        cin >> pesos[i];
    }

    //Calcular promedio usando aritmetica de punteros
    double suma = 0;
    for (double* p = pesos; p < pesos + puntosAcopioNuevos; p++) {
        suma += *p; // Acceder al valor usando aritmética de punteros
    }

    double promedio = suma / puntosAcopioNuevos;
    cout << "El promedio de los pesos es: " << promedio << endl;
    // Liberar memoria dinámica
    delete[] pesos;

    pesos = nullptr; // Evitar puntero colgante
    return 0;
}