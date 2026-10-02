
class listaEnlazada:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None

    def __init__(self):
        self.tope = None

    def apilar(self, x):
        nuevoNodo = self.Nodo(x)
        nuevoNodo.siguiente = self.tope
        self.tope = nuevoNodo

    def desapilar(self):
        if self.tope is None:
            return None
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        return valor

    def cima(self):
        if self.tope is None:
            return None
        return self.tope.valor

    def vacia(self):
        return self.tope is None

def calculadora(expresion):
    pila = listaEnlazada()
    for caracter in expresion.split():
        if caracter in "+-*/^r":
            b = pila.desapilar()
            a = pila.desapilar()
            if caracter == "+":
                pila.apilar(a + b)
            elif caracter == "-":
                pila.apilar(a - b)
            elif caracter == "*":
                pila.apilar(a * b)
            elif caracter == "/":
                pila.apilar(a / b)
            elif caracter == "^":
                pila.apilar(a ** b)
            elif caracter == "r":
                pila.apilar(a ** (1 / b))
        else:
            pila.apilar(int(caracter))
    return pila.desapilar()

def conversorDecimalasexagecimal(numero):
    if numero == 0:
        return "0"
    if numero > 0 and numero < 60:
        return str(numero) + "''"
    if numero >= 60:
        minutos = numero // 60
        segundos = numero % 60
        return str(minutos) + "'" + str(segundos) + "''"
    if numero >= 3600:
        horas = numero // 3600
        minutos = (numero % 3600) // 60
        segundos = numero % 60
        return str(horas) + "h " + str(minutos) + "'" + str(segundos) + "''"

    return ""

def conversordecimalaSexagecimalPila(numero):
    pila = listaEnlazada()
    while numero > 0:
        pila.apilar(numero % 60)
        numero //= 60
    resultado = ""
    while not pila.vacia():
        valor = pila.desapilar()
        if pila.vacia():
            resultado += str(valor) + "''"
        elif pila.cima() is None:
            resultado += str(valor) + "'"
        else:
            resultado += str(valor) + "'"
    return resultado
