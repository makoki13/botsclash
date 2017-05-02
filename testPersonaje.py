import clsPersonaje

x = clsPersonaje.Personaje("Makoki", 20 , 1, 4)
print (x.getNombre())
print (x.getVida())
x.aumentaVida(20)
print (x.getVida())
x.restaVida(50)
print (x.getVida())
print ("{}{}".format("Agilidad: ", x.getAgilidad()))