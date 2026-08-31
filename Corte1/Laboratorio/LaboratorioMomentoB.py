jornadaEspecial = []

print("Ingrese la cantidad de jornadas especiales que desea registrar:")
cantidadPuntosAcopioEspeciales = int(input())
for i in range(cantidadPuntosAcopioEspeciales):
    print("Ingrese el peso del punto de acopio especial", (i + 1), ":")
    peso = float(input())
    jornadaEspecial.append(peso)
promedio = sum(jornadaEspecial) / len(jornadaEspecial)
print("El promedio de los pesos de los puntos de acopio especiales es:", promedio)

# En lugar de crear punteros como en c, en python se crean referencias a los objetos. Por lo tanto, si se modifica un objeto a través de una referencia, todas las referencias a ese objeto verán el cambio. Esto es diferente a C, donde se pueden crear punteros que apuntan a diferentes direcciones de memoria y modificar los valores en esas direcciones sin afectar a otras variables.