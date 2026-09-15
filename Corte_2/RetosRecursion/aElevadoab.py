import time

#Función que recibe dos numeros a y b y devuelve a elevado a la b mediante recursión.
def a_elevado_a_b(a, b):
    if b == 0:
        #Caso Base: un numero elevado a 0 es 1
        return 1
    #Caso Recursivo: a se  multiplica por el resultado de a elevado a (b-1)
    return a * a_elevado_a_b(a, b-1)

#Función la cual reduce el tiempo de la función anterior para exponentes pares

def a_elevado_a_b_rapido(a, b):
    if b == 0:
        #Caso Base: un numero elevado a 0 es 1
        return 1
    if b % 2 == 0:
        #Caso Recursivo: si el exponente es par, se calcula a^(b/2) y se multiplica por sí mismo
        mitad = a_elevado_a_b_rapido(a, b // 2)
        return mitad * mitad
    else:
        #Caso Recursivo: si el exponente es impar, se multiplica a por a^(b-1)
        return a * a_elevado_a_b_rapido(a, b - 1)

#Ejemplo de uso
a = 2
b = 64
inicio = time.time()
print(a_elevado_a_b(a, b))
fin = time.time()
print("Tiempo de ejecución:", fin - inicio)

inicio = time.time()
print(a_elevado_a_b_rapido(a, b))
fin = time.time()
print("Tiempo de ejecución metodo rapido:", fin - inicio)
