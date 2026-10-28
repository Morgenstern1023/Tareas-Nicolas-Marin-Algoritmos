"""
Retos Arboles

Escriba una función imprimirJerarquia(nodo, nivel) que recorra el árbol en preorden e 
imprima cada nombre con dos espacios de sangría por nivel, de modo que el resultado se vea como un índice de documento. 
Debe funcionar para cualquier árbol, no solo para el del ejemplo.
"""

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None
    
    def agregar_hijo(self, hijo):
        if self.izquierdo is None:
            self.izquierdo = hijo
        elif self.derecho is None:
            self.derecho = hijo
        else:
            raise Exception("Un nodo no puede tener más de dos hijos")

#Toca acomodar para que aparezca horizontal y no vertical
def imprimirJerarquia(nodo, nivel=0):
    if nodo is None:
        return
    

    imprimirJerarquia(nodo.izquierdo, nivel + 1)
    

    print("  " * nivel + nodo.nombre)
    

    imprimirJerarquia(nodo.derecho, nivel + 1)


""""
Escriba espejo(nodo) que intercambie el hijo izquierdo y el derecho de TODOS los nodos del árbol. 
Luego imprima el inorden del árbol original y el del árbol espejado.

"""

def espejo(nodo):
    if nodo is None:
        return
    nodo.izquierdo, nodo.derecho = nodo.derecho, nodo.izquierdo
    espejo(nodo.izquierdo)
    espejo(nodo.derecho)

"""
Escriba sonIguales(a, b) que devuelva verdadero si dos árboles tienen la misma forma Y los mismos datos en las mismas posiciones. 
Pruébelo con el árbol original contra su propio espejo: debe dar falso.
"""

def sonIguales(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.nombre != b.nombre:
        return False
    if (a.izquierdo is None) != (b.izquierdo is None):
        return False
    if (a.derecho is None) != (b.derecho is None):
        return False
    if a.izquierdo and not sonIguales(a.izquierdo, b.izquierdo):
        return False
    if a.derecho and not sonIguales(a.derecho, b.derecho):
        return False
    return True


# Ejemplo de uso

raiz = Nodo("A")
hijo_B = Nodo("B")
hijo_C = Nodo("C")
raiz.agregar_hijo(hijo_B)
raiz.agregar_hijo(hijo_C)

hijo_D = Nodo("D")
hijo_E = Nodo("E")
hijo_B.agregar_hijo(hijo_D)
hijo_B.agregar_hijo(hijo_E)

hijo_F = Nodo("F")
hijo_G = Nodo("G")
hijo_C.agregar_hijo(hijo_F)
hijo_C.agregar_hijo(hijo_G)

print("Jerarquía del árbol original:")
imprimirJerarquia(raiz)

espejo(raiz)
print("\nJerarquía del árbol espejado:")
imprimirJerarquia(raiz)

print("\n¿El árbol original y su espejo son iguales?")
print(sonIguales(raiz, espejo(raiz)))
