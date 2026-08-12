#include <iostream>
#include <random>
#include <string>
using namespace std;

int main() {
    int indiceBola = 0;
    string colores[4] = {"roja", "azul", "amarilla", "blanca"};
    float compra = 0.0;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 3);

    cout << "Por favor inserte cuanto fue el valor de su compra: ";
    cin >> compra;

    if (compra >= 50000) {
        indiceBola = dis(gen);
        cout << "Felicidades, sacaste la bola de color " << colores[indiceBola] << "\n";
        if (colores[indiceBola] == "roja") {
            cout << "Ganaste un 10% de descuento en tu compra\n";
            compra = compra * 0.9;
        }
        else if (colores[indiceBola] == "azul") {
            cout << "Ganaste un 30% de descuento en tu compra\n";
            compra = compra * 0.7;
        }
        else if (colores[indiceBola] == "amarilla") {
            cout << "Ganaste un 50% de descuento en tu compra\n";
            compra = compra * 0.5;
        }
        else if (colores[indiceBola] == "blanca") {
            cout << "Ganaste un 100% de descuento en tu compra\n";
            compra = 0;
        }
    }
    else {
        cout << "Lo siento, no puede participar en el sorteo\n";
    }

    cout << "El valor final de su compra es: " << compra << "\n";
    
}