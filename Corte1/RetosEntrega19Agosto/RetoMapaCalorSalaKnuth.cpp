#include <iostream>
using namespace std;

int main() {
    // Se crean las variables a usar
    int usoHora = 0;
    int usoMaxHora = 0;
    int columnaMax = 0;
    int filaMax = 0;
    int usoDia = 0;
    int UsoTotalDia = 0;

    int usoHorarioSala[5][6] = {{usoHora, usoHora, usoHora, usoHora, usoHora, usoHora},
                             {usoHora, usoHora, usoHora, usoHora, usoHora, usoHora},
                             {usoHora, usoHora, usoHora, usoHora, usoHora, usoHora},
                             {usoHora, usoHora, usoHora, usoHora, usoHora, usoHora},
                             {usoHora, usoHora, usoHora, usoHora, usoHora, usoHora}};

    // Se usa un fro anidado para pedir todos los datos
    for (int i = 0; i < 5; i++) {
        cout << "Escriba los 6 datos de la sala para el dia " << i + 1 << ": ";
        for (int j = 0; j < 6; j++) {
            cin >> usoHora;
            usoHorarioSala[i][j] = usoHora;
        }
    }
    // Se usa un for anidado para recorrer la matriz y encontrar el uso máximo de la sala dia y hora incluidos
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            usoHora = usoHorarioSala[i][j];
            if (usoHora > usoMaxHora) {
                usoMaxHora = usoHora;
                filaMax = i;
                columnaMax = j;
            }
        }
    }
    cout << "El uso máximo de la sala fue de " << usoMaxHora << " en el dia " << filaMax + 1 << " y la hora " << columnaMax + 1 << endl;
    // FOr anidado que revisa  el uso total de usuarios por dia y dice el mayor
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            usoDia = usoDia + usoHorarioSala[i][j];
            if (usoDia > UsoTotalDia) {
                UsoTotalDia = usoDia;
                filaMax = i;
            }
        }
        usoDia = 0; // Reiniciar el uso diario para el siguiente día
        
    }
    cout << "El dia que mas se uso la sala fue el dia " << filaMax + 1 << " con un total de " << UsoTotalDia << " usuarios." << endl;
    // For que revisa las franjas y dias con menos de 5 usuarios
     for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) {
            if (usoHorarioSala[i][j] <= 5) {
            cout << "El dia " << i + 1 << " y la hora " << j + 1 << " tuvo menos de 5 usuarios" << endl;
            }
        }
    }
    return 0;
}