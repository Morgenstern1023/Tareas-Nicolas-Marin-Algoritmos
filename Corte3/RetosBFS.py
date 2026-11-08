"""Reto 1 — El módulo de rutas · Obligatorio · entregable del taller Sobre la red de su proyecto, escriba ruta(origen, destino) que devuelva el camino con menos tramos y su longitud, o un mensaje claro si no hay camino. Pruébelo con un destino alcanzable y con uno que no lo sea.

Pista: El caso sin camino es el que casi nadie prueba. Si dist[destino] sigue en −1 al terminar el BFS, no hay ruta.

Resultado esperado: La función debe manejar correctamente los tres casos: ruta normal, origen igual a destino, y destino inalcanzable.

Reto 2 — Los grados de separación · Obligatorio Calcule, para cada par de vértices de su red, la distancia mínima entre ellos. Reporte el diámetro de la red, que es la mayor de todas esas distancias, e identifique qué par de puntos lo produce.

Pista: Un BFS desde cada vértice. Son V recorridos de O(V+E), es decir O(V·(V+E)) en total. Para redes pequeñas es perfectamente viable.

Resultado esperado: El diámetro y el par de puntos más alejados. Interprete el resultado: ¿qué significa para la operación de su sistema?

Reto 3 — La propagación por olas (reto corchador) · Obligatorio Suponga que una falla se origina en un punto y se propaga a los vecinos en un minuto. Escriba un programa que diga en qué minuto queda afectado cada punto y cuántos minutos tarda en caer toda la red. Luego responda: ¿desde qué punto conviene MENOS que empiece la falla?

Pista: La respuesta a la primera parte es literalmente el arreglo dist. La segunda parte pide buscar el vértice que minimice la excentricidad, que es lo que haremos en la sesión 43.

Resultado esperado: El punto desde el cual la falla tarda más en propagarse es el punto más periférico de la red. Nómbrelo y explique por qué un centro de distribución debería estar en el extremo opuesto."""

#Reto 1 
def ruta(grafo, origen, destino):
    from collections import deque
    dist = [-1] * len(grafo)
    prev = [None] * len(grafo)
    dist[origen] = 0
    q = deque([origen])
    while q:
        u = q.popleft()
        for v in grafo[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                prev[v] = u
                q.append(v)
    if dist[destino] == -1:
        return f"No hay camino de {origen} a {destino}."
    camino = []
    u = destino
    while u is not None:
        camino.append(u)
        u = prev[u]
    camino.reverse()
    return camino, dist[destino]

#Reto 2
def grados_separacion(grafo):
    from collections import deque
    n = len(grafo)
    diametro = 0
    par_mas_alejado = (None, None)
    for origen in range(n):
        dist = [-1] * n
        dist[origen] = 0
        q = deque([origen])
        while q:
            u = q.popleft()
            for v in grafo[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        for destino in range(n):
            if dist[destino] > diametro:
                diametro = dist[destino]
                par_mas_alejado = (origen, destino)
    return diametro, par_mas_alejado

#Reto 3
def propagacion_olas(grafo, origen):
    #deque es una cola que permite agregar y quitar elementos por ambos extremos, útil para BFS
    from collections import deque
    n = len(grafo)
    dist = [-1] * n
    dist[origen] = 0
    q = deque([origen])
    while q:
        u = q.popleft()
        for v in grafo[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    minutos_totales = max(dist)
    # Mejor punto para que empiece la falla
    mejor_origen = dist.index(min(dist))
    return dist, minutos_totales, mejor_origen

#EL mejor punto para que empiece la falla es el que esta mas en la periferia, debido a que desde ahí la falla tarda más en propagarse a toda la red.

