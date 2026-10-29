
#Acomodar para que guarde codigo y nombre

class Nodo:
    def __init__(self, clave, nombreRecurso=""):
        self.clave = clave; self.nombre = nombreRecurso
        self.izq = None; self.der = None
        
def insertar(n, clave, nombreRecurso=""):
    if n is None: return Nodo(clave, nombreRecurso)
    if clave < n.clave: n.izq = insertar(n.izq, clave, nombreRecurso)   # el retorno se REENGANCHA
    elif clave > n.clave: n.der = insertar(n.der, clave, nombreRecurso)
     # clave repetida: no se inserta
    return n

def buscar(n, clave, pasos=None):
    if pasos is not None: pasos.append("vacio" if n is None else str(n.clave))
    if n is None or n.clave == clave: return n
    return buscar(n.izq, clave, pasos) if clave < n.clave else buscar(n.der, clave, pasos)

def minimo(n):
    while n.izq is not None: n=n.izq
    return n
 
def maximo(n):
    while n.der is not None: n = n.der
    return n
 
def eliminar(n, clave):
    if n is None: return None
    if clave < n.clave: n.izq = eliminar(n.izq, clave)
    elif clave > n.clave: n.der = eliminar(n.der, clave)
    else: #encontramos el nodo a eliminar
        if n.izq is None: return n.der
        if n.der is None: return n.izq
        suc=minimo(n.der)
        n.clave,n.nombre=suc.clave,suc.nombre
        n.der=eliminar(n.der,suc.clave)
    return n
def inorden(n, s):
    if n is None: return
    inorden(n.izq, s); s.append((n.clave, n.nombre)); inorden(n.der, s)
    
def altura(n):
    if n is None: return -1
    return 1 + max(altura(n.izq), altura(n.der))

def hijos(n,clave):
    n=buscar(n,clave)
    if n is None: return -1
    return (1 if n.izq else 0) + (1 if n.der else 0)

#Funcion que ordena los nodos en inorden y devuelve una lista de tuplas (clave, nombre)
def obtener_inorden(n):
    s = []
    inorden(n, s)
    return s

#Función que busca el recurso por calve o codigo y devuelve el nombre o mensaje de no encontrado, ademas de comparaciones

def buscar_recurso(n, clave):
    pasos = []
    nodo = buscar(n, clave, pasos)
    if nodo is None:
        return "Recurso no encontrado", pasos
    return nodo.nombre, pasos

#Función que da todos los valores de los nodos que entren en un rango especificado
def rango(n, min_clave, max_clave, s=None):
    if s is None: s = []
    if n is None: return s
    if min_clave < n.clave: rango(n.izq, min_clave, max_clave, s)
    if min_clave <= n.clave <= max_clave: s.append((n.clave, n.nombre))
    if max_clave > n.clave: rango(n.der, min_clave, max_clave, s)
    return s



def esBST(n, min_clave=float('-inf'), max_clave=float('inf')):
    if n is None: return True
    if not (min_clave < n.clave < max_clave): return False
    return esBST(n.izq, min_clave, n.clave) and esBST(n.der, n.clave, max_clave)

#ejemplo de uso 10 recursos

arbol = None
recursos = [
    (10, "Recurso A"),
    (5, "Recurso B"),
    (15, "Recurso C"),
    (3, "Recurso D"),
    (7, "Recurso E"),
    (12, "Recurso F"),
    (18, "Recurso G"),
    (1, "Recurso H"),
    (4, "Recurso I"),
    (6, "Recurso J")
]
for clave, nombre in recursos:
    arbol = insertar(arbol, clave, nombre)
    
# Ejemplo de búsqueda de un recurso
nombre, pasos = buscar_recurso(arbol, 7)
print(f"Nombre del recurso: {nombre}")
print(f"Pasos de búsqueda: {pasos}")

# Ejemplo de obtención de los recursos en inorden
inorden_lista = obtener_inorden(arbol)
print(f"Recursos en inorden: {inorden_lista}")

#ejemplo de uso de esBST 
arbol_contraejemplo = Nodo(50)
arbol_contraejemplo.izq = Nodo(30)
arbol_contraejemplo.izq.der = Nodo(60)
print(f"Es BST: {esBST(arbol_contraejemplo)}")