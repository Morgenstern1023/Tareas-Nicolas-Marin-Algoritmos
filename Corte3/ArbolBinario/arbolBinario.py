"""
El arbol binario, es una estructura que es no lineal que permite almacenar datos de manera jerárquica
Cada elemento del arbol se llama nodo, y cada uno puede tener cero o mas nodos hijos.
El nodo superior se llama raíz, y los nodos que no tienen hijos se llaman hojas.

Se puede tratar como una estructura de datos, en python puede ser como machine learning

Raiz: Nodo principal, sin padre.
Nodo: Cada elemento del árbol, puede tener cero o más hijos.
Padre e hijo: Relación entre nodos donde un nodo padre tiene uno o más nodos hijos.
Hojas: Nodos que no tienen hijos.
Arista: Conexión entre un nodo padre y un nodo hijo.

Arbol: Cada nodo puede tener n hijos
Arbol binario: Cada nodo puede tener como máximo dos hijos.
Arboles de busqueda binaria ABB: Son árboles binarios donde cada nodo cumple la propiedad de búsqueda binaria, es decir, el valor de cada nodo en el subárbol izquierdo 
es menor que el valor del nodo padre, y el valor de cada nodo en el subárbol derecho es mayor que el valor del nodo padre.

Arboles de decisión: Son árboles utilizados en machine learning para tomar decisiones basadas en características de los datos. 
Cada nodo interno representa una prueba sobre una característica, cada rama representa el resultado de la prueba, y cada hoja representa una clase o valor de predicción.
Se utiliza la libreria Scikit-learn para implementar árboles de decisión en machine learning.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

#Recorrido, existen tres tipos principales: preorden, inorden y postorden.
"""
Catalogo
Herramienta
Libro
Taladro
Sierra
Arte
Tecnico
Redes


SIERRA

                            Catalogo(1)
                         /   
                Herramienta(2)            Libro
                /
            Sierra(2)     Taladro      Arte      Tecnico

                                                 Redes

Catalogo(1)
Herramienta(2)
Sierra(2)

Si tienen el mismo valor se ordena alfabeticamente.

Tarea: Que es el nivel o profundidad

Recorrido por niveles o BFS (Breadth-First Search)

Ejercicio definir los 
"""