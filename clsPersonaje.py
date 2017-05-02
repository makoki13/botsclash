class Personaje:    
    def __init__(self, nombre, vida, recuperacion, agilidad):
        self.id = nombre
        self.vida = vida
        self.recuperacion = recuperacion
        self.agilidad = agilidad

        self.armas = []
        self.defensas = []

    def addArma(self,arma):
        self.armas.append(arma)
        return 

    def addDefensa(self,defensa):
        self.defensas.append(defensa)
        return

    #Se llama desde gestor de duelos
    def generaDanyo(self):
        '''
        pendiente de implementar:
        decide que arma tiene mas daño y devuelve su cantidad
        '''
        return 0

    def recibeDanyo(self,cantidad):
        '''
        pendiente de implementar:
        si hay una defensa cuyo valor defensa es mayor que cantidad entonces se resta esa cantidad
        si no la hay se coge la defensa con mayor defensa , se pone a cero y la diferencia de daño se resta a la vida del personaje
        '''        
        return

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