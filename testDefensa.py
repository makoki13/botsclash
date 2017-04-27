import clsDefensa

x = clsDefensa.Defensa("Escudo",20,5)
print (x.getNombre())
for i in range(10):
    print ("{}{}{}{}".format("Defensa: ", x.getDefensa(), " * Vida: ", x.getVida()))
    x.refrescaCiclo()
    x.absorbeDanyo(5)