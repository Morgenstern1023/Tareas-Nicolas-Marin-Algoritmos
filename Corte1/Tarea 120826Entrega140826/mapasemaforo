#Funcion para calcular porcentaje que decide color, se utiliza el if para evitar una division entre 0
def porcentajeColor (valor, minV, maxV):
    if maxV == minV:
        p = 0.5
    else:
       
        p = (valor - minV) / (maxV - minV)
    if p < 0.5:
        #El amarillo se consigue con rojo y verde en 255 entonces a medida que se acerca al 50% ambos crecen
        verde = 255
        rojo = int(255 * (p * 2))

    else: 
        rojo = 255
        verde = int(255 * (1 - (p - 0.5) * 2))

    azul = 0
    #Se retorna el color utilizando ANSI
    return f"\033[48;2;{rojo};{verde};{azul}m\033[30m"

semaforo = [[90,80,70],
            [60,50,40],
            [30,20,10]]

todosValores = [v for fila in semaforo for v in fila]
valorMinimo = min(todosValores)
valorMaximo = max(todosValores)
RESET = "\033[0m"
print("=== MAPA DE SEMÁFORO (Verde -> Amarillo -> Rojo) ===\n")

for fila in semaforo:
    linea = ""
    for valor in fila:
        color = porcentajeColor(valor, valorMinimo, valorMaximo)
        linea += f"{color} {valor:^4} {RESET} " #Reset se usa para pintar los recuadros unicamente
    print(linea)
    print()
