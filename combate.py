import clsArbitro
import clsPersonaje

def main():
    arbitro = clsArbitro.Arbitro()

    #Definimos el primer personaje
    personaje1 = clsPersonaje.Personaje("Makoki", 20, 0, 2)
    
    #definimos el segundo personaje
    personaje2 = clsPersonaje.Personaje("Ausias", 15, 0, 3)
 
    arbitro.addJugador(personaje1)
    arbitro.addJugador(personaje2)

    arbitro.setPrimerJugador()
    primerJugador = arbitro.getPrimerJugador()
    print ("{}{}".format("El primer jugador es: ", primerJugador.getNombre()))

    ganador = arbitro.ejecuta()

    print ("{}{}".format("El resultado es: ", ganador.getNombre()))

main()