# ============================================================
#  Laboratorio integrador · Corte 3 · RETO 3  (25 puntos)
#  Sesiones 40 y 42 — Representacion de grafos y BFS
#  Sistema: RedAcopio — rutas minimas entre puntos de la red
#
#  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r3.py
#  Ejecute:   python3 pruebas_r3.py
#Estudiante Nicolas
# ============================================================
from collections import deque

NOMBRES = ["ACOPIO","NORTE","SUR","ORIENTE","OCCIDENTE",
           "PLANTA","TALLER","PUERTO","VEREDA","MINA"]
ARISTAS = [(0,1),(0,2),(0,3),(1,4),(1,5),(2,7),(3,6),(5,6),(4,7),(7,8),(6,9)]
N = len(NOMBRES)


def construir():
    #Construye la lista de adyacencia del grafo
    """Devuelve la lista de adyacencia: una lista de N listas.
       El grafo es NO DIRIGIDO, asi que cada arista se registra en los dos
       extremos. Cada lista de vecinos debe quedar ORDENADA de menor a mayor.

       PENDIENTE: implementar."""

    #Crea una lista de N listas vacias
    lista = [[] for _ in range(N)]
    #Agrega cada arista a ambos extremos
    for u, v in ARISTAS:
        lista[u].append(v)
        lista[v].append(u)
    #Ordena cada lista de vecinos, para que queden de menor a mayor
    for vecinos in lista:
        vecinos.sort()
    return lista


def bfs(inicio):
    #Recorrido en anchura desde el nodo 'inicio'
    """Recorrido en anchura desde 'inicio'.
       Devuelve la tupla (orden, dist, padre):
         orden  lista de vertices en el orden en que se atendieron
         dist   dist[v] = numero de tramos desde inicio (-1 si no se alcanza)
         padre  padre[v] = vertice desde el que se llego a v (-1 para el inicio)

       Recuerde: se marca el vertice al ENCOLARLO, no al sacarlo.

       PENDIENTE: implementar."""
    #Inicializa la lista de adyacencia, el orden de atencion, las distancias y los padres
    lista = construir()
    orden = []
    dist = [-1] * N
    padre = [-1] * N
    q = deque()
    dist[inicio] = 0
    q.append(inicio)
    #Marca el nodo de inicio como visitado y lo encola
    while q:
        u = q.popleft()
        orden.append(u)
        for v in lista[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                padre[v] = u
                q.append(v)
    return orden, dist, padre


def camino(destino, padre):
    """Ya implementado: reconstruye la ruta siguiendo el arreglo padre."""
    ruta = []
    v = destino
    while v != -1:
        ruta.append(NOMBRES[v])
        v = padre[v]
    return list(reversed(ruta))


def por_niveles(dist):
    #Devuelve los vertices agrupados por su distancia desde el origen
    """Devuelve una lista de listas: en la posicion d, los NOMBRES de los
       vertices que estan a distancia d del origen.

       PENDIENTE: implementar."""
    #Encuentra la distancia maxima
    max_dist = max(dist)
    #Crea una lista de listas vacias de tamaño max_dist + 1
    niveles = [[] for _ in range(max_dist + 1)]
    #Agrega cada vertice a su nivel correspondiente
    for v, d in enumerate(dist):
        if d != -1:
            niveles[d].append(NOMBRES[v])
    return niveles
