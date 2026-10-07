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
    def hash_mala(self, clave): #Solo suma los cuatro primeros caracteres de la clave
        h = 0
        for c in str(clave)[:4]:
            h = (h + ord(c)) % self.cap
        return h
    def insertar(self, clave, valor):
        i = self.hash(clave)
        for par in self.cubetas[i]:
            if par[0] == clave:
                par[1] = valor          # ACTUALIZA, no duplica
                return
        self.cubetas[i].append([clave, valor])
        self.n += 1
        if self.factorCarga() > 0.75:
            self.redimensionar()
    def buscar(self, clave):
        i = self.hash(clave)
        for k, v in self.cubetas[i]:    # recorre SOLO esa cubeta
            if k == clave:
                return v
        return None
    def buscarHashMala(self, clave):
        i = self.hash_mala(clave)
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

    def mostrarDistribucion(self):#Sin mostrar la clave y 
        for i, cubeta in enumerate(self.cubetas):
            print(f"Cubeta {i}: {[v for k, v in cubeta]}")
        print(f"Factor de carga: {self.factorCarga()}")

    def colisiones(self):
        colisiones = {}
        for i, cubeta in enumerate(self.cubetas):
            if len(cubeta) > 1:
                colisiones[i] = cubeta
        return colisiones

    def redimensionar(self):
        viejas = self.cubetas
        self.cap *= 2
        self.cubetas = [[] for _ in range(self.cap)]
        self.n = 0
        for cubeta in viejas:
            for clave, valor in cubeta:
                self.insertar(clave, valor)

    def cubetaMasLlena(self):
        max_len = 0
        max_idx = -1
        for i, cubeta in enumerate(self.cubetas):
            if len(cubeta) > max_len:
                max_len = len(cubeta)
                max_idx = i
        return max_idx, max_len

    def cubetasVacias(self):
        vacias = []
        for i, cubeta in enumerate(self.cubetas):
            if len(cubeta) == 0:
                vacias.append(i)
        return vacias

    # EST-2026-0101 Ana Torres EST-2026-0107 Pedro Ruiz EST-2026-0102 
    # Carlos Rojas EST-2026-0108 Camila Diaz EST-2026-0103 Diego Pardo EST-2026-0109 Luis Herrera EST-2026-0104 
    # Sofia Mejia EST-2026-0110 Valentina Cruz EST-2026-0105 Juan Gomez EST-2026-0111 Andres Vega EST-2026-0106 
    # Maria Lopez EST-2026-0112 Laura Castro

tabla = TablaHash()
tabla.insertar("EST-2026-0101", "Ana Torres")
tabla.insertar("EST-2026-0102", "Carlos Rojas")
tabla.insertar("EST-2026-0103", "Diego Pardo")
tabla.insertar("EST-2026-0104", "Sofia Mejia")
tabla.insertar("EST-2026-0105", "Juan Gomez")
tabla.insertar("EST-2026-0106", "Maria Lopez")
tabla.insertar("EST-2026-0107", "Pedro Ruiz")
tabla.insertar("EST-2026-0108", "Camila Diaz")
tabla.insertar("EST-2026-0109", "Luis Herrera")
tabla.insertar("EST-2026-0110", "Valentina Cruz")
tabla.insertar("EST-2026-0111", "Andres Vega")
tabla.insertar("EST-2026-0112", "Laura Castro")

print(tabla.buscar("EST-2026-0107"))  

tabla.mostrarDistribucion()

print("Cubeta más llena:", tabla.cubetaMasLlena())
print("Cubetas vacías:", tabla.cubetasVacias())

print("Buscar con hash mala:", tabla.buscarHashMala("EST-2026-0107"))
