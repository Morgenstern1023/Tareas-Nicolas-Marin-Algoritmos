#include <iostream>
using namespace std;

int main(){
    int lecturas[6] = {20, -999, 22, 24, -999, 26};
    int cantidadDatos = 6;
    int contadorDatos = 1;
    int sumaDatos = lecturas[0];
    int contadorMentiras = 0;

    for (int i=1; i<cantidadDatos; i++){
        if (lecturas[i] != -999){
            sumaDatos += lecturas[i];
            contadorDatos++;
        } else {
            contadorMentiras++;
        }
    }
    cout << "El promedio de las lecturas es: " << sumaDatos/contadorDatos << endl;
    cout << "Los datos falsos son: " << contadorMentiras << endl;
    return 0;
}