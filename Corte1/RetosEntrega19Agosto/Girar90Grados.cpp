#include <iostream>
using namespace std;

int main() {
    //Se crea y se pregunta el tamaño de la matriz (filas y columnas)
    int tamanoMatrizFilas = 0;
    cout << "Ingrese cuantas filas tiene la matriz: ";
    cin >> tamanoMatrizFilas;

    int tamanoMatrizColumnas = 0;
    cout << "Ingrese cuantas columnas tiene la matriz: ";
    cin >> tamanoMatrizColumnas;

    //Se le pregunta al usuario cada valor de la matriz
    int matriz[tamanoMatrizFilas][tamanoMatrizColumnas];
    for (int i = 0; i < tamanoMatrizFilas; i++) {
        for (int j = 0; j < tamanoMatrizColumnas; j++) {
            cout << "Ingrese el valor para la posición [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }

    // Se gira cambiando filas por columnas y mostrando la matriz girada
    int matrizGirada[tamanoMatrizColumnas][tamanoMatrizFilas];
    for (int i = 0; i < tamanoMatrizFilas; i++) {
        for (int j = 0; j < tamanoMatrizColumnas; j++) {
            matrizGirada[j][tamanoMatrizFilas - 1 - i] = matriz[i][j];
        }
    }

    // Imprime la matriz girada 90 grados
    cout << "La matriz girada 90 grados es:" << endl;
    for (int i = 0; i < tamanoMatrizColumnas; i++) {
        for (int j = 0; j < tamanoMatrizFilas; j++) {
            cout << matrizGirada[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}