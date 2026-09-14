import time
nivel = 0

def factorial(n):
    global nivel
    print("|" * nivel + f"factorial({n}) entra")

    nivel += 1

    r = 1 if n <= 1 else n * factorial(n - 1)
    nivel -= 1
    print("|" * nivel + f"factorial({n}) devuelve {r}")
    return r
   

def fibonacci(n):
    if n <= 1:
        return n
    else:
        r = fibonacci(n - 1) + fibonacci(n - 2)
    return r

print("--- traza de la pila de llamadas ---")
r = factorial(4)
print("Resultado 4: ",r)
r =  factorial(5)
print("Resultado 5: ",r)
print()
inicio = time.perf_counter()
print("fibonacci de 5 =", fibonacci(5))
fin = time.perf_counter()
print(f"tiempo de ejecución {fin - inicio} segundos")

inicio = time.perf_counter()
print("fibonacci de 10 =", fibonacci(10))
fin = time.perf_counter()
print(f"tiempo de ejecución {fin - inicio} segundos")

inicio = time.perf_counter()
print("fibonacci de 15 =", fibonacci(15))
fin = time.perf_counter()
print(f"tiempo de ejecución {fin - inicio} segundos")