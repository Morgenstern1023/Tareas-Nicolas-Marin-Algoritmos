#include <iostream>
#include <random>
#include <string>
using namespace std;

int main()
{
    int numeroAleatorio = 0;
    string eleccionMaquina = "";
    string eleccionJugador = "";
    
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(1, 2);
    
    numeroAleatorio = distrib(gen);
    if (numeroAleatorio == 1) {
        eleccionMaquina = "Sello";
    }
    else {
        eleccionMaquina = "Cara";
    }
    cout << "Escriba si cree que va a salir cara o sello con mayuscula inicial: ";
    cin >> eleccionJugador;
    
    if (eleccionMaquina == eleccionJugador) {
        cout << "Ganaste era " << eleccionMaquina;
    }
    else {
        cout << "Perdiste era " << eleccionMaquina;
    }
}
