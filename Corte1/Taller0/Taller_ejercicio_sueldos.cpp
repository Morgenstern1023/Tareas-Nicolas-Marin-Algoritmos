#include <iostream>
#include <string>
using namespace std;

int main()
{
    float sueldo = 0;
    double nuevoSueldo = 0;
    cout << "Escriba su sueldo: ";
    cin >> sueldo;
    if (sueldo < 1000000) {
        nuevoSueldo = sueldo * 1.15;
    }
    else {
        nuevoSueldo = sueldo;
    }
    
    cout << "Su nuevo sueldo es: " << nuevoSueldo;
}