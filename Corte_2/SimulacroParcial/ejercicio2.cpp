#include <iostream> 
#include <vector> 
using namespace std; 

// Función que cuenta cuántos elementos del vector v son mayores o iguales al umbral
// v: vector de enteros
// n: índice actual
// umbral: valor de referencia
// Devuelve el número de elementos mayores o iguales al umbral hasta el índice n
int contar(const vector<int>& v, int n, int umbral) { 
 if (n < 0) return 0; // (1) 
 if (v[n] >= umbral) // (2) 
    return 1 + contar(v, n - 1, umbral); 
 return contar(v, n - 1, umbral); 
}

int main() {
    vector<int> v = {12, 45, 7, 38, 60, 19, 23};
    int umbral = 20;
    cout << "Número de elementos mayores o iguales al umbral: " << contar(v, v.size() - 1, umbral) << endl;
    return 0;
}
