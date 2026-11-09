// ============================================================
//  Laboratorio integrador · Corte 3 · RETO 4  (25 puntos)
//  Sesiones 41 y 43 — DFS, componentes conexas y vias criticas
//  Sistema: RedAcopio — que vias no pueden cerrarse
//
//  Este archivo NO tiene main(): el main esta en pruebas_r4.cpp
//  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r4.cpp ni red.h
//  Compile y ejecute:
//     g++ -std=c++17 -g -o pruebas_r4 conectividad.cpp pruebas_r4.cpp
//     ./pruebas_r4
// ============================================================
#include <vector>
#include <string>
#include "red.h"
using namespace std;


int cuantasComponentes(const vector<vector<int>>& g) {
   // Cuenta en cuantos pedazos esta partida la red.
   // Lance un DFS desde cada vertice que todavia no haya sido visitado;
   // cada DFS que arranca es una componente nueva.
   //
   // Use una PILA explicita (un vector<int> con push_back y pop_back),
   // no recursion.
   //
   // PENDIENTE: implementar.
   //se cuentan los nodos que se encuentran en cada componente
   int n = g.size();
   vector<bool> visitado(n, false);
   int componentes = 0;
   for (int i = 0; i < n; ++i) {
       //revisa estado
       if (!visitado[i]) {
           ++componentes;
           //inicia DFS desde el nodo i
           vector<int> pila = {i};
           while (!pila.empty()) {
               //toma el nodo de la cima de la pila
               int u = pila.back(); pila.pop_back();
               //verifica si ya fue visitado
               if (visitado[u]) continue;
               //marca el nodo como visitado
               visitado[u] = true;
               //agrega sus vecinos a la pila para que no explore un solo elemento
               for (int v : g[u]) {
                   if (!visitado[v]) pila.push_back(v);
               }
           }
       }
   }
   return componentes;
}


vector<string> viasCriticas() {
   // Una via es CRITICA si al cerrarla la red deja de estar conectada.
   // Para cada arista: arme la red SIN esa arista y cuente componentes.
   // Si pasa de 1 a mas de 1, la via es critica.
   //
   // Devuelva los nombres con el formato  "ORIGEN-DESTINO"
   // respetando el orden en que aparecen en ARISTAS.
   // Ejemplo de formato:  "ACOPIO-NORTE"
   const auto G = construir(ARISTAS);


   vector<string> criticas;
   for (const auto& arista : ARISTAS) {
       int u = arista.first;
       int v = arista.second;


       vector<vector<int>> g_sin = G;
       g_sin[u].erase(remove(g_sin[u].begin(), g_sin[u].end(), v), g_sin[u].end());
       g_sin[v].erase(remove(g_sin[v].begin(), g_sin[v].end(), u), g_sin[v].end());


       if (cuantasComponentes(g_sin) > 1) {
           criticas.push_back(NOMBRES[u] + "-" + NOMBRES[v]);
       }
   }
   return criticas;
}



