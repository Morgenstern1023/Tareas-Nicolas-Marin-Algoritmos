#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

// Ejercicio BTS: insertar los valores 50,30,70,20,40,60,80 y 35
// medir cuantos hijos tiene cada nodo antes de eliminar.


/* Nodo* insertar(Nodo* n, int clave) {
    if (n == nullptr) return new Nodo(clave);
    if (clave < n->clave)      n->izq = insertar(n->izq, clave);
    else if (clave > n->clave) n->der = insertar(n->der, clave);
    return n;                        // clave repetida: no se inserta
}*/


  struct Nodo {
    int clave;
    string nombre;
    Nodo* izquierdo;
    Nodo* derecho;

    // Constructor
    Nodo(int valor) {
        clave = valor;
        nombre = "";
        izquierdo = nullptr;
        derecho = nullptr;
    }
};
       

Nodo* insertar(Nodo* n, int clave, string nombre="") {
    if (n == nullptr) return new Nodo(clave);
    if (clave < n->clave)      n->izquierdo = insertar(n->izquierdo, clave, nombre);
    else if (clave > n->clave) n->derecho = insertar(n->derecho, clave, nombre);
    return n;                        // clave repetida: no se inserta
}

Nodo* buscar(Nodo* n, int clave, vector<int>& camino) {
    if (n == nullptr) return nullptr;
    camino.push_back(n->clave);
    if (n->clave == clave) return n;
    if (clave < n->clave) return buscar(n->izquierdo, clave, camino);
    return buscar(n->derecho, clave, camino);
}

Nodo* buscar(Nodo* n, int clave) {
    vector<int> camino;
    return buscar(n, clave, camino);
}

Nodo* minimo(Nodo* n) {
    while (n->izquierdo != nullptr) n = n->izquierdo;
    return n;
}
 
Nodo* maximo(Nodo* n) {
    while (n->derecho != nullptr) n = n->derecho;
    return n;
}

Nodo* eliminar(Nodo* n, int clave) {
    if (n == nullptr) return nullptr;
    if (clave < n->clave) n->izquierdo = eliminar(n->izquierdo, clave);
    else if (clave > n->clave) n->derecho = eliminar(n->derecho, clave);
    else { // encontramos el nodo a eliminar
        if (n->izquierdo == nullptr) return n->derecho;
        if (n->derecho == nullptr) return n->izquierdo;
        Nodo* suc = minimo(n->derecho);
        n->clave = suc->clave;
        n->nombre = suc->nombre;
        n->derecho = eliminar(n->derecho, suc->clave);
    }
    return n;
}

Nodo* inorden(Nodo* n, vector<int>& s) {
    if (n == nullptr) return nullptr;
    inorden(n->izquierdo, s);
    s.push_back(n->clave);
    inorden(n->derecho, s);
    return n;
}

int altura(Nodo* n) {
    if (n == nullptr) return -1;
    int izq = altura(n->izquierdo);
    int der = altura(n->derecho);
    return 1 + (izq > der ? izq : der);
}

int hijos(Nodo* n, int clave) {
    n = buscar(n, clave);
    if (n == nullptr) return -1;
    return (n->izquierdo ? 1 : 0) + (n->derecho ? 1 : 0);
}

int main() {
    
    Nodo* raiz = nullptr;
    for (int c : {50,30,70,20,40,60,80,35}) {
        raiz = insertar(raiz, c, "");
    }
    int alturaMezclado = altura(raiz);
    vector<int> s;
    inorden(raiz, s);
    cout << "Inorden (queda ordenado):";
    for (int x : s) cout << " " << x;
    cout << endl;
    cout << "minimo = " << minimo(raiz)->clave << " maximo = " << maximo(raiz)->clave << " altura = " << altura(raiz) << endl;

    for (int objetivo : {40,65}) {
        vector<int> p;
        Nodo* r = buscar(raiz, objetivo, p);
        cout << "buscar(" << objetivo << "): camino ";
        for (size_t i = 0; i < p.size(); i++) {
            cout << p[i];
            if (i + 1 < p.size() || !r) cout << " -> ";
        }
        // Si no se encuentra, llegar al vacío cuenta como una comparación más
        int comparaciones = (int)p.size() + (r ? 0 : 1);
        if (!r) cout << "vacio";
        cout << (r ? " => ENCONTRADO" : " => NO ESTA")
             << " (" << comparaciones << " comparaciones)" << endl;
    }
    
    map<int,string> Nombre = {{0,"caso 1: hoja, 0 hijos"}, {1,"caso 2: un hijo"}, {2,"caso 3: dos hijos"}};
    
    for (int clave : {20,30,50}) {
        int k = hijos(raiz, clave);
        raiz = eliminar(raiz, clave);
        s.clear();
        inorden(raiz, s);
        cout << "eliminar(" << clave << ") [" << Nombre[k] << "] ->";
        for (int x : s) cout << " " << x;
        cout << endl;
    }
    delete raiz;
    Nodo* deg = nullptr;
    for (int c : {10,20,30,40,50,60,70,80}) {
        deg = insertar(deg, c);
    }
    cout << "\nBTS con datos ordenados: altura = " << altura(deg)
         << " con 8 nodos (una lista enlazada)" << endl;
    cout << "BTS con datos mezclados: altura = " << alturaMezclado
         << " con 8 nodos (log2(8) = 3)" << endl;

    return 0;
}

    

//NOOMBRE={0:"caso 1: hoja, 0 hijos", 1:"caso 2: un hijo", 2:"caso 3: dos hijos"}
//for clave in [20,30,50]:
//    k=hijos(raiz,clave )
//    raiz=eliminar(raiz,clave)
//    s=[];inorden(raiz,s)
//    print(f"eliminar({clave}) [{NOOMBRE[k]}] ->",s)
//deg=None
//for c in [10,20,30,40,50,60,70,80]:
//    deg=insertar(deg,c)
//print(f"\nBTS con datos ordenados: altura = {altura(deg)} con 8 nodos (una lista enlazada)")
//print(f"BTS con datos mezclados: altura = {altura(raiz)} con 8 nodos (log2(8) = 3)")



// Salida: Inorden (queda ordenado): [20, 30, 35, 40, 50, 60, 70, 80]
//minimo = 20  maximo = 80  altura = 3
//buscar(40): camino 50 -> 30 -> 40  =>  ENCONTRADO  (3 comparaciones)
//buscar(65): camino 50 -> 70 -> 60 -> vacio  =>  NO ESTA  (4 comparaciones)
//eliminar(20) [caso 1: hoja, 0 hijos] -> [30, 35, 40, 50, 60, 70, 80]
//eliminar(30) [caso 2: un hijo] -> [35, 40, 50, 60, 70, 80]
//eliminar(50) [caso 3: dos hijos] -> [35, 40, 60, 70, 80]
//BST con datos ordenados: altura = 7 con 8 nodos (una lista enlazada)
//BST con datos mezclados: altura = 3 con 8 nodos (log2(8) = 3)