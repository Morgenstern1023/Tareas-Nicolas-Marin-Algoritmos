#include <iostream>
using namespace std;

// Un barrio puso en marcha una central de reciclaje. Cada punto de acopio recibe material durante la semana 
// y la junta comunal necesita un programa que registre los pesos y produzca un informe.

/*Definir una matriz de 4 puntos de acopio × 6 días con los pesos recogidos en kilogramos.
Calcular e imprimir: total por punto, total por día, el punto más productivo de la semana y el día de menor recolección de toda la central.
Informar cuántos registros tienen valor 0 (días en que el punto no operó).*/

//Función para calcular total por punto
int totalPorPunto(int matriz[4][6], int punto) {
    int total = 0;
    for (int j = 0; j < 6; j++) {
        total += matriz[punto][j];
    }
    return total;
}

// Función para calcular total por día
int totalPorDia(int matriz[4][6], int dia) {
    int total = 0;
    for (int i = 0; i < 4; i++) {
        total += matriz[i][dia];
    }
    return total;
}

//Función dia mas productivo
int diaMasProductivo(int matriz[4][6]) {
    int maxDia = 0;
    int maxTotal = totalPorDia(matriz, 0);
    for (int j = 1; j < 6; j++) {
        int total = totalPorDia(matriz, j);
        if (total > maxTotal) {
            maxTotal = total;
            maxDia = j;
        }
    }
    return maxDia;
}

//Función dia menos productivo
int diaMenosProductivo(int matriz[4][6]) {
    int minDia = 0;
    int minTotal = totalPorDia(matriz, 0);
    for (int j = 1; j < 6; j++) {
        int total = totalPorDia(matriz, j);
        if (total < minTotal) {
            minTotal = total;
            minDia = j;
        }
    }
    return minDia;
}

int main() {

 int matriz[4][6] = {};

 //Recoge los datos de la matriz
 for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 6; j++) {
        cout << "Ingrese el peso recogido en el punto de acopio " << i + 1 << " para el día " << j + 1 << ": ";
        cin >> matriz[i][j];
    }
 }
 //Se usa un for para que imprima el total por punto de acopio, usando la función totalPorPunto
 for (int i = 0; i < 4; i++) {
    cout << "Total por punto de acopio " << i + 1 << ": " << totalPorPunto(matriz, i) << endl;
 }
//Se usa un for para que imprima el total por día, usando la función totalPorDia
 for (int j = 0; j < 6; j++) {
    cout << "Total por día " << j + 1 << ": " << totalPorDia(matriz, j) << endl;
 }

 //Se imprime el dia más productivo de la semana, usando la función diaMasProductivo
 cout << "El día más productivo de la semana fue el día " << diaMasProductivo(matriz) + 1 << endl;

 //Se imprime el dia menor de recolección de toda la central, usando la función diaMenosProductivo
 cout << "El día de menor recolección de toda la central fue el día " << diaMenosProductivo(matriz) + 1 << endl;

 return 0;
}