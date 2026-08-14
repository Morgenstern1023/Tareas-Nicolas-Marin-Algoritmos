#include <iostream>
using namespace std;

int main() {
    int cantidadLecturas = 0;
    int i = 0;
    int inputdato = 0;
    int contadorDatos = 0;
    int sumaDatos = 0;
    int contadorMentiras = 0;
    cout << "Ingrese la cantidad de lecturas que desea ingresar: ";
    cin >> cantidadLecturas;

    int lecturas [cantidadLecturas] = {};

    while (i < cantidadLecturas) {
        cout << "Ingrese el dato " << i + 1 << ": ";
        cin >> inputdato;
        lecturas[i] = inputdato;
        i++;
    }
        for (int k = 0; k<cantidadLecturas; k++){
        if (lecturas[k] != -999){
            sumaDatos += lecturas[k];
            contadorDatos++;
        } else {
            contadorMentiras++;
        }
    }
    if (contadorDatos > 0) {
        cout << "El promedio de las lecturas es: " << sumaDatos/contadorDatos << endl;
    }
    cout << "Los datos falsos son: " << contadorMentiras << endl;
    return 0;
}