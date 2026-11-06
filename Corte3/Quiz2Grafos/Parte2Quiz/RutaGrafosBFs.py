from collections import deque


NOMBRES = ["CENTRO","NORTE","SUR","ORIENTE","OCCIDENTE",
           "CHAPINERO","USAQUEN","BOSA","VEREDA"]
ARISTAS = [(0,1),(0,2),(0,3),(1,4),(1,5),
           (2,7),(3,6),(5,6),(4,7),(7,8),(8,1),(7,5),(5,8),(2,6),(6,8),(5,2)]
N = 9
lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    lista[u].append(v)
    lista[v].append(u)
def bfs(inicio):
    visitado = [False] * N
    dist  = [-1] * N          # distancia en numero de tramos
    padre = [-1] * N          # de donde llegue: permite reconstruir el camino
    cola = deque([inicio])
    visitado[inicio] = True   # se marca al ENCOLAR, no al sacar
    dist[inicio] = 0
    orden = []
    while cola:
        u = cola.popleft()    # FIFO: sale el primero que entro
        orden.append(u)
        for v in lista[u]:
            if not visitado[v]:
                visitado[v] = True
                dist[v]  = dist[u] + 1
                padre[v] = u
                cola.append(v)
    return orden, dist, padre

print("CAMINO MAS CORTO desde CENTRO hacia VEREDA:")
inicio = 0
destino = 8
orden, dist, padre = bfs(inicio)
if dist[destino] == -1:
    print("No existe una ruta.")
else:
    camino = []
    v = destino
    while v != -1:
        camino.append(v)
        v = padre[v]
    camino.reverse()
    for i, nodo in enumerate(camino):
        if i > 0:
            print(" -> ", end="")
        print(NOMBRES[nodo], end="")
    print(f" ({dist[destino]} tramos)")
