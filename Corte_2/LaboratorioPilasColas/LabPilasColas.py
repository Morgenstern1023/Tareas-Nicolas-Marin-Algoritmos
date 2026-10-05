# Cola sobre lista enlazada

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
    def estaVacia(self):
        return self.frente is None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.estaVacia():
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.estaVacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato

    def verFrente(self):
        if self.estaVacia():
            return None
        return self.frente.dato

    def verCuantosHay(self):
        contador = 0
        actual = self.frente
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

# ejemplo de uso en el cual se vacia todos los elementos de la cola y se vuelve a encolar

cola = Cola()

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Frente:", cola.verFrente())
print("Cantidad de elementos:", cola.verCuantosHay())
print("Desencolando:", cola.desencolar())
print( cola.desencolar())
print( cola.desencolar())
print( cola.desencolar())
print("Frente después de vaciar la cola:", cola.verFrente())
print("Cantidad de elementos después de vaciar la cola:", cola.verCuantosHay())
print("Frente después de desencolar:", cola.verFrente())
print("Cantidad de elementos después de desencolar:", cola.verCuantosHay())
cola.encolar(4)
print("Frente después de encolar 4:", cola.verFrente())
print("Cantidad de elementos después de encolar 4:", cola.verCuantosHay())

class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return len(self.items) == 0

    def apilarRegistrar(self, item):
        self.items.append(item)

    def desapilarDeshacer(self):
        if self.estaVacia():
            return None
        #Devolver recurso a disponible
        return self.items.pop()

    def verTopeUltimaOperacion(self):
        if self.estaVacia():
            return None
        return self.items[-1]

    def verCuantosHay(self):
        return len(self.items)

"""

Preguntas

1. Si se elimina el ultimo elemento de una cola en una lista enlazada se debe actualizar el frente y final de la fila
porque asi la cola queda sin referencias a nodos que ya no existen.

2. Si en una cola circular de capacidad cinco el frente esta en tres y hay cuatro elementos la siguiente posicion se guarda en dos.
porque se usa la siguiente formula (frente + cantidad) % capacidad

3. Si se quieren deshacer tres ultimas operaciones se usa una pila porque se puede usar pop para borrar los ultimos elementos agregados.

4. Para atender por orden de llegada se usa una cola por el FIFO (First In, First Out)

"""