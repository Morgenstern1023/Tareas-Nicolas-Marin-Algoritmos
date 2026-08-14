#include <iostream>
using namespace std;

int main() {
    int datosLluvia[9] = {0, 1, 1, 0, 1, 1, 1, 0, 1};
    int rachaMaxima = 0;
    int rachaActual = 0;

    for (int i = 0; i < 9; i++) {
        if (datosLluvia[i] == 1) {
            rachaActual++;
            if (rachaActual > rachaMaxima) {
                rachaMaxima = rachaActual;
            }
        } else {
            rachaActual = 0;
        }
    }

    cout << "La racha máxima de lluvia fue de " << rachaMaxima << " días." << endl;
    return 0;
}