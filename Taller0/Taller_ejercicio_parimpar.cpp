#include <iostream>
#include <string>
using namespace std;

int main()
{
    int numero = 0;
 
    cout << "Escriba el numero del cual desee saber si es par o impar: ";
    cin >> numero;
 
    if (numero % 2 == 0) {
        cout << "El numero " << numero << " es par";
        }
    else {
        cout << "El numero " << numero << " es impar";
    }
}