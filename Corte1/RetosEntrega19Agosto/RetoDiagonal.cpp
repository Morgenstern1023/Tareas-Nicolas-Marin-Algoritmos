#include <iostream>
using namespace std;

int main() {
    int tamanoMatriz = 0;
    int sumaDiagonalPrincipal = 0;
    int sumaDiagonalSecundaria = 0;
    int valorMatriz = 0;
    cout << "Ingrese el tamaño de la matriz: ";
    cin >> tamanoMatriz;

    int matriz[tamanoMatriz][tamanoMatriz];

    for (int i = 0; i < tamanoMatriz; i++) {
        for (int j = 0; j < tamanoMatriz; j++) {
            cout << "Ingrese el valor para la posición [" << i << "][" << j << "]: ";
            cin >> valorMatriz;
            matriz[i][j] = valorMatriz;
        }
    }

    for (int i = 0; i < tamanoMatriz; i++) {
        sumaDiagonalPrincipal += matriz[i][i];
        sumaDiagonalSecundaria += matriz[i][tamanoMatriz - 1 - i];
    }
    if (sumaDiagonalPrincipal == sumaDiagonalSecundaria) {
        cout << "La suma de la diagonal principal es igual a la suma de la diagonal secundaria." << endl;
    } else {
        cout << "La suma de la diagonal principal no es igual a la suma de la diagonal secundaria." << endl;
    }
    cout << "Suma de la diagonal principal: " << sumaDiagonalPrincipal << endl;
    cout << "Suma de la diagonal secundaria: " << sumaDiagonalSecundaria << endl;
    return 0;
}

