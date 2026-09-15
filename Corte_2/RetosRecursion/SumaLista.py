## La función recibe una lista de números y devuelve la suma de todos sus elementos mediante recursión.
def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])

lista = [1, 2, 3, 4, 5]
print(suma_lista(lista))