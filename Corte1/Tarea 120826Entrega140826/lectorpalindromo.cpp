#include <iostream>
#include <string>
using namespace std;

int main() {

    string numeroCodigo = "0";
    cout << "Este programa determina si un numero es un palindromo o no. \nIngrese un numero: ";
    cin >> numeroCodigo;
    // Se crea un array del tamaño de numeros y se rellena con los digtos usando un for
    char digitosNumero[numeroCodigo.length()];

    for (int i = 0; i < numeroCodigo.length(); i++ && numeroCodigo.length() > 0) {
        digitosNumero[i] = numeroCodigo[i];
    }

    for (int i= 0, j = numeroCodigo.length() - 1; i < j; i++, j--) {
        if (digitosNumero[i] != digitosNumero[j]) {
            cout << "El numero " << numeroCodigo << " no es un palindromo y por ende el codigo no es valido." << endl;
            return 0;
        }
    }
    cout << "El numero " << numeroCodigo << " es un palindromo y por ende el codigo es valido." << endl;
}