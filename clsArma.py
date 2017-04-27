class Arma:
    id=''
    danyo=100
    ciclosRecarga=1
    ciclosVida=-1    
    ciclosRecargaPendientes=0

    def __init__(self,nombre,ciclosRecarga,ciclosVida):
        self.id=nombre
        self.ciclosRecarga = ciclosRecarga
        self.ciclosVida = ciclosVida

    def dispara(self):
        if self.ciclosVida!=-1:
            if self.ciclosVida > 0: self.ciclosVida-=1
        self.initCiclosRecarga()
        return self.getDanyo()
    
    #Se llama desde gestor de duelos
    def refrescaCiclo(self):
        if self.puedeDisparar(): self.dispara()
        else: 
            if self.ciclosRecargaPendientes>0: self.ciclosRecargaPendientes-=1
        

    def getDanyo(self):
        return self.danyo

    def initCiclosRecarga(self):
        self.ciclosRecargaPendientes = self.ciclosRecarga

    def puedeDisparar(self):
        if self.ciclosVida == 0: return False
        return self.ciclosRecargaPendientes == 0

    def getNombre(self):
        return self.id

    def getCiclosRecargaPendientes(self): return self.ciclosRecargaPendientes

    def getMunicion(self):
        return self.ciclosVida