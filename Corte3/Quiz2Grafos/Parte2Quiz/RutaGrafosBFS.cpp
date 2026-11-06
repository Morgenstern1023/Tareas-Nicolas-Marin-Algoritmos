#include <algorithm>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const vector<string> NOMBRES = {
    "CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE",
    "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"
};

const vector<pair<int, int>> ARISTAS = {
    {0, 1}, {0, 2}, {0, 3}, {1, 4}, {1, 5}, {2, 7},
    {3, 6}, {5, 6}, {4, 7}, {7, 8}, {8, 1}, {7, 5},
    {5, 8}, {2, 6}, {6, 8}, {5, 2}
};

vector<vector<int>> crearListaAdyacencia() {
    vector<vector<int>> lista(NOMBRES.size());
    for (auto [u, v] : ARISTAS) {
        lista[u].push_back(v);
        lista[v].push_back(u);
    }
    return lista;
}

void bfs(int inicio, const vector<vector<int>>& lista, vector<int>& orden,
         vector<int>& dist, vector<int>& padre) {
    if (inicio < 0 || static_cast<size_t>(inicio) >= lista.size()) {
        throw out_of_range("El nodo inicial no existe en el grafo.");
    }

    vector<bool> visitado(lista.size(), false);
    dist.assign(lista.size(), -1);
    padre.assign(lista.size(), -1);
    orden.clear();

    queue<int> cola;
    cola.push(inicio);
    visitado[inicio] = true;
    dist[inicio] = 0;

    while (!cola.empty()) {
        int u = cola.front();
        cola.pop();
        orden.push_back(u);

        for (int v : lista[u]) {
            if (!visitado[v]) {
                visitado[v] = true;
                dist[v] = dist[u] + 1;
                padre[v] = u;
                cola.push(v);
            }
        }
    }
}

int main() {
    const vector<vector<int>> lista = crearListaAdyacencia();
    vector<int> orden, dist, padre;
    bfs(0, lista, orden, dist, padre);

    const int destino = 8;
    cout << "CAMINO MAS CORTO desde CENTRO hacia VEREDA:" << endl;

    if (dist[destino] == -1) {
        cout << "No existe una ruta." << endl;
        return 0;
    }

    vector<int> camino;
    for (int v = destino; v != -1; v = padre[v]) {
        camino.push_back(v);
    }
    reverse(camino.begin(), camino.end());

    for (size_t i = 0; i < camino.size(); ++i) {
        if (i > 0) {
            cout << " -> ";
        }
        cout << NOMBRES[camino[i]];
    }
    cout << " (" << dist[destino] << " tramos)" << endl;

    return 0;
}
