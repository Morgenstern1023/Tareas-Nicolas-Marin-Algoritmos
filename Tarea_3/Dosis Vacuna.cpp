#include <iostream>
using namespace std;

int main()
{

int mesesBebe = 0;
double pesoBebe = 0;
double dosisVacuna = 0;

cout << "Este programa dice la dosis de vacuna que se debe asignar por favor escriba el peso del peso del bebe: ";
cin >> pesoBebe;
cout << "Ahora escriba los meses del bebe: ";
cin >> mesesBebe;

dosisVacuna = (8*(pesoBebe + 10))/(mesesBebe * 10);
cout << "Se debe aplicar la siguiente dosis: " << dosisVacuna;

}