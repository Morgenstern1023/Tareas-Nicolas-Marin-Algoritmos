"""
Notaciones: Dependen de los ordenes
Big O:
O(1): Constante, no cambia con el tamaño de la entrada. v[i]
O(n): Lineal, crece proporcionalmente con el tamaño de la entrada. for i in range(n)
O(n^2): Cuadrática, crece proporcionalmente al cuadrado del tamaño de la entrada. for i in range(n):
    for j in range(n):
O(log n): Logarítmica, crece proporcionalmente al logaritmo del tamaño de la entrada. busqueda binaria
Regla 1: Ignorar las constantes y términos de menor orden. Por ejemplo, O(2n) se simplifica a O(n)
Regla 2: Para operaciones consecutivas, tomar la de mayor orden. Por ejemplo, O(n) + O(n^2) se simplifica a O(n^2)
"""
