def siguienteMayor(a):
    n = len(a)
    r = [-1] * n
    pila = []
    
    for i in range(n):
        while pila and a[i] > a[pila[-1]]:
            r[pila.pop()] = a[i]
        pila.append(i)
    
    return r

def siguienteMayorDistancia(a):
    n = len(a)
    r = [-1] * n
    pila = []
    
    for i in range(n):
        while pila and a[i] > a[pila[-1]]:
            idx = pila.pop()
            distancia = i - idx
            r[idx] = distancia
        pila.append(i)
    r = reemplazoMenosUnoPorCero(r)
    return r

def reemplazoMenosUnoPorCero(a):
    return [0 if x == -1 else x for x in a]

print(siguienteMayorDistancia([73,74,75,71,69,72,76,73]))