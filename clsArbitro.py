class Arbitro:
    def __init__(self):
        self.personajes = []
        self.primer_jugador = ''
        self.segundo_jugador = ''

    def addJugador(self, jugador):
        "Añade un personaje a la lista"
        self.personajes.append(jugador)
        return

    def setPrimerJugador(self):
        agilidad1 = self.personajes[0].getAgilidad()
        agilidad2 = self.personajes[1].getAgilidad()
        if agilidad2 > agilidad1:
            self.primer_jugador = self.personajes[1]
            self.segundo_jugador = self.personajes[0]
        else:
            self.primer_jugador = self.personajes[0]
            self.segundo_jugador = self.personajes[1]
        return

    def getPrimerJugador(self):
        return self.primer_jugador

    def ejecuta(self):
        '''
        pendiente de implmenetar
        Mientras algun jugador siga vivo:
        primero conseguimos el daño del primer jugador
        se lo aplicamos al segundo jugador
        si el segundo jugador tiene vida cero declaramos ganador al primer jugador
        sino conseguimos el daño del segundo jugador
        se lo aplicamos al primer jugador
        si el primer jugador tiene vida cero declaramos ganador al segundo jugador
        '''

        return self.primer_jugador #eso se cambiará por el jugador que realmente gane
