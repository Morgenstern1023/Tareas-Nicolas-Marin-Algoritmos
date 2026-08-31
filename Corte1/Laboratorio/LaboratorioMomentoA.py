matriz = []

# Recoger valores de la matriz:
for i in range(4):
    fila = []
    for j in range(6):
        valor = input("Ingrese el valor del dia {} del punto de acopio {}: ".format(j + 1, i + 1))
        fila.append(valor)
    matriz.append(fila)

##Calcular total de cada punto de acopio:

for i in range(4):
    total = 0
    for j in range(6):
        total += int(matriz[i][j])
    print("El total del punto de acopio {} es: {}".format(i + 1, total))

## Calcular total por dia (Dia más y menos productivo):

for j in range(6):
    total_dia = 0
    diaMasProductivo = 0
    diaMasProductivoIndex = 0
    diaMenosProductivo = 100000000
    diaMenosProductivoIndex = 0
    for i in range(4):
        total_dia += int(matriz[i][j])
    print("El total del dia {} es: {}".format(j + 1, total_dia))
    if total_dia > diaMasProductivo:
        diaMasProductivo = total_dia
        diaMasProductivoIndex = j + 1
    if total_dia < diaMenosProductivo:
        diaMenosProductivo = total_dia
        diaMenosProductivoIndex = j + 1
print("El dia mas productivo fue el dia {} con un total de {}".format(diaMasProductivoIndex, diaMasProductivo))
print("El dia menos productivo fue el dia {} con un total de {}".format(diaMenosProductivoIndex, diaMenosProductivo))
