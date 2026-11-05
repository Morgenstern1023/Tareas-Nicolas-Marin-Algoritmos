#Modele la red real de su línea con mínimo diez vértices y quince aristas. Impleméntela en las dos representaciones, 
# calcule la densidad y escriba dos líneas justificando cuál usará el proyecto.

#Prototipo o idea inicial

#Representar la red del proyecto con las sedes como vertices y el recorrido entre ellas como aristas.
# En caso de no ser suficientes vertices se puede plantear hacer la busqueda de recursos no como arbol binario, en cambio grafos
# Queda como posible idea a revisar


# más efectiva que existe para este tipo de funciones. Escríbala antes que las conversiones. 
# Resultado esperado: listaAMatriz(matrizALista(m)) debe ser igual a m para cualquier m válida.

def prueba_ida_y_vuelta(m):
    return listaAMatriz(matrizALista(m)) == m

def matrizALista(m):
    l = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 0:
                l.append((i, j, m[i][j]))
    return l

def listaAMatriz(l):
    if not l:
        return []
    n = max(max(i, j) for i, j, _ in l) + 1
    m = [[0] * n for _ in range(n)]
    for i, j, val in l:
        m[i][j] = val
    return m
# Ejemplo de uso
m = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
]
print(prueba_ida_y_vuelta(m))  # Debería imprimir True
print(prueba_ida_y_vuelta([]))  # Debería imprimir True para la matriz vacía



# Un grafo no dirigido de cinco vértices donde todos tengan grado 3 no puede existir.
# Esto debido a que la suma de los grados de todos los vértices es par, ya que cada arista contribuye  dos grados.
# En un grafo de cinco vértices donde todos tienen grado 3, la suma de los grados sería 5 * 3 = 15, que es impar.
# Por lo tanto, no puede existir tal grafo.

# Generalización: Para un grafo no dirigido con V vértices donde todos tienen grado d, la suma de los grados sería V * d.
# Esta suma debe ser par, ya que cada arista contribuye a dos grados. Por lo tanto, V * d debe ser par.
# Si V * d es impar, no puede existir tal grafo.

