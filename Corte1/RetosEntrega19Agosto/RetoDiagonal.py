# Se inicializan variables
tamanoMatriz = 0
tamanoMatriz = int(input("Ingrese el tamaño de la matriz: "))
valorMatriz = 0
sumaDiagonalPrincipal = 0
sumaDiagonalSecundaria = 0

matriz = []

#El usuario rellena la matriz con los valores que quiera, se usa .append para agregar los valores a la matriz, ya que en otro caso da error debido a que esta vacia
for i in range(tamanoMatriz):
    fila = []
    for j in range(tamanoMatriz):
        valorMatriz = int(input(f"Ingrese el valor de la posición [{i}][{j}]: "))
        fila.append(valorMatriz)
    matriz.append(fila)

# Se recorre la matriz sumando los valores de la diagonal principal y secundaria
#Se optimiza el recorrido usando un solo for, ya que ambas se pueden con i, solo toca hacer la operacion para la secundaria
for i in range(tamanoMatriz):
    sumaDiagonalPrincipal += matriz[i][i]
    sumaDiagonalSecundaria += matriz[i][tamanoMatriz - 1 - i]

if sumaDiagonalPrincipal == sumaDiagonalSecundaria:
    print("La diagonal principal y secundaria son iguales.")
else:
    print("La diagonal principal y secundaria no son iguales.")
print(f"La suma de la diagonal principal es: {sumaDiagonalPrincipal}")
print(f"La suma de la diagonal secundaria es: {sumaDiagonalSecundaria}")
