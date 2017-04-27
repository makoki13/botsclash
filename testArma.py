import clsArma

x = clsArma.Arma("Enola Gay",2,5)
print (x.getNombre())
print (x.getDanyo())

for i in range(30):
    print ("{}{}".format("Ciclos pendientes disparo: ", x.getCiclosRecargaPendientes()))
    if x.puedeDisparar(): print ("PUEDE DISPARAR") 
    else: print ("NO PUEDE DISPARAR")
    print ("{}{}".format("Munición: ", x.getMunicion()))
    x.refrescaCiclo()
