numero1 = input ("Escriba el primer numero:")
numero2 = input ("Escriba el segundo numero:")
operacion =input ("Escriba la operacion que desea realizar: suma, resta, multiplicacion, division, potencia, raiz: ")

if operacion == "suma":
    resultado = float(numero1) + float(numero2)
    print("El resultado de la suma es: ", resultado)
elif operacion == "resta":
    resultado = float(numero1) - float(numero2)
    print("El resultado de la resta es: ", resultado)
elif operacion == "multiplicacion":
    resultado = float(numero1) * float(numero2)
    print("El resultado de la multiplicacion es: ", resultado)
elif operacion == "division":
    resultado = float(numero1) / float(numero2)
    print("El resultado de la division es: ", resultado)
elif operacion == "potencia":
    resultado = float(numero1) ** float(numero2)
    print("El resultado de la potencia es: ", resultado)
elif operacion == "raiz":
    resultado = float(numero1) ** (1/float(numero2))
    print("El resultado de la raiz es: ", resultado)
else:
    print("Input invalido, por favor ingrese una operacion valida: suma, resta, multiplicacion, division, potencia, raiz")