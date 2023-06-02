from Casilla import *
lista=[]
lista.append(Casilla("tomas Bascope"))
lista.append(Casilla("Paola Uzeda"))
lista.append(Casilla("Andres"))
lista.append(Casilla("Bravo"))

for i in range(0,4):
    print(lista[i].getnCalle())
    