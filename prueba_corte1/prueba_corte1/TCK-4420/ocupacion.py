# ============================================================
#  Cívica Software  ·  TCK-4420  ·  Severidad P3
#  Sistema: RedAcopio  —  Reporte de ocupación
#  NO MODIFIQUE la seccion de datos ni el archivo de pruebas.
# ============================================================

# filas = puntos de acopio, columnas = dias de la semana
ocupacion = [
    [4, 2, 6, 1, 3, 0],
    [0, 5, 5, 2, 7, 1],
    [8, 1, 0, 4, 2, 6],
    [3, 3, 3, 0, 0, 5],
]

def total_por_punto(m):
    """Devuelve una lista con el total recogido por cada punto (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def total_por_dia(m):
    #Se cambia la i por la j y viceversa para recorrer correctamente la matriz y sumar por columnas en lugar de filas
    """Devuelve una lista con el total recogido cada dia (columna).
       BUG REPORTADO: entrega totales incorrectos."""
    totales = []
    for j in range (len(m[0])):
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        totales.append(s)
    return totales


def dia_mas_flojo(m):
    """Devuelve el indice del dia con MENOR recoleccion total.
       PENDIENTE: implementar."""
    #Se implementa la función dia mas flojo Suma cada columna y luego revisa con un if si es menor que el minimo actual, si es el primero lo cambia, tambien si es cero para el primero
    for j in range(len(m[0])):
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        if j == 0 or s < min_s:
            min_s = s
            min_j = j
            dia_mas_flojo = j
    return dia_mas_flojo


def puntos_inactivos(m):
    """Devuelve cuantos registros estan en 0 (el punto no opero ese dia).
       PENDIENTE: implementar."""
    #Se implementa la función puntos inactivos que Revisa si el elemento es cero y si lo es suma uno a inactivos, cuando terminan los ciclos devuelve el total
    inactivos = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                inactivos += 1
    return inactivos
    
