#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main(){

double numero1 = 0.0;
double numero2 = 0.0;
double resultado = 0.0;
string operacion = "";

cout << "Escriba que operación quiere hacer, por favor escribala como aparece en pantalla: suma, resta, multiplicacion, division, potencia, raiz: \n";
cin >> operacion;
cout << "Escriba el primer numero: ";
cin >> numero1;
cout << "escriba el segundo numero: ";
cin >> numero2;

if (operacion == "suma") {
    resultado = numero1 + numero2;
}
else if (operacion == "resta") {
    resultado = numero1 - numero2;
}
else if (operacion == "multiplicacion") {
    resultado = numero1 * numero2;
}
else if (operacion == "division") {
    resultado = numero1 / numero2;
}
else if (operacion == "potencia") {
    resultado = pow(numero1,numero2);
}
else if (operacion == "raiz") {
    resultado = pow(numero1, 1.0/numero2);
}
else {
    cout << "Input invalido.";
    return 0;
}

cout << "El resultado de la operación es: " << resultado;
}




