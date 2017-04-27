class Personaje:
    id=''
    vida=100
    recuperacion=0
    agilidad=0

    def __init__(self,nombre):
        self.id=nombre

    #Se llama desde gestor de duelos
    def refrescaCiclo(self):
        self.aumentaVida(self.recuperacion)

    def restaVida(self,cantidad):
        if cantidad > self.vida:
            self.vida=0
        else:
            self.vida-=cantidad

    def aumentaVida(self,cantidad):
        self.vida+=cantidad

    def getAgilidad(self):
        return self.agilidad

    def getVida(self):
        return self.vida

    def getNombre(self):
        return self.id