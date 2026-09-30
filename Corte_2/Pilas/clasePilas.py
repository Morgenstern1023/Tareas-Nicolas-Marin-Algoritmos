"""
Pilas LIFO (Last In, First Out), el ultimo que entra es el primero que sale
Solo se accede al tope de la pila no puede acceder a elementos intermedios
Operaciones: push (x) coloca x al tope de la pila
            pop() elimina y retorna el elemento del tope de la pila si esta no esta vacia
            peek() retorna el elemento del tope de la pila sin eliminarlo precondicionado a que no este vacia
            is_empty() verifica si la pila esta vacia
            size() retorna el numero de elementos en la pila
            top() retorna el elemento del tope de la pila sin eliminarlo, similar a peek()
            tres operaciones: apilar, desapilar y ver el tope (cima) sin sacarlo
            O(1): Tiempos constante

"""

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        if self.vacia():
            return None
        return self.items.pop()

    def cima(self):
        if self.vacia():
            return None
        return self.items[-1]

    def vacia(self):
        return len(self.items) == 0

#Apilar en un array apila al final O(1)
#Apilar en una lista enlazada al inicio O(1)
#Desapilar en un array elimina el ultimo elemento O(1)
#Desapilar en una lista enlazada al inicio O(1)

"""
Ejercicio 1

(a[b]{c}) y (a[b)c]

El segundo esta mal debido a que cierra el parentesis antes de cerrar el corchete

"""

def balanceados(s):
    p =Pila(); pares = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            p.apilar(c)
        elif c in ')]}':
            if p.vacia() or p.desapilar() != pares[c]:
                return False
    return True
    

#Ejemplos
"""
print("{(a[b]{})}")
print(balanceados("{(a[b]{})}"))  # True
print("(a[b)c]")
print(balanceados("(a[b)c]"))    # False
print("([((a))])")
print(balanceados("([((a))])"))  # True
print("((a)[b]{c}})")
print(balanceados("((a)[b]{c}})"))  # False
"""
"""
#Ejercicios
print("([]{})")
print(balanceados("([]{})"))  # True
#Da true por que la pila queda vacia al final
print("([)]")
print(balanceados("([)]"))  # False
#Queda falso debido a que el orden entre parentesis y corchentes no queda balanceado, quedando un corchete en top y encontrando un parentesis
"""

print("(a[b]{c})") 
print(balanceados("(a[b]{c})"))  # True debido a que esta balanceado
print("(a[b)c]")
print(balanceados("(a[b)c]"))  # False porque el orden de los paréntesis y corchetes no está balanceado
print("((()")
print(balanceados("((()"))  # False
#Queda falso debido a que quedan elementos en la pila, si se eliminara la ultima linea del metodo seria true
print("{}[]()")
print(balanceados("{}[]()"))  # True porque esta balanceado
print("Eliminada la ultima linea")

