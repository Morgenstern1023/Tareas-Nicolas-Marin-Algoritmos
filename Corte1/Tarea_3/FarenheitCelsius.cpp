#include <iostream>
using namespace std;

int main()
{

double gradosFarenheit = 0;
double gradosCelsius = 0;

cout << "Escriba los grados farenheit que quiere convertir: ";
cin >> gradosFarenheit;

gradosCelsius = (gradosFarenheit - 32)/1.8;
cout << "Son " << gradosCelsius << " grados celsius";
}