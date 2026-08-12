#include <iostream>
#include <random>
using namespace std;

int main() {
    int numerosGanadores[5] = {2, 3, 7, 11, 12};
    int dado1 = 0, dado2 = 0;
    int seguirJugando = 1;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 6);
    while (seguirJugando == 1) {

        dado1 = dis(gen);
        dado2 = dis(gen);
    
        if ((dado1 + dado2) == numerosGanadores[0] || (dado1 + dado2) == numerosGanadores[1] || (dado1 + dado2) == numerosGanadores[2] || (dado1 + dado2) == numerosGanadores[3] || (dado1 + dado2) == numerosGanadores[4]) {
            cout << "Felicidades, ganaste sacaste " << dado1 + dado2 << "\n";
        }
        else {
            cout << "Lo siento, perdiste sacaste " << dado1 + dado2 << "\n";
        }
        cout << "Si desea volver a jugar presione 1 ";
        cin >> seguirJugando;
    }
}