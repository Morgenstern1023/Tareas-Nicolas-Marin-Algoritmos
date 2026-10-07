#Momento 1

class TablaHash:
    def __init__(self, capacidad=8):
        self.cap = capacidad
        self.cubetas = [[] for _ in range(self.cap)]
        self.n=0
    def hash(self, clave):
        h = 0
        for c in str(clave):
            h = (h * 31 + ord(c)) % self.cap
        return h
    def insertar(self, clave, valor):
        i = self.hash(clave)
        for par in self.cubetas[i]:
            if par[0] == clave:
                par[1] = valor          # ACTUALIZA, no duplica
                return
        self.cubetas[i].append([clave, valor])
        self.n += 1
    def buscar(self, clave):
        i = self.hash(clave)
        for k, v in self.cubetas[i]:    # recorre SOLO esa cubeta
            if k == clave:
                return v
        return None
    def eliminar(self, clave):
        i = self.hash(clave)
        for idx, (k, _) in enumerate(self.cubetas[i]):
            if k == clave:
                self.cubetas[i].pop(idx)
                self.n -= 1
                return True
        return False
    def factorCarga(self):
        return self.n / self.cap

    def mostrarDistribucion(self):
        for i, cubeta in enumerate(self.cubetas):
            print(f"Cubeta {i}: {cubeta}")
        print(f"Factor de carga: {self.factorCarga()}")

    def colisiones(self):
        colisiones = {}
        for i, cubeta in enumerate(self.cubetas):
            if len(cubeta) > 1:
                colisiones[i] = cubeta
        return colisiones

tabla = TablaHash()
tabla.insertar("REC-001",tabla.hash("REC-001"))
tabla.insertar("REC-002",tabla.hash("REC-002"))
tabla.insertar("REC-003",tabla.hash("REC-003"))
tabla.insertar("EQ-100",tabla.hash("EQ-100"))
tabla.insertar("EQ-101",tabla.hash("EQ-101"))
tabla.insertar("PA-007",tabla.hash("PA-007"))
tabla.insertar("PA-008",tabla.hash("PA-008"))
tabla.insertar("EST-42",tabla.hash("EST-42"))

tabla.mostrarDistribucion()
print(tabla.buscar("REC-001"))
print(tabla.buscar("NO-EXISTE"))
tabla.eliminar("REC-001")
tabla.insertar("REC-0001",tabla.hash("REC-0001"))
print(tabla.buscar("REC-0001"))
print(tabla.buscar("REC-001"))
tabla.eliminar("REC-002")
tabla.mostrarDistribucion()
print("Colisiones:", tabla.colisiones())

        



