usoHora = 0
franjaCongestion = 0
totalDia = 0
totalMaxDia = 0
UsoHorarioSalaKnuth = [[usoHora, usoHora, usoHora, usoHora, usoHora, usoHora],
                       [usoHora, usoHora, usoHora, usoHora, usoHora, usoHora],
                       [usoHora, usoHora, usoHora, usoHora, usoHora, usoHora],
                       [usoHora, usoHora, usoHora, usoHora, usoHora, usoHora],
                       [usoHora, usoHora, usoHora, usoHora, usoHora, usoHora]]
#Se le pide al usuario que ingrese cada dato usando for anidado para cada uno
for i in range(5):
    for j in range(6):
        inputHora = int(input(f"Ingrese el uso horario de la sala Knuth para el día {i + 1} y la hora {j + 1}: "))
        UsoHorarioSalaKnuth[i][j] = inputHora

for i in range(5):
    for j in range(6):
        #Se busca la franja horaria con mayor congestion, no menciona multiples franjas con el mismo valor, solo toma la primera
        if UsoHorarioSalaKnuth[i][j] > franjaCongestion:
            franjaCongestion = UsoHorarioSalaKnuth[i][j]
            diaCongestion = i
            horaCongestion = j
#Se dice el dia yla hora de mayor congestion numericamente y cuando se uso, para que diga el dia se puede hacer un switch o varios ifs
print(f"La franja horaria con mayor congestion es el día {diaCongestion + 1} y la hora {horaCongestion + 1} con un uso horario de {franjaCongestion}.")

#Se crea un for anidado que sume el uso total de cada dia y si es mayor lo reemplaza, al salir del bucle se imprime el dia con mayor gente y cuantos fueron
for i in range(5):
    for j in range(6):
        totalDia = totalDia + UsoHorarioSalaKnuth[i][j]
    if totalDia > totalMaxDia:
        totalMaxDia = totalDia
        diaMax = i
    totalDia = 0
print(f"El día con mayor uso, es el día {diaMax + 1} con un total de {totalMaxDia} de uso de usuarios.")

for i in range(5):
    for j in range(6):
        if UsoHorarioSalaKnuth[i][j] < 5:
            print(f"El día {i + 1} y la hora {j + 1} tuvo un uso menor a 5 personas.")