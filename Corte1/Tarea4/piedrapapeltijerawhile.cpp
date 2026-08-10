#include <iostream>
#include <random>
#include <string>
using namespace std;

int main()
{
    string eleccionJugador = "";
    string eleccionMaquina = "";
    int numeroAleatorio = 0;
    string seguirJugando = "Si";
    
    
    while (seguirJugando == "Si") {
        
    random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> distrib(1, 99);

    cout << "Este programa sirve para jugar piedra papel o tijera, por favor elige y escribelo en lowercase: ";
    cin >> eleccionJugador;
    numeroAleatorio = distrib(gen);
    
    if (eleccionJugador == "piedra") {
        if (numeroAleatorio <= 33) {
            cout << "Empatamos";
            eleccionMaquina = "piedra";
        }
        else if (numeroAleatorio <= 66) {
            cout << "Perdiste";
            eleccionMaquina = "papel";
        }
        else {
            cout << "Ganaste";
            eleccionMaquina = "tijera";
        }
    }
    
    else if (eleccionJugador == "papel") {
        if (numeroAleatorio <= 33) {
            cout << "Ganaste";
            eleccionMaquina = "piedra";
        }
        else if (numeroAleatorio <= 66) {
            cout << "Empatamos";
            eleccionMaquina = "papel";
        }
        else {
            cout << "Perdiste";
            eleccionMaquina = "tijera";
        }
    }
    else if (eleccionJugador == "tijera") {
        if (numeroAleatorio <= 33) {
            cout << "Perdiste";
            eleccionMaquina = "piedra";
        }
        else if (numeroAleatorio <= 66) {
            cout << "Ganaste";
            eleccionMaquina = "papel";
        }
        else {
            cout << "Empatamos";
            eleccionMaquina = "tijera";
        }
    }
    else {
        cout << "Imput invalido";
    }
    cout << "\n Usuario: " << eleccionJugador;
    cout << "\n Maquina: " << eleccionMaquina << "\n";
    cout << "Si quiere seguir jugando escriba Si de la manera que observa: ";
    cin >> seguirJugando;
    }
}