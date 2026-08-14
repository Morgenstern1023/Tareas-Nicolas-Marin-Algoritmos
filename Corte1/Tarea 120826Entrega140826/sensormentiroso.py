lecturas = [20, -999, 22, 24, -999, 26]
contadorMentiras = 0
contadorDatos = 0
sumaDatos = 0
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