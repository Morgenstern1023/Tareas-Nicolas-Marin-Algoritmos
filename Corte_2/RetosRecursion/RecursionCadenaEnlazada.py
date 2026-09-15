##Funcion que recorre todos los nodos de una cadena enlazada mediante recursión.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

def recorrer_cadena_enlazada(nodo):
    if nodo is None:
        # Caso Base: si el nodo es None, se termina la recursión
        return
    # Caso Recursivo: se imprime el valor del nodo y se llama a la función con el siguiente nodo
    print(nodo.valor)
    recorrer_cadena_enlazada(nodo.siguiente)

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

recorrer_cadena_enlazada(lista.cabeza)