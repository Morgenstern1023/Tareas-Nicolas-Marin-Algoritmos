#AVL Adelson-Velsky and Landis

"""

            A
        /       \
    B               C
                        \
                            D


"""


"""
Implementar altura, factor equilibrio y recalcular
Implementar rotar a la izquierda y a la derecha respetando el orden de recalcular
construir los 4 arboles desbalanceados y aplicamos la rotación que corresponda
"""

#Rotacion Manual Escriba un pequeño programa que lea por teclado tres claves en el orden en que se insertarían, 
# construya el árbol SIN balancear, diagnostique cuál de los cuatro casos es (o si está equilibrado) y aplique la rotación 
# correcta. Debe imprimir el árbol antes y después. Pista: El diagnóstico sale de dos números: el fe del nodo y el fe de su 
# hijo del lado pesado. No necesita más. Resultado esperado: Con 30, 10, 20 debe diagnosticar LR. Con 10, 20, 30 
# debe diagnosticar RR. Con 10, 30, 20 debe diagnosticar RL.

class Nodo:
    def __init__(self, c):
        self.clave = c; self.izq = None; self.der = None; self.alt = 0
        
def alt(n):  return -1 if n is None else n.alt
def fe(n):   return 0 if n is None else alt(n.izq) - alt(n.der)   # factor de equilibrio
def recalc(n): n.alt = 1 + max(alt(n.izq), alt(n.der))   

def insertar(n, clave):
    if n is None:
        return Nodo(clave)
    if clave < n.clave:
        n.izq = insertar(n.izq, clave)
    elif clave > n.clave:
        n.der = insertar(n.der, clave)
    recalc(n)
    return n

def rotarDerecha(y):
     #        y                x
    #       / \              / \
    #      x   C    ==>     A   y
    #     / \                  / \
    #    A   B                B   C
    x= y.izq; B=x.der
    x.der=y; y.izq=B
    recalc(y);recalc(x)
    return x

def rotarIzquierda(x):
    #      x                  y
    #     / \                / \
    #    A   y      ==>     x   C
    #       / \            / \
    #      B   C          A   B
    y=x.der; B=y.izq
    y.izq=x; x.der=B
    recalc(x);recalc(y)
    return y

def inorden(n,s):
    if n is None:return
    inorden(n.izq,s);s.append(n.clave);inorden(n.der,s)
    
def preorden(n,s):
    if n is None:return
    s.append(f"{n.clave}(fe={fe(n)})"); preorden(n.izq,s);preorden(n.der,s)

def diagnosticar(raiz):
    if fe(raiz) == 2:
        return "LL" if fe(raiz.izq) >= 0 else "LR"
    if fe(raiz) == -2:
        return "RR" if fe(raiz.der) <= 0 else "RL"
    return None

def aplicarRotacion(raiz, caso):
    if caso == "LL":
        return rotarDerecha(raiz)
    if caso == "RR":
        return rotarIzquierda(raiz)
    if caso == "LR":
        raiz.izq = rotarIzquierda(raiz.izq)
        return rotarDerecha(raiz)
    if caso == "RL":
        raiz.der = rotarDerecha(raiz.der)
        return rotarIzquierda(raiz)
    return raiz

#funcion para ver el arbol dibujado
def ver(titulo,raiz):
    s=[]; preorden(raiz,s)
    t=[]; inorden(raiz,t)
    print(f"{titulo:22s} preorden: {' '.join(s)}")
    print(f"{'':22s} inorden: {t} altura={alt(raiz)}")

def imprimirJerarquia(nodo, nivel=0):
    if nodo is None:
        return
    

    imprimirJerarquia(nodo.izq, nivel + 1)
    

    print("  " * nivel + str(nodo.clave))
    

    imprimirJerarquia(nodo.der, nivel + 1)


def main():
    a=int(input("Ingrese la primera clave: "))
    b=int(input("Ingrese la segunda clave: "))
    c=int(input("Ingrese la tercera clave: "))
    raiz = None
    for clave in (a, b, c):
        raiz = insertar(raiz, clave)

    ver("Árbol antes de la rotación", raiz)
    imprimirJerarquia(raiz)

    caso = diagnosticar(raiz)
    if caso is None:
        print("Equilibrado, no hace falta rotar")
    else:
        print(f"Caso: {caso}.")
        raiz = aplicarRotacion(raiz, caso)

    ver("Árbol después de la rotación", raiz)
    imprimirJerarquia(raiz)

if __name__=="__main__":
    main()