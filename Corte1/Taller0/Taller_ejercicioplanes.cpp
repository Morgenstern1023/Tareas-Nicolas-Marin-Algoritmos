#include <iostream>
#include <string>
using namespace std;

int main()
{
 string tipoPlan = "";
 float precio = 0;
 float nuevoPrecio = 0;
 cout << "Escriba el tipo de plan que posee prepago o postpago como aparece en pantalla: ";
 cin >> tipoPlan;
 cout << "Escriba el precio de lo que va a comprar: ";
 cin >> precio;
 if (tipoPlan == "prepago") {
    if (precio > 100000 && precio < 900000) {
        nuevoPrecio = precio * 0.9;
    }
    else if (precio > 1000000) {
        nuevoPrecio = precio * 0.8;
    }
 }
else if (tipoPlan == "postpago"){
    if (precio < 500000) {
        nuevoPrecio = precio * 0.85;
    }
    else if (precio > 500000 && precio < 1000000) {
        nuevoPrecio = precio * 0.80;
    }
    else if (precio > 1000000) {
        nuevoPrecio = precio * 0.75;
    }
}
cout << "El nuevo costo es: " << nuevoPrecio;
}