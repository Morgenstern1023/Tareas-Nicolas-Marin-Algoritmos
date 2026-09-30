
class listaEnlazada:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None

    def __init__(self):
        self.tope = None

    def apilar(self, x):
        nuevoNodo = self.Nodo(x)
        nuevoNodo.siguiente = self.tope
        self.tope = nuevoNodo

    def desapilar(self):
        if self.tope is None:
            return None
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        return valor

    def cima(self):
        if self.tope is None:
            return None
        return self.tope.valor

    def vacia(self):
        return self.tope is None

"""
Una pila monotonica es una pila en la cual todos los elementos están en orden creciente o decreciente.
Para mantener este orden siempre que se quiera agregar un nuevo elemento se debe desapilar todos los elementos que rompan el orden
Se usan para reducir la complejidad cuando se necesitan buscar de forma eficiente un elemento anterior o siguiente mayor o menor a cada numero
complejidad de O(n) en el peor de los casos
"""

#Evaluación de expresiones en notación polaca inversa

def evaluar_expresion_polaca_inversa(expresion):
    pila = listaEnlazada()
    for digito in expresion.split():
        if digito.isdigit():
            pila.apilar(int(digito))
        else:
            b = pila.desapilar()
            a = pila.desapilar()
            if digito == '+':
                pila.apilar(f"{a} + {b}")
            elif digito == '-':
                pila.apilar(f"{a} - {b}")
            elif digito == '*':
                pila.apilar(f"{a} * {b}")
            elif digito == '/':
                pila.apilar(f"{a} / {b}")
    return pila.desapilar()

print(evaluar_expresion_polaca_inversa("3 4 +"))
    