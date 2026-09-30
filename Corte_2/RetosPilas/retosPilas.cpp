#include <iostream>
#include <cassert>
#include <memory>
#include <utility>
using namespace std;

template <class T>
class Pila {
    unique_ptr<T[]> a;
    size_t n = 0, cap = 0;
    void redimensionar(size_t c) {
        unique_ptr<T[]> b(new T[c]);
        for (size_t i = 0; i < n; i++) b[i] = move(a[i]);
        a = move(b);
        cap = c;
    }
public:
    void apilar(T x) {
        if (n == cap) redimensionar(cap ? 2 * cap : 1);
        a[n++] = move(x);
    }

    void desapilar() {
        assert(n > 0);
        --n;
        if (n < cap / 4) redimensionar(cap / 2);
    }

    T& cima() const {
        assert(n > 0);
        return a[n - 1];
    }

    bool vacia() const {
        return n == 0;
    }
    size_t tamaño() const {
        return n;
    }
};

class listaEnlazada {
    class Nodo {
    public:
        int valor;
        Nodo* siguiente;
        Nodo(int v) : valor(v), siguiente(nullptr) {}
    };
    Nodo* tope = nullptr;
public:
    void apilar(int x) {
        Nodo* nuevoNodo = new Nodo(x);
        nuevoNodo->siguiente = tope;
        tope = nuevoNodo;
    }

    void desapilar() {
        assert(tope != nullptr);
        Nodo* temp = tope;
        tope = tope->siguiente;
        delete temp;
    }

    int cima() const {
        assert(tope != nullptr);
        return tope->valor;
    }

    bool vacia() const {
        return tope == nullptr;
    }
};