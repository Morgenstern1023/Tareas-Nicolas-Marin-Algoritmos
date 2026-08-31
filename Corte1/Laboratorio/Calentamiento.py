m = [[0] * 2 for _ in range(2)]
m[0][0] = 7
print(m)
#Esto da como resultado [[7, 0], [0, 0]] porque cada lista interna es independiente.

def f(lista):
    lista = lista + [4]

datos = [1, 2, 3]
f(datos)
print(datos)
#Esto da como resultado [1, 2, 3] porque la función f crea una nueva lista y no modifica la lista original.
