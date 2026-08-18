#Se inicializan variables
filasMatriz = 0
filasMatriz = int(input("Ingrese el número de filas de la matriz: "))
columnasMatriz = 0
columnasMatriz = int(input("Ingrese el número de columnas de la matriz: "))
matriz = []
matrizRotada = []

#For para que el usuario ingrese valores de matriz
for i in range(filasMatriz):
    fila = []
    for j in range(columnasMatriz):
        valorMatriz = int(input(f"Ingrese el valor de la posición [{i}][{j}]: "))
        fila.append(valorMatriz)
    matriz.append(fila)
#For que rota la matriz, cambia filas por columnas, la resta es para evitar que esten de primeros los valores de la primera fila porque seria 270
for i in range(columnasMatriz):
    filaRotada = []
    for j in range(filasMatriz):
        filaRotada.append(matriz[filasMatriz - 1 - j][i])
    matrizRotada.append(filaRotada)

for i in range(columnasMatriz):
    for j in range(filasMatriz):
        print(matrizRotada[i][j], end=" ")
    print()
