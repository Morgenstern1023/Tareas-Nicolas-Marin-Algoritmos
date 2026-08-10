#include <iostream>
#include <string>
using namespace std;

int main()
{
    int horasTrabajo = 0;
    double sueldo = 0;
    
    cout << "Escriba las horas trabajadas: ";
    cin >> horasTrabajo;
    
    if (horasTrabajo <= 35 ) {
        sueldo = horasTrabajo * 40000;
    }
    
    else {
        sueldo = (35 * 40000) + ((horasTrabajo - 35) * 5000);
    }
    cout << "Este es su sueldo: " << sueldo;
}