rachaMaxima = 0
rachaActual = 0
datosLluvia = [0,1,1,0,1,1,1,0,1]
for i in datosLluvia:
    if i == 1:
        rachaActual += 1
        if rachaActual > rachaMaxima:
            rachaMaxima = rachaActual
    else:
        rachaActual = 0
print(f"La racha máxima de lluvia fue de {rachaMaxima} días.")