// ============================================================
//  Prueba corta · Segundo corte · EJERCICIO 4  (25 puntos)
//  Tema: mapas y conjuntos
//  Sistema: RedAcopio — consolidado de recoleccion por zona
//
//  Este archivo NO tiene main(): el main esta en pruebas_e4.cpp
//  NO MODIFIQUE el archivo pruebas_e4.cpp
//  Compile y ejecute:
//     g++ -std=c++17 -g -o pruebas_e4 zonas.cpp pruebas_e4.cpp
//     ./pruebas_e4
// ============================================================
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;

// Debe hacer TRES cosas:
//   1. llenar 'totales' con los kilos acumulados por zona
//   2. llenar 'repetidas' con las zonas que aparecen en MAS DE UN registro
//   3. devolver el nombre de la zona con mayor total acumulado
//
// Si 'reg' esta vacio, devuelva la cadena vacia "" y no agregue nada.
//
// PENDIENTE: implementar el cuerpo de la funcion.

string zonaMayor(const vector<pair<string,int>>& reg,
                 map<string,int>& totales,
                 set<string>& repetidas) {
                    // Función que cuenta los kilos acumulados por zona,
                    // identifica las zonas repetidas y devuelve la zona con mayor total.
    if (reg.empty()) return "";
    
    map<string,int> contador;
    for (const auto& [zona, kilos] : reg) {
        totales[zona] += kilos;
        if (contador.count(zona)) {
            contador[zona] += 1;
            if (contador[zona] == 2)
                repetidas.insert(zona);
        } else {
            contador[zona] = 1;
        }
    }
    string mayorZona;
    int mayorKilos = -1;
    for (const auto& [zona, kilos] : totales) {
        if (kilos > mayorKilos) {
            mayorKilos = kilos;
            mayorZona = zona;
        }
    }
    return mayorZona;
}

// Conviene un map y no un vector de parejas para acumular los totales por zona porque
// permite acceder y actualizar los totales de cada zona en tiempo constante, mientras
// que con un vector de parejas habría que recorrer todo el vector para encontrar la zona.

//La complejidad de un mapa ordenado es O(log n)
// La complejidad de un mapa desordenado para consultar y actualizar elementos es O(1) en promedio.
// La diferencia en complejidad se debe a que un mapa ordenado mantiene los elementos en un árbol balanceado,
// mientras que un mapa desordenado utiliza una tabla hash para acceder y actualizar elementos en tiempo constante en promedio.

