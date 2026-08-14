cantidadDatos = int(input("Ingrese la cantidad de datos que desea ingresar: "))
lecturas = []
contadorMentiras = 0
contadorDatos = 0
sumaDatos = 0

print("Ingrese los datos de las lecturas (ingrese -999 para indicar un dato falso):")

while len(lecturas) < cantidadDatos: 
    inputDato = input(f"Ingrese el dato {len(lecturas) + 1}: ") #El mas 1 es para que se muestre dato 1,2,3 en lugar de 0,1,2
    lecturas.append(int(inputDato))
for i in lecturas:
    if i == -999:
       contadorMentiras += 1
    else:
        contadorDatos += 1
        sumaDatos += i

print(f"Total de datos falsos: {contadorMentiras}")
print(f"Total de datos válidos: {contadorDatos}")
if contadorDatos > 0:
    print(f"Promedio de datos válidos: {sumaDatos / contadorDatos}")