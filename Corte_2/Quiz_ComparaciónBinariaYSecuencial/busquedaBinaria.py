import time

#Busquedas secuenciales y binarias
def binaria(v,x):
    inicio = time.perf_counter()
    cantidadPasos = 0
    izq=0
    der=len(v)-1
    while izq<=der:
        medio=(izq+der)//2
        if v[medio]==x:
            fin = time.perf_counter()
            cantidadPasos += 1
            print(f"Cantidad de pasos: {cantidadPasos}")
            print(f"Tiempo de ejecución: {fin - inicio} segundos")
            return medio
        elif v[medio]<x:
            izq=medio+1
            cantidadPasos += 1
        else:
            der=medio-1
            cantidadPasos += 1
    fin = time.perf_counter()
    print(f"Cantidad de pasos: {cantidadPasos}")
    print(f"Tiempo de ejecución: {fin - inicio} segundos")

    return -1
#A[0,n-1] xEA, si no lo hace devuelve -1

def secuencial(v,x):
    inicio = time.perf_counter()
    cantidadPasos = 0
    for i in range(len(v)):
        cantidadPasos += 1
        if v[i]==x:
            fin = time.perf_counter()
            print(f"Cantidad de pasos: {cantidadPasos}")
            print(f"Tiempo de ejecución: {fin - inicio} segundos")
            return i
    fin = time.perf_counter()
    print(f"Cantidad de pasos: {cantidadPasos}")
    print(f"Tiempo de ejecución: {fin - inicio} segundos")
    return -1

vector=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
print ("Busqueda binaria")
print("elemento", 10,  "indice en el que se encuentra:", binaria(vector,10))
print ("Busqueda secuencial")
print("elemento", 10,  "indice en el que se encuentra:", secuencial(vector,10))