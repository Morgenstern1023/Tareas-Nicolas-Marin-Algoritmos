numeroCodigo = input("Este programa determina si un numero es un palindromo o no. \n\nIngrese un numero: ")
numeroString = str(numeroCodigo)
digitosNumero = list(numeroString)

for i in range(len(digitosNumero) // 2 and len(digitosNumero) != 0):
    #El -i + 1 es porque en python el negativo es el negativo del indice
    if digitosNumero[i] != digitosNumero[-(i + 1)]:
        print(f"El numero {numeroCodigo} no es un palindromo, es decir no es un codigo valido.")
        break
    else:
        print(f"El numero {numeroCodigo} es un palindromo, es decir el codigo es valido.")
