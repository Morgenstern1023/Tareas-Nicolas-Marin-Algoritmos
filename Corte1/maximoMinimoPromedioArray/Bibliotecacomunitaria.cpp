#include <iostream>
using namespace std;

int main()
{
    int computador = 0;
    int videobeam = 1;
    int sala = 2;
    int usoRecurso = 0; // Se crean variables de el recurso a usar (son constantes) y que tanto se usan
    int usoRecursos[3][5] = {{usoRecurso, usoRecurso, usoRecurso, usoRecurso, usoRecurso},
                             {usoRecurso, usoRecurso, usoRecurso, usoRecurso, usoRecurso},
                             {usoRecurso, usoRecurso, usoRecurso, usoRecurso, usoRecurso}};

    for (int i = 0; i < 3; i++)
    {
        cout << "Escriba los 5 datos del computador, luego videobeam y por ultimo sala: ";
        for (int j = 0; j < 5; j++)
        {
            cin >> usoRecurso;
            usoRecursos[i][j] = usoRecurso;
        }
    }

    cout << "\t \t L \t \t M \t \t M \t \t J \t \t V \n";
    for (int i = 0; i < 3; i++)
    {
        if (i == 0)
        {
            cout << "Computador \t ";
        }
        else if (i == 1)
        {
            cout << "Videobeam \t ";
        }
        else if (i == 2)
        {
            cout << "Sala \t \t ";
        }
        for (int j = 0; j < 5; j++)
        {
            cout << usoRecursos[i][j] << "\t \t";
        }
        cout << "\n";
    }
    for (int i=0; i<3; i++){
        int datoMaximo = 0;
        for (int j=0;j<5;j++){
            int datoActual = usoRecursos[i][j];
            if (datoActual > datoMaximo) {
                datoMaximo = datoActual;
            }
        }
        if (i == 0)
        {
            cout << " Dato maximo computador: " << datoMaximo;
        }
        else if (i == 1)
        {
            cout << "Dato maximo videobeam \t " << datoMaximo;
        }
        else if (i == 2) {
            cout << "Dato maximo sala: " << datoMaximo;
        }
    }
}
