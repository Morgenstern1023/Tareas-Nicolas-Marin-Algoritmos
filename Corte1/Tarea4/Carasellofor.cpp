#include <iostream>
#include <random>
#include <string>
using namespace std;

int main()
{
    int numeroAleatorio = 0;
    string eleccionMaquina = "";
    string eleccionJugador = "";
    
    
    for (int i = 0; i < 3; i++) {
    
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(1, 100);
    
    numeroAleatorio = distrib(gen);
    if (numeroAleatorio <= 50) {
        eleccionMaquina = "Sello";
    }
    else {
        eleccionMaquina = "Cara";
    }
    cout << "Escriba si cree que va a salir cara o sello con mayuscula inicial: ";
    cin >> eleccionJugador;
    
    if (eleccionMaquina == eleccionJugador) {
        cout << "Ganaste era " << eleccionMaquina << "\n";
    }
    else {
        cout << "Perdiste era " << eleccionMaquina << "\n";
    }
    }
}