#include <iostream>
#include <string>
using namespace std;

int main()
{
    float distancia = 0;
    float velocidad1 = 0;
    float velocidad2 = 0;
    float tiempo = 0;
    
    cout << "Escriba la distancia entre ciudades: ";
    cin >> distancia;
    cout << "Escriba las velocidades de los carros: ";
    cin >> velocidad1;
    cin >> velocidad2;
    
    tiempo = distancia/ (velocidad1 + velocidad2);
    
    cout << "los carros se encuentran en " << tiempo << " horas";
}