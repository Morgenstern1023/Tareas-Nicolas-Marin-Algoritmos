
"""
Reto 1 — El detector de islas · Obligatorio Sobre la red de su proyecto, escriba un informe automático que diga cuántos componentes hay, qué vértices tiene cada una, y cuál es la más grande. Después de eliminar dos aristas a propósito y vuelva a correrlo.

Pista: El componente de un vértice se identifica con un número: asigne a cada vértice el índice de la componente a la que pertenece durante el recorrido.

Resultado esperado: Un informe legible, no una lista de números. Debe decir, por ejemplo, 'la red está partida en 3 zonas; la zona 2 tiene 4 puntos y no tiene conexión con el centro'.

Reto 2 — El plan de estudios imposible · Obligatorio Construya un grafo DIRIGIDO de prerrequisitos con al menos seis asignaturas e introduzca a propósito un ciclo. Escriba un detector de ciclos para gráficos dirigidos y haga que informe cuáles asignaturas forman el ciclo.

Pista: En un gráfico dirigido a la regla del padre NO sirve. Se necesitan tres estados por vértice: sin visitar, en proceso, y terminado. Encontrar un vecino en el proceso es el ciclo.

Resultado esperado: El programa debe imprimir la secuencia de asignaturas del ciclo, no solo decir que existe.

Reto 3 — El camino más largo (reto corchador) · Obligatorio Escriba una función que encuentre el camino más LARGO sin repetir vértices entre dos puntos de la red. Mida cuánto tarda con 9 vértices, con 15 y con 20.

Pista: Esto no es DFS con visitado: hay que desmarcar al regresar, como en el backtracking de la sesión 15. Y cuidado con el tiempo.

Resultado esperado: Al llegar a 20 vértices el programa se vuelve impracticable. Eso no es un error suyo: el problema del camino más largo es NP-difícil. Escriba un párrafo explicando por qué el camino más CORTO sí es fácil (sesión 42) y el más largo no.
"""
from time import perf_counter

#Reto1 
#Funcion que realiza DFS para encontrar todas las islas (componentes conectados) en el grafo, si no visita uno se hace la búsqueda desde ese vértice(vecino)
def islas_dfs(grafo, vertice, visitado, componente):
    visitado[vertice] = True
    componente.append(vertice)
    for vecino in grafo[vertice]:
        if not visitado[vecino]:
            islas_dfs(grafo, vecino, visitado, componente)

#Funcion que detecta todas las islas en el grafo y devuelve la lista de componentes conectados
def detectar_islas(grafo):
    visitado = [False] * len(grafo)
    componentes = []
    for vertice in range(len(grafo)):
        if not visitado[vertice]:
            componente = []
            islas_dfs(grafo, vertice, visitado, componente)
            componentes.append(componente)
    return componentes
#Funcion que imprime un informe sobre las islas detectadas en el grafo y devuelve la zona más grande y su tamaño
def informe_islas(grafo):
    componentes = detectar_islas(grafo)
    print(f"La red está partida en {len(componentes)} zonas.")
    for i, componente in enumerate(componentes):
        print(f"La zona {i+1} tiene {len(componente)} puntos: {componente}")
    mas_grande = max(componentes, key=len)
    print(f"La zona más grande es la zona {componentes.index(mas_grande)+1} con {len(mas_grande)} puntos.")
    return componentes.index(mas_grande)+1, len(mas_grande)

#Reto 2

#Funcion que realiza DFS para detectar ciclos en un grafo dirigido
def ciclo_dfs(grafo, vertice, visitado, en_proceso, ciclo):
    visitado[vertice] = True
    en_proceso[vertice] = True
    for vecino in grafo[vertice]:
        if en_proceso[vecino]:
            ciclo.append(vecino)
            return True
        if not visitado[vecino]:
            if ciclo_dfs(grafo, vecino, visitado, en_proceso, ciclo):
                ciclo.append(vertice)
                return True
    en_proceso[vertice] = False
    return False

#Funcion que detecta un ciclo en el grafo y devuelve la secuencia de vértices del ciclo
def detectar_ciclo(grafo):
    visitado = [False] * len(grafo)
    en_proceso = [False] * len(grafo)
    ciclo = []
    for vertice in range(len(grafo)):
        if not visitado[vertice]:
            if ciclo_dfs(grafo, vertice, visitado, en_proceso, ciclo):
                ciclo.reverse()
                return ciclo
    return None

#Funcion que imprime un informe sobre el ciclo detectado en el grafo
def informe_ciclo(grafo):
    ciclo = detectar_ciclo(grafo)
    if ciclo:
        print(f"Se ha detectado un ciclo: {ciclo}")
    else:
        print("No se ha detectado ningún ciclo.")
    return ciclo

#Reto 3

def camino_mas_largo(grafo, inicio, destino):
    # Verifica que los índices de inicio y destino sean válidos dentro del grafo (Agregado por IA)
    if not 0 <= inicio < len(grafo) or not 0 <= destino < len(grafo):
        raise ValueError("El inicio y el destino deben ser índices válidos del grafo.")

    visitado = [False] * len(grafo)
    camino_actual = [inicio]
    mejor_camino = []
    visitado[inicio] = True

    def buscar(vertice):
        #El nonlocal permite modificar la variable mejor_camino definida en el ámbito externo a esta función(Agregado por IA)
        nonlocal mejor_camino

        if vertice == destino:
            if len(camino_actual) > len(mejor_camino):
                mejor_camino = camino_actual.copy()
            return

        for vecino in grafo[vertice]:
            if not visitado[vecino]:
                visitado[vecino] = True
                camino_actual.append(vecino)
                buscar(vecino)
                camino_actual.pop()
                visitado[vecino] = False

    buscar(inicio)
    return mejor_camino

#El camino más corto se resuelve eficientemente con DFS, por que visita vértices y aristas con una complejidad de O(V + E).
#En cambio el mas largo es una combinacion con backtracking, ya que se deben explorar todas las posibles rutas para encontrar la de mayor longitud.

