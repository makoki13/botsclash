class Defensa:
    id = ''
    defensa = 10
    ciclosVida=-1

    def __init__(self,nombre,defensa,ciclosVida):
        self.id=nombre
        self.defensa = defensa
        self.ciclosVida = ciclosVida

    #Se llama desde gestor de duelos
    def refrescaCiclo(self):
        if self.ciclosVida > 0: self.ciclosVida -= 1

    def absorbeDanyo(self,cantidad):
        if cantidad > self.defensa:
            self.defensa=0
        else:
            self.defensa-=cantidad

    def getVida(self):
        return self.ciclosVida

    def getDefensa(self):
        return self.defensa

    def getNombre(self):
        return self.id