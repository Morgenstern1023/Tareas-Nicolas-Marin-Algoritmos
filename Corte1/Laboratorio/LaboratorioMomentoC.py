class PuntoAcopio:
    def __init__(self, barrio, codigo, pesoTotal):
        self.barrio = barrio
        self.codigo = codigo
        self.pesoTotal = pesoTotal

    def registrarRecoleccion(self, peso):
        self.pesoTotal += peso

    def superaMeta(self, meta):
        return self.pesoTotal > meta

    def describir(self):
        return f"Punto de Acopio - Barrio: {self.barrio}, Código: {self.codigo}, Peso Total: {self.pesoTotal} kg"

class MaterialEspecial(PuntoAcopio):
    def __init__(self, barrio, codigo, pesoTotal, tipoMaterial):
        super().__init__(barrio, codigo, pesoTotal)
        self.tipoMaterial = tipoMaterial

    def describir(self):
        return f"Material Especial - Barrio: {self.barrio}, Código: {self.codigo}, Peso Total: {self.pesoTotal} kg, Tipo de Material: {self.tipoMaterial}"