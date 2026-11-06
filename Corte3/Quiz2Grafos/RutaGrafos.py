

NOMBRES = ["CENTRO","NORTE","SUR","ORIENTE","OCCIDENTE",
           "CHAPINERO","USAQUEN","BOSA","VEREDA"]
ARISTAS = [(0,1),(0,2),(0,3),(1,4),(1,5),
           (2,7),(3,6),(5,6),(4,7),(7,8),(8,1),(7,5),(5,8),(2,6),(6,8),(5,2)]
N = 9
lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    lista[u].append(v)
def dfs_rec(u, visitado, orden):
    visitado[u] = True          # el hilo de Ariadna
    orden.append(u)
    for v in lista[u]:
        if not visitado[v]:
            dfs_rec(v, visitado, orden)
    return orden

# Version iterativa del recorrido DFS
def dfs_iter(inicio):
    visitado = [False] * N
    pila = [inicio]
    orden = []
    while pila:
        u = pila.pop()                   # LIFO: sale el ultimo que entro
        if visitado[u]:
            continue                     # pudo entrar dos veces a la pila
        visitado[u] = True
        orden.append(u)
        for v in reversed(lista[u]):     # al reves, para igualar al recursivo
            if not visitado[v]:
                pila.append(v)
    return orden

print("DFS recursivo desde CENTRO:", [NOMBRES[i] for i in dfs_rec(0, [False]*N, [])])
print("DFS iterativo desde CENTRO:", [NOMBRES[i] for i in dfs_iter(0)])
print("Componentes conexas de la red completa:")
visitado = [False] * N
for u in range(N):
    if not visitado[u]:
        orden = dfs_rec(u, visitado, [])
        print([NOMBRES[i] for i in orden])

