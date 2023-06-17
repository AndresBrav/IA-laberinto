import cv2
from Casilla import *
lista=[]
sucre=Casilla('Sucre',50,1)
bascope=Casilla("Bascope",50,2)
Perez1=Casilla("Perez1",45,1)
Perez2=Casilla("Perez2",45,1)
Perez3=Casilla("Perez3",45,1)
Perez4=Casilla("Perez4",45,1)
Lopez1=Casilla("Lopez1",75,1)
Frias=Casilla("Frias",45,1)
Gotham1=Casilla("Gotham1",45,1)
Gotham2=Casilla("Gotham2",45,1)
Gotham3=Casilla("Gotham3",45,1)
Gotham4=Casilla("Gotham4",45,1)
Gotham5=Casilla("Gotham5",45,1)
Gotham6=Casilla("Gotham6",45,1)


Acacia1=Casilla("Acacia1",45,1)
Acacia2=Casilla("Acacia2",45,1)
Acacia3=Casilla("Acacia3",45,1)
Acacia4=Casilla("Acacia4",45,1)
Acacia5=Casilla("Acacia5",45,1)

Esquina1=Casilla("Esquina1",45,1)
Esquina2=Casilla("Esquina2",45,1)
Carnaby1=Casilla("Carnaby1",45,1)
Carnaby2=Casilla("Carnaby2",45,1)
Carnaby3=Casilla("Carnaby3",45,1)
Carnaby4=Casilla("Carnaby4",45,1)

Acme1=Casilla("Acme1",45,1)
Acme2=Casilla("Acme2",45,1)
Acme3=Casilla("Acme3",45,1)

B11=Casilla("B11",45,1)
B12=Casilla("B12",45,1)
B13=Casilla("B13",45,1)

Elm=Casilla("Elm",45,1)

Elmwood1=Casilla("Elmwood1",45,1)
Elmwood2=Casilla("Elmwood2",45,1)
Elmwood3=Casilla("Elmwood3",45,1)
Elmwood4=Casilla("Elmwood4",45,1)

Bourbon1=Casilla("Bourbon1",45,1)
Bourbon2=Casilla("Bourbon2",45,1)
Bourbon3=Casilla("Bourbon3",45,1)
Bourbon4=Casilla("Bourbon4",45,1)
Bourbon5=Casilla("Bourbon5",45,1)

Baker1=Casilla("Baker1",45,1)
Baker2=Casilla("Baker2",45,1)
Baker3=Casilla("Baker3",45,1)
Baker4=Casilla("Baker4",45,1)
Melrose1=Casilla("Melrose1",45,1)
Melrose2=Casilla("Melrose2",45,1)
Melrose3=Casilla("Melrose3",45,1)
Melrose4=Casilla("Melrose4",45,1)
Southpark1=Casilla("Southpark1",45,1)
Southpark2=Casilla("Southpark2",45,1)
Southpark3=Casilla("Southpark3",45,1)
Southpark4=Casilla("Southpark4",45,1)
Southpark5=Casilla("Southpark5",45,1)
Southpark6=Casilla("Southpark6",45,1)
Southpark7=Casilla("Southpark7",45,1)
Southpark8=Casilla("Southpark8",45,1)
B21=Casilla("B21",45,1)
B22=Casilla("B22",45,1)
B23=Casilla("B23",45,1)
Wallstreet1=Casilla("Wallstreet1",45,1)
Wallstreet2=Casilla("Wallstreet2",45,1)
Wallstreet3=Casilla("Wallstreet3",45,1)
Wallstreet4=Casilla("Wallstreet4",45,1)
Wallstreet5=Casilla("Wallstreet5",45,1)
A11=Casilla("A11",45,1)
A21=Casilla("A21",45,1)
Arkham1=Casilla("Arkham1",45,1)
Arkham2=Casilla("Arkham2",45,1)
Arkham3=Casilla("Arkham3",45,1)
Foster1=Casilla("Foster1",45,1)
Foster2=Casilla("Foster2",45,1)
Piedradura1=Casilla("Piedradura1",45,1)
Piedradura2=Casilla("Piedradura2",45,1)
Piedradura3=Casilla("Piedradura3",45,1)
Nogal1=Casilla("Nogal1",45,1)
Nogal2=Casilla("Nogal2",45,1)
Nogal3=Casilla("Nogal3",45,1)
Nogal4=Casilla("Nogal4",45,1)
C1=Casilla("C1",45,1)
C2=Casilla("C2",45,1)
C3=Casilla("C3",45,1)
Mar1=Casilla("Mar1",45,1)
Mar2=Casilla("Mar2",45,1)
Mar3=Casilla("Mar3",45,1)
Olmos1=Casilla("Olmos1",45,1)
Olmos2=Casilla("Olmos2",45,1)
Olmos3=Casilla("Olmos3",45,1)
Olmos4=Casilla("Olmos4",45,1)
Olmos5=Casilla("Olmos5",45,1)
Siempreviva1=Casilla("Siempreviva1",45,1)
Siempreviva2=Casilla("Siempreviva2",45,1)
Siempreviva3=Casilla("Siempreviva3",45,1)
Siempreviva4=Casilla("Siempreviva4",45,1)
Metroville1=Casilla("Metroville1",45,1)
Metroville2=Casilla("Metroville2",45,1)
Coronado1=Casilla("Coronado1",45,1)
Coronado2=Casilla("Coronado2",45,1)
Coronado3=Casilla("Coronado3",45,1)
Coronado4=Casilla("Coronado4",45,1)
Coronado5=Casilla("Coronado5",45,1)

Salero1=Casilla("Salero1",45,1)
Salero2=Casilla("Salero2",45,1)
Salero3=Casilla("Salero3",45,1)
Nintendo1=Casilla("Nintendo1",45,1)
Nintendo2=Casilla("Nintendo2",45,1)
Nintendo3=Casilla("Nintendo3",45,1)
AbbeyRoad1=Casilla("AbbeyRoad1",45,1)
AbbeyRoad2=Casilla("AbbeyRoad2",45,1)
AbbeyRoad3=Casilla("AbbeyRoad3",45,1)
AbbeyRoad4=Casilla("AbbeyRoad4",45,1)
AbbeyRoad5=Casilla("AbbeyRoad5",45,1)
AbbeyRoad6=Casilla("AbbeyRoad6",45,1)
AbbeyRoad7=Casilla("AbbeyRoad7",45,1)
Elmwood21=Casilla("Elmwood21",45,1)
Elmwood22=Casilla("Elmwood22",45,1)
Elmwood23=Casilla("Elmwood23",45,1)
Elmwood24=Casilla("Elmwood24",45,1)
Peachtree1=Casilla("Peachtree1",45,1)
Peachtree2=Casilla("Peachtree2",45,1)
Peachtree3=Casilla("Peachtree3",45,1)
Peachtree4=Casilla("Peachtree4",45,1)
Peachtree5=Casilla("Peachtree5",45,1)
Peachtree6=Casilla("Peachtree6",45,1)
Peachtree7=Casilla("Peachtree7",45,1)
Luna=Casilla("Luna",45,1)
Luz=Casilla("Luz",45,1)
D1=Casilla("D1",45,1)
Vida=Casilla("Vida",45,1)
Nube1=Casilla("Nube1",45,1)
Nube2=Casilla("Nube2",45,1)
Alba=Casilla("Alba",45,1)
Brisa1=Casilla("Brisa1",45,1)
Brisa2=Casilla("Brisa2",45,1)
Aroma1=Casilla("Aroma1",45,1)
Aroma2=Casilla("Aroma2",45,1)
Aroma3=Casilla("Aroma3",45,1)
Aroma4=Casilla("Aroma4",45,1)
Aroma5=Casilla("Aroma5",45,1)
Aroma6=Casilla("Aroma6",45,1)
Aroma7=Casilla("Aroma7",45,1)
Aroma8=Casilla("Aroma8",45,1)
Elmore1=Casilla("Elmore1",45,1)
Elmore2=Casilla("Elmore2",45,1)
Elmore3=Casilla("Elmore3",45,1)
Elmore4=Casilla("Elmore4",45,1)
Elmore5=Casilla("Elmore5",45,1)
Elmore6=Casilla("Elmore6",45,1)
Elmore7=Casilla("Elmore7",45,1)
Elmore8=Casilla("Elmore8",45,1)
Elmore9=Casilla("Elmore9",45,1)
Elmore10=Casilla("Elmore10",45,1)
Elmore11=Casilla("Elmore11",45,1)
Elmore12=Casilla("Elmore11",45,1)
Springfield1=Casilla("Springfield1",45,1)
Springfield2=Casilla("Springfield2",45,1)
Springfield3=Casilla("Springfield3",45,1)
Springfield4=Casilla("Springfield4",45,1)
Springfield5=Casilla("Springfield5",45,1)
Springfield6=Casilla("Springfield6",45,1)
Springfield7=Casilla("Springfield7",45,1)
Springfield8=Casilla("Springfield8",45,1)
Springfield9=Casilla("Springfield9",45,1)
Springfield10=Casilla("Springfield10",45,1)
Springfield11=Casilla("Springfield11",45,1)
Springfield12=Casilla("Springfield12",45,1)
Springfield13=Casilla("Springfield13",45,1)
Springfield14=Casilla("Springfield14",45,1)
Springfield15=Casilla("Springfield15",45,1)
Springfield16=Casilla("Springfield16",45,1)
Millaverde1=Casilla("Millaverde1",45,1)
Millaverde2=Casilla("Millaverde2",45,1)
Millaverde3=Casilla("Millaverde3",45,1)
Millaverde4=Casilla("Millaverde4",45,1)
Millaverde5=Casilla("Millaverde5",45,1)
Millaverde6=Casilla("Millaverde6",45,1)
Millaverde7=Casilla("Millaverde7",45,1)
Millaverde8=Casilla("Millaverde8",45,1)
CSol=Casilla("CSol",45,1)
"""Seccion Loida"""


def cargarGrafico(listaRecorrido):
    img=cv2.imread("IA proyecto/mapaIA5.jpg")
    lista=listaRecorrido
    dist=0
    tiempo=0
    
    try:
        if "Sucre" in lista:
                Sucre(img) #se dibuja en la imgen
                dist=dist+sucre.getDistancia() # suma distancias
                tiempo=tiempo+sucre.getTRecorrido() #suma el tiempo de recorrido

        if "Bascope" in lista:
            Bascope(img)
            dist=dist+bascope.getDistancia()
            tiempo=tiempo+bascope.getTRecorrido()
        if "Perez1" in lista:
            perez1(img)
            dist=dist+Perez1.getDistancia()
            tiempo=tiempo+Perez1.getTRecorrido()
        if "Perez2" in lista:
            perez2(img)
            dist=dist+Perez2.getDistancia()
            tiempo=tiempo+Perez2.getTRecorrido()

        if "Perez3" in lista:
            perez3(img)
            dist=dist+Perez3.getDistancia()
            tiempo=tiempo+Perez3.getTRecorrido()
        if "Perez4" in lista:
            perez1(img)
            dist=dist+Perez4.getDistancia()
            tiempo=tiempo+Perez4.getTRecorrido()
        if "Lopez1" in lista:
            lopez1(img)
            dist=dist+Lopez1.getDistancia()
            tiempo=tiempo+Lopez1.getTRecorrido()

        if "Frias" in lista:
            frias(img)
            dist=dist+Frias.getDistancia()
            tiempo=tiempo+Frias.getTRecorrido()

        """Seccion de victor"""  
             
        if "Gotham1" in lista:
            gotham1(img)
            dist = dist + Gotham1.getDistancia()
            tiempo = tiempo + Gotham1.getTRecorrido()
        if "Gotham2" in lista:
            gotham2(img)
            dist = dist + Gotham2.getDistancia()
            tiempo = tiempo + Gotham2.getTRecorrido()
        if "Gotham3" in lista:
            gotham3(img)
            dist = dist + Gotham3.getDistancia()
            tiempo = tiempo + Gotham3.getTRecorrido()

        if "Gotham4" in lista:
            gotham4(img)
            dist = dist + Gotham4.getDistancia()
            tiempo = tiempo + Gotham4.getTRecorrido()

        if "Gotham5" in lista:
            gotham5(img)
            dist = dist + Gotham5.getDistancia()
            tiempo = tiempo + Gotham5.getTRecorrido()

        if "Gotham6" in lista:
            gotham6(img)
            dist = dist + Gotham6.getDistancia()
            tiempo = tiempo + Gotham6.getTRecorrido()

        if "Acacia1" in lista:
            acacia1(img)
            dist = dist + Acacia1.getDistancia()
            tiempo = tiempo + Acacia1.getTRecorrido()

        if "Acacia2" in lista:
            acacia2(img)
            dist = dist + Acacia2.getDistancia()
            tiempo = tiempo + Acacia2.getTRecorrido()
        
        if "Acacia3" in lista:
            acacia3(img)
            dist = dist + Acacia3.getDistancia()
            tiempo = tiempo + Acacia3.getTRecorrido()

        if "Acacia4" in lista:
            acacia4(img)
            dist = dist + Acacia4.getDistancia()
            tiempo = tiempo + Acacia4.getTRecorrido()

        if "Acacia5" in lista:
            acacia5(img)
            dist = dist + Acacia5.getDistancia()
            tiempo = tiempo + Acacia5.getTRecorrido()

        if "Esquina1" in lista:
            esquina1(img)
            dist = dist + Esquina1.getDistancia()
            tiempo = tiempo + Esquina1.getTRecorrido()

        if "Esquina2" in lista:
            esquina2(img)
            dist = dist + Esquina2.getDistancia()
            tiempo = tiempo + Esquina2.getTRecorrido()

        if "Carnaby1" in lista:
            carnaby1(img)
            dist = dist + Carnaby1.getDistancia()
            tiempo = tiempo + Carnaby1.getTRecorrido()
            
        if "Carnaby2" in lista:
            carnaby2(img)
            dist = dist + Carnaby2.getDistancia()
            tiempo = tiempo + Carnaby2.getTRecorrido()

        if "Carnaby3" in lista:
            carnaby3(img)
            dist = dist + Carnaby3.getDistancia()
            tiempo = tiempo + Carnaby3.getTRecorrido()

        if "Carnaby4" in lista:
            carnaby4(img)
            dist = dist + Carnaby4.getDistancia()
            tiempo = tiempo + Carnaby4.getTRecorrido()

        if "Acme1" in lista:
            acme1(img)
            dist = dist + Acme1.getDistancia()
            tiempo = tiempo + Acme1.getTRecorrido()

        if "Acme2" in lista:
            acme2(img)
            dist = dist + Acme2.getDistancia()
            tiempo = tiempo + Acme2.getTRecorrido()

        if "Acme3" in lista:
            acme3(img)
            dist = dist + Acme3.getDistancia()
            tiempo = tiempo + Acme3.getTRecorrido()

        if "B11" in lista:
            b11(img)
            dist = dist + B11.getDistancia()
            tiempo = tiempo + B11.getTRecorrido()

        if "B12" in lista:
            b12(img)
            dist = dist + B12.getDistancia()
            tiempo = tiempo + B12.getTRecorrido()

        if "B13" in lista:
            b13(img)
            dist = dist + B13.getDistancia()
            tiempo = tiempo + B13.getTRecorrido()

        if "Elm" in lista:
            elm(img)
            dist = dist + Elm.getDistancia()
            tiempo = tiempo + Elm.getTRecorrido()

        if "Elmwood1" in lista:
            elmwood1(img)
            dist = dist + Elmwood1.getDistancia()
            tiempo = tiempo + Elmwood1.getTRecorrido()

        if "Elmwood2" in lista:
            elmwood2(img)
            dist = dist + Elmwood2.getDistancia()
            tiempo = tiempo + Elmwood2.getTRecorrido()

        if "Elmwood3" in lista:
            elmwood3(img)
            dist = dist + Elmwood3.getDistancia()
            tiempo = tiempo + Elmwood3.getTRecorrido()

        if "Elmwood4" in lista:
            elmwood4(img)
            dist = dist + Elmwood4.getDistancia()
            tiempo = tiempo + Elmwood4.getTRecorrido()

        if "Bourbon1" in lista:
            bourbon1(img)
            dist = dist + Bourbon1.getDistancia()
            tiempo = tiempo + Bourbon1.getTRecorrido()

        if "Bourbon2" in lista:
            bourbon2(img)
            dist = dist + Bourbon2.getDistancia()
            tiempo = tiempo + Bourbon2.getTRecorrido()

        if "Bourbon3" in lista:
            bourbon3(img)
            dist = dist + Bourbon3.getDistancia()
            tiempo = tiempo + Bourbon3.getTRecorrido()

        if "Bourbon4" in lista:
            bourbon4(img)
            dist = dist + Bourbon4.getDistancia()
            tiempo = tiempo + Bourbon4.getTRecorrido()

        if "Bourbon5" in lista:
            bourbon5(img)
            dist = dist + Bourbon5.getDistancia()
            tiempo = tiempo + Bourbon5.getTRecorrido()
            
        if "Baker1" in lista:
            baker1(img)
            dist = dist + Baker1.getDistancia()
            tiempo = tiempo + Baker1.getTRecorrido()

        if "Baker2" in lista:
            baker2(img)
            dist = dist + Baker2.getDistancia()
            tiempo = tiempo + Baker2.getTRecorrido()

        if "Baker3" in lista:
            baker3(img)
            dist = dist + Baker3.getDistancia()
            tiempo = tiempo + Baker3.getTRecorrido()

        if "Baker4" in lista:
            baker4(img)
            dist = dist + Baker4.getDistancia()
            tiempo = tiempo + Baker4.getTRecorrido()

        if "Melrose1" in lista:
            melrose1(img)
            dist = dist + Melrose1.getDistancia()
            tiempo = tiempo + Melrose1.getTRecorrido()

        if "Melrose2" in lista:
            melrose2(img)
            dist = dist + Melrose2.getDistancia()
            tiempo = tiempo + Melrose2.getTRecorrido()

        if "Melrose3" in lista:
            melrose3(img)
            dist = dist + Melrose3.getDistancia()
            tiempo = tiempo + Melrose3.getTRecorrido()

        if "Melrose4" in lista:
            melrose4(img)
            dist = dist + Melrose4.getDistancia()
            tiempo = tiempo + Melrose4.getTRecorrido()

        if "Southpark1" in lista:
            southPark1(img)
            dist = dist + Southpark1.getDistancia()
            tiempo = tiempo + Southpark1.getTRecorrido()

        if "Southpark2" in lista:
            southPark2(img)
            dist = dist + Southpark2.getDistancia()
            tiempo = tiempo + Southpark2.getTRecorrido()
            
        if "Southpark3" in lista:
            southPark3(img)
            dist = dist + Southpark3.getDistancia()
            tiempo = tiempo + Southpark3.getTRecorrido()

        if "Southpark4" in lista:
            southPark4(img)
            dist = dist + Southpark4.getDistancia()
            tiempo = tiempo + Southpark4.getTRecorrido()

        if "Southpark5" in lista:
            southPark5(img)
            dist = dist + Southpark5.getDistancia()
            tiempo = tiempo + Southpark5.getTRecorrido()

        if "Southpark6" in lista:
            southPark6(img)
            dist = dist + Southpark6.getDistancia()
            tiempo = tiempo + Southpark6.getTRecorrido()

        if "Southpark7" in lista:
            southPark7(img)
            dist = dist + Southpark7.getDistancia()
            tiempo = tiempo + Southpark7.getTRecorrido()

        if "Southpark8" in lista:
            southPark8(img)
            dist = dist + Southpark8.getDistancia()
            tiempo = tiempo + Southpark8.getTRecorrido()

        if "B21" in lista:
            b21(img)
            dist = dist + B21.getDistancia()
            tiempo = tiempo + B21.getTRecorrido()

        if "B22" in lista:
            b22(img)
            dist = dist + B22.getDistancia()
            tiempo = tiempo + B22.getTRecorrido()

        if "B23" in lista:
            b23(img)
            dist = dist + B23.getDistancia()
            tiempo = tiempo + B23.getTRecorrido()

        if "Wallstreet1" in lista:
            wallStreet1(img)
            dist = dist + Wallstreet1.getDistancia()
            tiempo = tiempo + Wallstreet1.getTRecorrido()

        if "Wallstreet2" in lista:
            wallStreet2(img)
            dist = dist + Wallstreet2.getDistancia()
            tiempo = tiempo + Wallstreet2.getTRecorrido()
        
        if "Wallstreet3" in lista:
            wallStreet3(img)
            dist = dist + Wallstreet3.getDistancia()
            tiempo = tiempo + Wallstreet3.getTRecorrido()

        if "Wallstreet4" in lista:
            wallStreet4(img)
            dist = dist + Wallstreet4.getDistancia()
            tiempo = tiempo + Wallstreet4.getTRecorrido()
            
        if "Wallstreet5" in lista:
            wallStreet5(img)
            dist = dist + Wallstreet5.getDistancia()
            tiempo = tiempo + Wallstreet5.getTRecorrido()

        if "A11" in lista:
            a11(img)
            dist = dist + A11.getDistancia()
            tiempo = tiempo + A11.getTRecorrido()

        if "A21" in lista:
            a21(img)
            dist = dist + A21.getDistancia()
            tiempo = tiempo + A21.getTRecorrido()

        if "Arkham1" in lista:
            arkham1(img)
            dist = dist + Arkham1.getDistancia()
            tiempo = tiempo + Arkham1.getTRecorrido()

        if "Arkham2" in lista:
            arkham2(img)
            dist = dist + Arkham2.getDistancia()
            tiempo = tiempo + Arkham2.getTRecorrido()

        if "Arkham3" in lista:
            arkham3(img)
            dist = dist + Arkham3.getDistancia()
            tiempo = tiempo + Arkham3.getTRecorrido()

        if "Foster1" in lista:
            foster1(img)
            dist = dist + Foster1.getDistancia()
            tiempo = tiempo + Foster1.getTRecorrido()

        if "Foster2" in lista:
            foster2(img)
            dist = dist + Foster2.getDistancia()
            tiempo = tiempo + Foster2.getTRecorrido()
        
        if "Piedradura1" in lista:
            piedradura1(img)
            dist = dist + Piedradura1.getDistancia()
            tiempo = tiempo + Piedradura1.getTRecorrido()

        if "Piedradura2" in lista:
            piedradura2(img)
            dist = dist + Piedradura2.getDistancia()
            tiempo = tiempo + Piedradura2.getTRecorrido()

        if "Piedradura3" in lista:
            piedradura3(img)
            dist = dist + Piedradura3.getDistancia()
            tiempo = tiempo + Piedradura3.getTRecorrido()

        if "Nogal1" in lista:
            nogal1(img)
            dist = dist + Nogal1.getDistancia()
            tiempo = tiempo + Nogal1.getTRecorrido()

        if "Nogal2" in lista:
            nogal2(img)
            dist = dist + Nogal2.getDistancia()
            tiempo = tiempo + Nogal2.getTRecorrido()

        if "Nogal3" in lista:
            nogal3(img)
            dist = dist + Nogal3.getDistancia()
            tiempo = tiempo + Nogal3.getTRecorrido()

        if "Nogal4" in lista:
            nogal4(img)
            dist = dist + Nogal4.getDistancia()
            tiempo = tiempo + Nogal4.getTRecorrido()

        if "C1" in lista:
            c1(img)
            dist = dist + C1.getDistancia()
            tiempo = tiempo + C1.getTRecorrido()

        if "C2" in lista:
            c2(img)
            dist = dist + C2.getDistancia()
            tiempo = tiempo + C2.getTRecorrido()

        if "C3" in lista:
            c3(img)
            dist = dist + C3.getDistancia()
            tiempo = tiempo + C3.getTRecorrido()
            
        if "Mar1" in lista:
            mar1(img)
            dist = dist + Mar1.getDistancia()
            tiempo = tiempo + Mar1.getTRecorrido()

        if "Mar2" in lista:
            mar2(img)
            dist = dist + Mar2.getDistancia()
            tiempo = tiempo + Mar2.getTRecorrido()
        
        if "Mar3" in lista:
            mar3(img)
            dist = dist + Mar3.getDistancia()
            tiempo = tiempo + Mar3.getTRecorrido()

        if "Olmos1" in lista:
            olmos1(img)
            dist = dist + Olmos1.getDistancia()
            tiempo = tiempo + Olmos1.getTRecorrido()

        if "Olmos2" in lista:
            olmos2(img)
            dist = dist + Olmos2.getDistancia()
            tiempo = tiempo + Olmos2.getTRecorrido()

        if "Olmos3" in lista:
            olmos3(img)
            dist = dist + Olmos3.getDistancia()
            tiempo = tiempo + Olmos3.getTRecorrido()

        if "Olmos4" in lista:
            olmos4(img)
            dist = dist + Olmos4.getDistancia()
            tiempo = tiempo + Olmos4.getTRecorrido()

        if "Olmos5" in lista:
            olmos5(img)
            dist = dist + Olmos5.getDistancia()
            tiempo = tiempo + Olmos5.getTRecorrido()

        if "Siempreviva1" in lista:
            siempreviva1(img)
            dist = dist + Siempreviva1.getDistancia()
            tiempo = tiempo + Siempreviva1.getTRecorrido()

        if "Siempreviva2" in lista:
            siempreviva2(img)
            dist = dist + Siempreviva2.getDistancia()
            tiempo = tiempo + Siempreviva2.getTRecorrido()

        if "Siempreviva3" in lista:
            siempreviva3(img)
            dist = dist + Siempreviva3.getDistancia()
            tiempo = tiempo + Siempreviva3.getTRecorrido()

        if "Siempreviva4" in lista:
            siempreviva4(img)
            dist = dist + Siempreviva4.getDistancia()
            tiempo = tiempo + Siempreviva4.getTRecorrido()

        if "Metroville1" in lista:
            metroville1(img)
            dist = dist + Metroville1.getDistancia()
            tiempo = tiempo + Metroville1.getTRecorrido()

        if "Metroville2" in lista:
            metroville2(img)
            dist = dist + Metroville2.getDistancia()
            tiempo = tiempo + Metroville2.getTRecorrido()

        if "Coronado1" in lista:
            coronado1(img)
            dist = dist + Coronado1.getDistancia()
            tiempo = tiempo + Coronado1.getTRecorrido()

        if "Coronado2" in lista:
            coronado2(img)
            dist = dist + Coronado2.getDistancia()
            tiempo = tiempo + Coronado2.getTRecorrido()

        if "Coronado3" in lista:
            coronado3(img)
            dist = dist + Coronado3.getDistancia()
            tiempo = tiempo + Coronado3.getTRecorrido()

        if "Coronado4" in lista:
            coronado4(img)
            dist = dist + Coronado4.getDistancia()
            tiempo = tiempo + Coronado4.getTRecorrido()

        if "Coronado5" in lista:
            coronado5(img)
            dist = dist + Coronado5.getDistancia()
            tiempo = tiempo + Coronado5.getTRecorrido()

        if "Salero1" in lista:
            salero1(img)
            dist = dist + Salero1.getDistancia()
            tiempo = tiempo + Salero1.getTRecorrido()
        if "Salero2" in lista:
            salero2(img)
            dist = dist + Salero2.getDistancia()
            tiempo = tiempo + Salero2.getTRecorrido()
        if "Salero3" in lista:
            salero3(img)
            dist = dist + Salero3.getDistancia()
            tiempo = tiempo + Salero3.getTRecorrido()

        if "Nintendo1" in lista:
            nintendo1(img)
            dist = dist + Nintendo1.getDistancia()
            tiempo = tiempo + Nintendo1.getTRecorrido()

        if "Nintendo2" in lista:
            nintendo2(img)
            dist = dist + Nintendo2.getDistancia()
            tiempo = tiempo + Nintendo2.getTRecorrido()

        if "Nintendo3" in lista:
            nintendo3(img)
            dist = dist + Nintendo3.getDistancia()
            tiempo = tiempo + Nintendo3.getTRecorrido()

        if "AbbeyRoad1" in lista:
            abbeyroad1(img)
            dist = dist + AbbeyRoad1.getDistancia()
            tiempo = tiempo + AbbeyRoad1.getTRecorrido()

        if "AbbeyRoad2" in lista:
            abbeyroad2(img)
            dist = dist + AbbeyRoad2.getDistancia()
            tiempo = tiempo + AbbeyRoad2.getTRecorrido()

        if "AbbeyRoad3" in lista:
            abbeyroad3(img)
            dist = dist + AbbeyRoad3.getDistancia()
            tiempo = tiempo + AbbeyRoad3.getTRecorrido()

        if "AbbeyRoad4" in lista:
            abbeyroad4(img)
            dist = dist + AbbeyRoad4.getDistancia()
            tiempo = tiempo + AbbeyRoad4.getTRecorrido()

        if "AbbeyRoad5" in lista:
            abbeyroad5(img)
            dist = dist + AbbeyRoad5.getDistancia()
            tiempo = tiempo + AbbeyRoad5.getTRecorrido()
            
        if "AbbeyRoad6" in lista:
            abbeyroad6(img)
            dist = dist + AbbeyRoad6.getDistancia()
            tiempo = tiempo + AbbeyRoad6.getTRecorrido()

        if "AbbeyRoad7" in lista:
            abbeyroad7(img)
            dist = dist + AbbeyRoad7.getDistancia()
            tiempo = tiempo + AbbeyRoad7.getTRecorrido()

        if "Elmwood21" in lista:
            elmwood21(img)
            dist = dist + Elmwood21.getDistancia()
            tiempo = tiempo + Elmwood21.getTRecorrido()

        if "Elmwood22" in lista:
            elmwood22(img)
            dist = dist + Elmwood22.getDistancia()
            tiempo = tiempo + Elmwood22.getTRecorrido()

        if "Elmwood23" in lista:
            elmwood23(img)
            dist = dist + Elmwood23.getDistancia()
            tiempo = tiempo + Elmwood23.getTRecorrido()

        if "Elmwood24" in lista:
            elmwood24(img)
            dist = dist + Elmwood24.getDistancia()
            tiempo = tiempo + Elmwood24.getTRecorrido()

        if "Peachtree1" in lista:
            peachtree1(img)
            dist = dist + Peachtree1.getDistancia()
            tiempo = tiempo + Peachtree1.getTRecorrido()

        if "Peachtree2" in lista:
            peachtree2(img)
            dist = dist + Peachtree2.getDistancia()
            tiempo = tiempo + Peachtree2.getTRecorrido()

        if "Peachtree3" in lista:
            peachtree3(img)
            dist = dist + Peachtree3.getDistancia()
            tiempo = tiempo + Peachtree3.getTRecorrido()

        if "Peachtree4" in lista:
            peachtree4(img)
            dist = dist + Peachtree4.getDistancia()
            tiempo = tiempo + Peachtree4.getTRecorrido()

        if "Peachtree5" in lista:
            peachtree5(img)
            dist = dist + Peachtree5.getDistancia()
            tiempo = tiempo + Peachtree5.getTRecorrido()

        if "Peachtree6" in lista:
            peachtree6(img)
            dist = dist + Peachtree6.getDistancia()
            tiempo = tiempo + Peachtree6.getTRecorrido()

        if "Peachtree7" in lista:
            peachtree7(img)
            dist = dist + Peachtree7.getDistancia()
            tiempo = tiempo + Peachtree7.getTRecorrido()

        if "Luna" in lista:
            luna(img)
            dist = dist + Luna.getDistancia()
            tiempo = tiempo + Luna.getTRecorrido()

        if "Luz" in lista:
            luz(img)
            dist = dist + Luz.getDistancia()
            tiempo = tiempo + Luz.getTRecorrido()

        if "D1" in lista:
            d1(img)
            dist = dist + D1.getDistancia()
            tiempo = tiempo + D1.getTRecorrido()

        if "Vida" in lista:
            vida(img)
            dist = dist + Vida.getDistancia()
            tiempo = tiempo + Vida.getTRecorrido()

        if "Nube1" in lista:
            nube1(img)
            dist = dist + Nube1.getDistancia()
            tiempo = tiempo + Nube1.getTRecorrido()

        if "Nube2" in lista:
            nube2(img)
            dist = dist + Nube2.getDistancia()
            tiempo = tiempo + Nube2.getTRecorrido()

        if "Alba" in lista:
            alba(img)
            dist = dist + Alba.getDistancia()
            tiempo = tiempo + Alba.getTRecorrido()

        if "Brisa1" in lista:
            brisa1(img)
            dist = dist + Brisa1.getDistancia()
            tiempo = tiempo + Brisa1.getTRecorrido()
            
        if "Brisa2" in lista:
            brisa2(img)
            dist = dist + Brisa2.getDistancia()
            tiempo = tiempo + Brisa2.getTRecorrido()

        if "Aroma1" in lista:
            aroma1(img)
            dist = dist + Aroma1.getDistancia()
            tiempo = tiempo + Aroma1.getTRecorrido()

        if "Aroma2" in lista:
            aroma2(img)
            dist = dist + Aroma2.getDistancia()
            tiempo = tiempo + Aroma2.getTRecorrido()

        if "Aroma3" in lista:
            aroma3(img)
            dist = dist + Aroma3.getDistancia()
            tiempo = tiempo + Aroma3.getTRecorrido()

        if "Aroma4" in lista:
            aroma4(img)
            dist = dist + Aroma4.getDistancia()
            tiempo = tiempo + Aroma4.getTRecorrido()

        if "Aroma5" in lista:
            aroma5(img)
            dist = dist + Aroma5.getDistancia()
            tiempo = tiempo + Aroma5.getTRecorrido()

        if "Aroma6" in lista:
            aroma6(img)
            dist = dist + Aroma6.getDistancia()
            tiempo = tiempo + Aroma6.getTRecorrido()

        if "Aroma7" in lista:
            aroma7(img)
            dist = dist + Aroma7.getDistancia()
            tiempo = tiempo + Aroma7.getTRecorrido()

        if "Aroma8" in lista:
            aroma8(img)
            dist = dist + Aroma8.getDistancia()
            tiempo = tiempo + Aroma8.getTRecorrido()

        if "Elmore1" in lista:
            elmore1(img)
            dist = dist + Elmore1.getDistancia()
            tiempo = tiempo + Elmore1.getTRecorrido()

        if "Elmore2" in lista:
            elmore2(img)
            dist = dist + Elmore2.getDistancia()
            tiempo = tiempo + Elmore2.getTRecorrido()

        if "Elmore3" in lista:
            elmore3(img)
            dist = dist + Elmore3.getDistancia()
            tiempo = tiempo + Elmore3.getTRecorrido()

        if "Elmore4" in lista:
            elmore4(img)
            dist = dist + Elmore4.getDistancia()
            tiempo = tiempo + Elmore4.getTRecorrido()

        if "Elmore5" in lista:
            elmore5(img)
            dist = dist + Elmore5.getDistancia()
            tiempo = tiempo + Elmore5.getTRecorrido()

        if "Elmore6" in lista:
            elmore6(img)
            dist = dist + Elmore6.getDistancia()
            tiempo = tiempo + Elmore6.getTRecorrido()

        if "Elmore7" in lista:
            elmore7(img)
            dist = dist + Elmore7.getDistancia()
            tiempo = tiempo + Elmore7.getTRecorrido()

        if "Elmore8" in lista:
            elmore8(img)
            dist = dist + Elmore8.getDistancia()
            tiempo = tiempo + Elmore8.getTRecorrido()

        if "Elmore9" in lista:
            elmore9(img)
            dist = dist + Elmore9.getDistancia()
            tiempo = tiempo + Elmore9.getTRecorrido()

        if "Elmore10" in lista:
            elmore10(img)
            dist = dist + Elmore10.getDistancia()
            tiempo = tiempo + Elmore10.getTRecorrido()

        if "Elmore11" in lista:
            elmore11(img)
            dist = dist + Elmore11.getDistancia()
            tiempo = tiempo + Elmore11.getTRecorrido()
        
        if "Elmore12" in lista:
            elmore12(img)
            dist = dist + Elmore12.getDistancia()
            tiempo = tiempo + Elmore12.getTRecorrido()
            
        if "Springfield1" in lista:
            springfield1(img)
            dist = dist + Springfield1.getDistancia()
            tiempo = tiempo + Springfield1.getTRecorrido()

        if "Springfield2" in lista:
            springfield2(img)
            dist = dist + Springfield2.getDistancia()
            tiempo = tiempo + Springfield2.getTRecorrido()

        if "Springfield3" in lista:
            springfield3(img)
            dist = dist + Springfield3.getDistancia()
            tiempo = tiempo + Springfield3.getTRecorrido()

        if "Springfield4" in lista:
            springfield4(img)
            dist = dist + Springfield4.getDistancia()
            tiempo = tiempo + Springfield4.getTRecorrido()

        if "Springfield5" in lista:
            springfield5(img)
            dist = dist + Springfield5.getDistancia()
            tiempo = tiempo + Springfield5.getTRecorrido()

        if "Springfield6" in lista:
            springfield6(img)
            dist = dist + Springfield6.getDistancia()
            tiempo = tiempo + Springfield6.getTRecorrido()

        if "Springfield7" in lista:
            springfield7(img)
            dist = dist + Springfield7.getDistancia()
            tiempo = tiempo + Springfield7.getTRecorrido()

        if "Springfield8" in lista:
            springfield8(img)
            dist = dist + Springfield8.getDistancia()
            tiempo = tiempo + Springfield8.getTRecorrido()

        if "Springfield9" in lista:
            springfield9(img)
            dist = dist + Springfield9.getDistancia()
            tiempo = tiempo + Springfield9.getTRecorrido()

        if "Springfield10" in lista:
            springfield10(img)
            dist = dist + Springfield10.getDistancia()
            tiempo = tiempo + Springfield10.getTRecorrido()

        if "Springfield11" in lista:
            springfield11(img)
            dist = dist + Springfield11.getDistancia()
            tiempo = tiempo + Springfield11.getTRecorrido()

        if "Springfield12" in lista:
            springfield12(img)
            dist = dist + Springfield12.getDistancia()
            tiempo = tiempo + Springfield12.getTRecorrido()

        if "Springfield13" in lista:
            springfield13(img)
            dist = dist + Springfield13.getDistancia()
            tiempo = tiempo + Springfield13.getTRecorrido()

        if "Springfield14" in lista:
            springfield14(img)
            dist = dist + Springfield14.getDistancia()
            tiempo = tiempo + Springfield14.getTRecorrido()

        if "Springfield15" in lista:
            springfield15(img)
            dist = dist + Springfield15.getDistancia()
            tiempo = tiempo + Springfield15.getTRecorrido()

        if "Springfield16" in lista:
            springfield16(img)
            dist = dist + Springfield16.getDistancia()
            tiempo = tiempo + Springfield16.getTRecorrido()

        if "Millaverde1" in lista:
            millaverde1(img)
            dist = dist + Millaverde1.getDistancia()
            tiempo = tiempo + Millaverde1.getTRecorrido()

        if "Millaverde2" in lista:
            millaverde2(img)
            dist = dist + Millaverde2.getDistancia()
            tiempo = tiempo + Millaverde2.getTRecorrido()

        if "Millaverde3" in lista:
            millaverde3(img)
            dist = dist + Millaverde3.getDistancia()
            tiempo = tiempo + Millaverde3.getTRecorrido()

        if "Millaverde4" in lista:
            millaverde4(img)
            dist = dist + Millaverde4.getDistancia()
            tiempo = tiempo + Millaverde4.getTRecorrido()

        if "Millaverde5" in lista:
            millaverde5(img)
            dist = dist + Millaverde5.getDistancia()
            tiempo = tiempo + Millaverde5.getTRecorrido()

        if "Millaverde6" in lista:
            millaverde6(img)
            dist = dist + Millaverde6.getDistancia()
            tiempo = tiempo + Millaverde6.getTRecorrido()

        if "Millaverde7" in lista:
            millaverde7(img)
            dist = dist + Millaverde7.getDistancia()
            tiempo = tiempo + Millaverde7.getTRecorrido()

        if "Millaverde8" in lista:
            millaverde8(img)
            dist = dist + Millaverde8.getDistancia()
            tiempo = tiempo + Millaverde8.getTRecorrido()
        
        if "CSol" in lista:
            sol(img)
            dist = dist + CSol.getDistancia()
            tiempo = tiempo + CSol.getTRecorrido()

        
    except Exception:
        print("problemassssssssssss")
        
    print(dist)
    print(tiempo)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
          
    
def Sucre(img):
    for i in range(11,23):
        img[33,i]=(0,0,255) 
        img[34,i]=(0,0,255)
        img[35,i]=(0,0,255)
        img[36,i]=(0,0,255)
        img[37,i]=(0,0,255)

def Bascope(img):
    for i in range(45,55):
        img[i,32]=(0,0,255) 
        img[i,33]=(0,0,255) 
        img[i,34]=(0,0,255)
        img[i,35]=(0,0,255)

def perez1(img):
    for i in range(41,53):
        img[60,i]=(0,0,255) 
        img[61,i]=(0,0,255)
        img[62,i]=(0,0,255)
        img[63,i]=(0,0,255)
        img[64,i]=(0,0,255)

def perez2(img):
    for i in range(71,83):
        img[60,i]=(0,0,255) 
        img[61,i]=(0,0,255)
        img[62,i]=(0,0,255)
        img[63,i]=(0,0,255)
        img[64,i]=(0,0,255)

def perez3(img):
     for i in range(111,123):
        img[60,i]=(0,0,255) 
        img[61,i]=(0,0,255)
        img[62,i]=(0,0,255)
        img[63,i]=(0,0,255)
        img[64,i]=(0,0,255)
   

def perez4(img):
     for i in range(151,163):
        img[60,i]=(0,0,255) 
        img[61,i]=(0,0,255)
        img[62,i]=(0,0,255)
        img[63,i]=(0,0,255)
        img[64,i]=(0,0,255)

def lopez1(img):
    for i in range(32,45):
        img[i,130]=(0,0,255) 
        img[i,131]=(0,0,255) 
        img[i,132]=(0,0,255)
        img[i,133]=(0,0,255)

def lopez2(img):
    for i in range(62,75):
        img[i,130]=(0,0,255) 
        img[i,131]=(0,0,255) 
        img[i,132]=(0,0,255)
        img[i,133]=(0,0,255)

def lopez3(img):
   for i in range(112,125):
        img[i,130]=(0,0,255) 
        img[i,131]=(0,0,255) 
        img[i,132]=(0,0,255)
        img[i,133]=(0,0,255)


def bravo2(img):
      for i in range(75,85):
        img[220,i]=(0,0,255) 
        img[221,i]=(0,0,255)
        img[222,i]=(0,0,255)
        img[223,i]=(0,0,255)
        img[224,i]=(0,0,255)

def bravo3(img):
     for i in range(111,123):
        img[220,i]=(0,0,255) 
        img[221,i]=(0,0,255)
        img[222,i]=(0,0,255)
        img[223,i]=(0,0,255)
        img[224,i]=(0,0,255)

def bravo1(img):
     for i in range(35,45):
        img[220,i]=(0,0,255) 
        img[221,i]=(0,0,255)
        img[222,i]=(0,0,255)
        img[223,i]=(0,0,255)
        img[224,i]=(0,0,255)

def frias(img):
     for i in range(75,85):
        img[240,i]=(0,0,255) 
        img[241,i]=(0,0,255)
        img[242,i]=(0,0,255)
        img[243,i]=(0,0,255)
        img[244,i]=(0,0,255)

def torrez1(img):
     for i in range(55,65):
        img[228,i]=(0,0,255) 
        img[229,i]=(0,0,255)
        img[230,i]=(0,0,255)
        img[231,i]=(0,0,255)
        img[232,i]=(0,0,255)

def torrez2(img):
     for i in range(55,65):
        img[252,i]=(0,0,255) 
        img[253,i]=(0,0,255)
        img[254,i]=(0,0,255)
        img[255,i]=(0,0,255)
        img[256,i]=(0,0,255)

def juan2(img):
     for i in range(95,105):
        img[252,i]=(0,0,255) 
        img[253,i]=(0,0,255)
        img[254,i]=(0,0,255)
        img[255,i]=(0,0,255)
        img[256,i]=(0,0,255)

def juan1(img):
     for i in range(95,105):
        img[228,i]=(0,0,255) 
        img[229,i]=(0,0,255)
        img[230,i]=(0,0,255)
        img[231,i]=(0,0,255)
        img[232,i]=(0,0,255)

def pasteur1(img):
    for i in range(11,23):
        img[327,i]=(0,0,255) 
        img[328,i]=(0,0,255)
        img[329,i]=(0,0,255)
        img[330,i]=(0,0,255)
        img[331,i]=(0,0,255)

def pasteur2(img):
    for i in range(53,63):
        img[327,i]=(0,0,255) 
        img[328,i]=(0,0,255)
        img[329,i]=(0,0,255)
        img[330,i]=(0,0,255)
        img[331,i]=(0,0,255)

def pasteur3(img):
    for i in range(83,93):
        img[327,i]=(0,0,255) 
        img[328,i]=(0,0,255)
        img[329,i]=(0,0,255)
        img[330,i]=(0,0,255)
        img[331,i]=(0,0,255)

def pasteur4(img):
    for i in range(110,123):
        img[327,i]=(0,0,255) 
        img[328,i]=(0,0,255)
        img[329,i]=(0,0,255)
        img[330,i]=(0,0,255)
        img[331,i]=(0,0,255)

def beni(img):
    for i in range(11,23):
        img[353,i]=(0,0,255) 
        img[354,i]=(0,0,255)
        img[355,i]=(0,0,255)
        img[356,i]=(0,0,255)
        img[357,i]=(0,0,255)

def colombia1(img):
     for i in range(32,45):
        img[i,178]=(0,0,255) 
        img[i,179]=(0,0,255) 
        img[i,180]=(0,0,255)
        img[i,181]=(0,0,255)

def colombia2(img):
     for i in range(62,75):
        img[i,178]=(0,0,255) 
        img[i,179]=(0,0,255) 
        img[i,180]=(0,0,255)
        img[i,181]=(0,0,255)

def colombia3(img):
     for j in range(125,135):
        img[j,178]=(0,0,255) 
        img[j,179]=(0,0,255) 
        img[j,180]=(0,0,255)
        img[j,181]=(0,0,255)
     for i in range(95,105):
        img[i,178]=(0,0,255) 
        img[i,179]=(0,0,255) 
        img[i,180]=(0,0,255)
        img[i,181]=(0,0,255)
    
def colombia4(img):
     for j in range(180,190):
        img[j,178]=(0,0,255) 
        img[j,179]=(0,0,255) 
        img[j,180]=(0,0,255)
        img[j,181]=(0,0,255)
    
def jordan1(img):
     for i in range(83,93):
        img[355,i]=(0,0,255) 
        img[356,i]=(0,0,255)
        img[357,i]=(0,0,255)
        img[358,i]=(0,0,255)
        img[359,i]=(0,0,255)

def jordan2(img):
     for i in range(110,123):
        img[355,i]=(0,0,255) 
        img[356,i]=(0,0,255)
        img[357,i]=(0,0,255)
        img[358,i]=(0,0,255)
        img[359,i]=(0,0,255)

def jordan3(img):
    for i in range(150,163):
        img[355,i]=(0,0,255) 
        img[356,i]=(0,0,255)
        img[357,i]=(0,0,255)
        img[358,i]=(0,0,255)
        img[359,i]=(0,0,255)

def jordan4(img):
    for i in range(183,193):
        img[355,i]=(0,0,255) 
        img[356,i]=(0,0,255)
        img[357,i]=(0,0,255)
        img[358,i]=(0,0,255)
        img[359,i]=(0,0,255)

def españa1(img):
     for i in range(5,15):
        img[i,178]=(0,0,255) 
        img[i+1,179]=(0,0,255) 
        img[i+2,180]=(0,0,255)
        img[i+3,181]=(0,0,255)
        img[i+4,182]=(0,0,255)
        img[i+5,183]=(0,0,255)

def españa2(img):
     for i in range(35,45):
        img[i,210]=(0,0,255) 
        img[i+1,211]=(0,0,255) 
        img[i+2,212]=(0,0,255)
        img[i+3,213]=(0,0,255)
        img[i+4,214]=(0,0,255)
        img[i+5,215]=(0,0,255)
def españa3(img):
     for i in range(115,125):
        img[i,290]=(0,0,255) 
        img[i+1,291]=(0,0,255) 
        img[i+2,292]=(0,0,255)
        img[i+3,293]=(0,0,255)
        img[i+4,294]=(0,0,255)
        img[i+5,295]=(0,0,255)
def españa4(img):
     for i in range(135,145):
        img[i,310]=(0,0,255) 
        img[i+1,311]=(0,0,255) 
        img[i+2,312]=(0,0,255)
        img[i+3,313]=(0,0,255)
        img[i+4,314]=(0,0,255)
        img[i+5,315]=(0,0,255)
def españa5(img):
     for i in range(155,165):
        img[i,330]=(0,0,255) 
        img[i+1,331]=(0,0,255) 
        img[i+2,332]=(0,0,255)
        img[i+3,333]=(0,0,255)
        img[i+4,334]=(0,0,255)
        img[i+5,335]=(0,0,255)
def españa6(img):
     for i in range(185,195):
        img[i,360]=(0,0,255) 
        img[i+1,361]=(0,0,255) 
        img[i+2,362]=(0,0,255)
        img[i+3,363]=(0,0,255)
        img[i+4,364]=(0,0,255)
        img[i+5,365]=(0,0,255)
def francia1(img):
     for i in range(115,125):
        img[i,260]=(0,0,255) 
        img[i-1,261]=(0,0,255) 
        img[i-2,262]=(0,0,255)
        img[i-3,263]=(0,0,255)
        img[i-4,264]=(0,0,255)
        img[i-5,265]=(0,0,255)
def francia2(img):
     for i in range(145,155):
        img[i,290]=(0,0,255) 
        img[i+1,291]=(0,0,255) 
        img[i+2,292]=(0,0,255)
        img[i+3,293]=(0,0,255)
        img[i+4,294]=(0,0,255)
        img[i+5,295]=(0,0,255)
def francia3(img):
     for i in range(165,175):
        img[i,310]=(0,0,255) 
        img[i+1,311]=(0,0,255) 
        img[i+2,312]=(0,0,255)
        img[i+3,313]=(0,0,255)
        img[i+4,314]=(0,0,255)
        img[i+5,315]=(0,0,255)
def peru1(img):
     for i in range(115,125):
        img[i,330]=(0,0,255) 
        img[i+1,331]=(0,0,255) 
        img[i+2,332]=(0,0,255)
        img[i+3,333]=(0,0,255)
def peru2(img):
     for i in range(135,145):
        img[i,350]=(0,0,255) 
        img[i+1,351]=(0,0,255) 
        img[i+2,352]=(0,0,255)
        img[i+3,353]=(0,0,255)
def melgarejo1(img):
     for i in range(135,145):
        img[i,250]=(0,0,255) 
        img[i-1,251]=(0,0,255) 
        img[i-2,252]=(0,0,255)
        img[i-3,253]=(0,0,255)
def melgarejo2(img):
     for i in range(155,165):
        img[i,230]=(0,0,255) 
        img[i-1,231]=(0,0,255) 
        img[i-2,232]=(0,0,255)
        img[i-3,233]=(0,0,255)
def melgarejo3(img):
     for i in range(185,195):
        img[i,200]=(0,0,255) 
        img[i-1,201]=(0,0,255) 
        img[i-2,202]=(0,0,255)
        img[i-3,203]=(0,0,255)
def santa(img):
     for i in range(35,45):
        img[i,250]=(0,0,255) 
        img[i-1,251]=(0,0,255) 
        img[i-2,252]=(0,0,255)
        img[i-3,253]=(0,0,255)
        img[i-4,254]=(0,0,255)
        img[i-5,255]=(0,0,255)
def BGalindo1(img):
        for i in range(41,93):
                img[80,i]=(0,0,255) 
                img[81,i]=(0,0,255)
                img[82,i]=(0,0,255)
                img[83,i]=(0,0,255)
                img[84,i]=(0,0,255)

def BGalindo2(img):
        for i in range(113,123):
                img[80,i]=(0,0,255) 
                img[81,i]=(0,0,255)
                img[82,i]=(0,0,255)
                img[83,i]=(0,0,255)
                img[84,i]=(0,0,255)

def BGalindo3(img):
        for i in range(143,163):
                img[80,i]=(0,0,255) 
                img[81,i]=(0,0,255)
                img[82,i]=(0,0,255)
                img[83,i]=(0,0,255)
                img[84,i]=(0,0,255)
def BGalindo4(img):
        for i in range(193,293):
                img[80,i]=(0,0,255) 
                img[81,i]=(0,0,255)
                img[82,i]=(0,0,255)
                img[83,i]=(0,0,255)
                img[84,i]=(0,0,255)

def Suarez1(img):
    for i in range(11,23):
        img[383,i]=(0,0,255) 
        img[384,i]=(0,0,255)
        img[385,i]=(0,0,255)
        img[386,i]=(0,0,255)
        img[387,i]=(0,0,255)
def Suarez2(img):
    for i in range(45,75):
        img[383,i]=(0,0,255) 
        img[384,i]=(0,0,255)
        img[385,i]=(0,0,255)
        img[386,i]=(0,0,255)
        img[387,i]=(0,0,255)
def Suarez3(img):
    for i in range(145,155):
        img[383,i]=(0,0,255) 
        img[384,i]=(0,0,255)
        img[385,i]=(0,0,255)
        img[386,i]=(0,0,255)
        img[387,i]=(0,0,255)
def Suarez4(img):
    for i in range(185,225):
        img[383,i]=(0,0,255) 
        img[384,i]=(0,0,255)
        img[385,i]=(0,0,255)
        img[386,i]=(0,0,255)
        img[387,i]=(0,0,255)
def Bolivar1(img):
     for j in range(285,295):
        img[j,190]=(0,0,255) 
        img[j,191]=(0,0,255) 
        img[j,192]=(0,0,255)
        img[j,193]=(0,0,255)
def Bolivar2(img):
     for j in range(300,310):
        img[j,190]=(0,0,255) 
        img[j,191]=(0,0,255) 
        img[j,192]=(0,0,255)
        img[j,193]=(0,0,255)
def Bolivar3(img):
     for j in range(345,355):
        img[j,165]=(0,0,255) 
        img[j,166]=(0,0,255) 
        img[j,167]=(0,0,255)
        img[j,168]=(0,0,255)
def Bolivar4(img):
     for j in range(365,375):
        img[j,165]=(0,0,255) 
        img[j,166]=(0,0,255) 
        img[j,167]=(0,0,255)
        img[j,168]=(0,0,255)
def Polonia1(img):
     for i in range(203,213):
                img[273,i]=(0,0,255) 
                img[274,i]=(0,0,255)
                img[275,i]=(0,0,255)
                img[276,i]=(0,0,255)
                img[277,i]=(0,0,255)

def Polonia2(img):
     for i in range(243,253):
                img[273,i]=(0,0,255) 
                img[274,i]=(0,0,255)
                img[275,i]=(0,0,255)
                img[276,i]=(0,0,255)
                img[277,i]=(0,0,255)
def Polonia3(img):
     for i in range(293,303):
                img[273,i]=(0,0,255) 
                img[274,i]=(0,0,255)
                img[275,i]=(0,0,255)
                img[276,i]=(0,0,255)
                img[277,i]=(0,0,255)
def Polonia4(img):
     for i in range(323,333):
                img[273,i]=(0,0,255) 
                img[274,i]=(0,0,255)
                img[275,i]=(0,0,255)
                img[276,i]=(0,0,255)
                img[277,i]=(0,0,255)
def pinos1(img):
     for j in range(263,270):
        img[j,315]=(0,0,255) 
        img[j,316]=(0,0,255) 
        img[j,317]=(0,0,255)
        img[j,318]=(0,0,255)
def pinos2(img):
     for j in range(285,295):
        img[j,315]=(0,0,255) 
        img[j,316]=(0,0,255) 
        img[j,317]=(0,0,255)
        img[j,318]=(0,0,255)
def pinos3(img):
     for j in range(315,325):
        img[j,315]=(0,0,255) 
        img[j,316]=(0,0,255) 
        img[j,317]=(0,0,255)
        img[j,318]=(0,0,255)
def nataniel1(img):
        for j in range(263,270):
                img[j,225]=(0,0,255) 
                img[j,226]=(0,0,255) 
                img[j,227]=(0,0,255)
                img[j,228]=(0,0,255)
def nataniel2(img):
        for j in range(280,290):
                img[j,225]=(0,0,255) 
                img[j,226]=(0,0,255) 
                img[j,227]=(0,0,255)
                img[j,228]=(0,0,255)
def nataniel3(img):
        for j in range(310,340):
                img[j,225]=(0,0,255) 
                img[j,226]=(0,0,255) 
                img[j,227]=(0,0,255)
                img[j,228]=(0,0,255)      
def portugal2(img):
     for i in range(115,125):
        img[i,310]=(0,0,255) 
        img[i-1,311]=(0,0,255) 
        img[i-2,312]=(0,0,255)
        img[i-3,313]=(0,0,255)
        img[i-4,314]=(0,0,255)
        img[i-5,315]=(0,0,255)
def portugal1(img):
     for i in range(100,110):
        img[i,325]=(0,0,255) 
        img[i-1,326]=(0,0,255) 
        img[i-2,327]=(0,0,255)
        img[i-3,328]=(0,0,255)
        img[i-4,329]=(0,0,255)
        img[i-5,330]=(0,0,255)
def brasil1(img):
     for i in range(115,125):
        img[i,345]=(0,0,255) 
        img[i-1,346]=(0,0,255) 
        img[i-2,347]=(0,0,255)
        img[i-3,348]=(0,0,255)
        img[i-4,349]=(0,0,255)
        img[i-5,350]=(0,0,255)
def brasil2(img):
     for i in range(135,145):
        img[i,330]=(0,0,255) 
        img[i-1,331]=(0,0,255) 
        img[i-2,332]=(0,0,255)
        img[i-3,333]=(0,0,255)
        img[i-4,334]=(0,0,255)
        img[i-5,335]=(0,0,255)
def jose1(img):
     for i in range(55,65):
        img[i,290]=(0,0,255) 
        img[i-1,291]=(0,0,255) 
        img[i-2,292]=(0,0,255)
        img[i-3,293]=(0,0,255)
def jose2(img):
     for i in range(115,125):
        img[i,220]=(0,0,255) 
        img[i-1,221]=(0,0,255) 
        img[i-2,222]=(0,0,255)
        img[i-3,223]=(0,0,255)
def jose3(img):
     for i in range(135,145):
        img[i,210]=(0,0,255) 
        img[i-1,211]=(0,0,255) 
        img[i-2,212]=(0,0,255)
        img[i-3,213]=(0,0,255)
def jose4(img):
     for i in range(155,165):
        img[i,190]=(0,0,255) 
        img[i-1,191]=(0,0,255) 
        img[i-2,192]=(0,0,255)
        img[i-3,193]=(0,0,255)
def italia2(img):
        for i in range(165,175):
                img[i,280]=(0,0,255) 
                img[i+1,281]=(0,0,255) 
                img[i+2,282]=(0,0,255)
                img[i+3,283]=(0,0,255)
def italia1(img):
     for i in range(135,145):
        img[i,230]=(0,0,255) 
        img[i+1,231]=(0,0,255) 
        img[i+2,232]=(0,0,255)
        img[i+3,233]=(0,0,255)
def aroma1(img):
     for i in range(5,15):
        img[i,250]=(0,0,255) 
        img[i+1,251]=(0,0,255) 
        img[i+2,252]=(0,0,255)
        img[i+3,253]=(0,0,255)
def aroma2(img):
        for i in range(55,65):
                img[i,310]=(0,0,255) 
                img[i+1,311]=(0,0,255) 
                img[i+2,312]=(0,0,255)
                img[i+3,313]=(0,0,255)
def aroma3(img):
     for i in range(85,95):
        img[i,345]=(0,0,255) 
        img[i+1,346]=(0,0,255) 
        img[i+2,347]=(0,0,255)
        img[i+3,348]=(0,0,255)
        img[i+4,349]=(0,0,255)
        img[i+5,350]=(0,0,255)
def ayacucho1(img):
     for i in range(185,195):
        for j in range(330,340):
                img[i,j]=(0,0,255) 
                i=i-1
def ayacucho2(img):
        for j in range(285,295):
                img[j,285]=(0,0,255) 
                img[j,286]=(0,0,255) 
                img[j,287]=(0,0,255)
                img[j,288]=(0,0,255)
def ayacucho3(img):
        for j in range(305,335):
                img[j,285]=(0,0,255) 
                img[j,286]=(0,0,255) 
                img[j,287]=(0,0,255)
                img[j,288]=(0,0,255)
"""Empieza victor"""
def pintarHorizontal(img,iniX,largo,iniY,ancho): 
    try:
        for i in range(iniX,iniX + largo):
            for j in range (iniY,iniY+ancho):
                img[j,i]=(0,0,255) 
    except Exception:
        print("error")
    
         
def pintarvertical(img,iniX,largo,iniY,ancho): 
    try:
        for i in range(iniY,iniY + largo):
            for j in range (iniX,iniX+ancho):
                img[i,j]=(0,0,255) 
    except Exception:
        print("error")

def pintardiagonalIzqDer(img,iniX,largo,iniY,ancho):
    try:
        for i in range(0,ancho):
            iniY=iniY+1
            for j in range(0,largo):
                img[iniY+j,iniX+j]=(0,0,255) 
    except Exception:
        print("error")
            
            
def pintardiagonalDerIzq(img,iniX,largo,iniY,ancho):
    try:
        for i in range(0,ancho):
            iniY=iniY+1
            for j in range(0,largo):
                img[iniY+j,iniX-j]=(0,0,255)   
    except Exception:
        print("error")         

def gotham1(img):
    pintardiagonalIzqDer(img,655,10,90,4)
def gotham2(img):
    pintardiagonalIzqDer(img,675,12,110,4)
def gotham3(img):
    pintardiagonalIzqDer(img,702,10,137,4)
def gotham4(img):
    pintardiagonalIzqDer(img,725,15,157,4)  
def gotham5(img):
    pintardiagonalIzqDer(img,752,10,182,4) 
def gotham6(img):
    pintardiagonalIzqDer(img,773,20,203,4)
    
def acacia1(img):
    pintardiagonalIzqDer(img,688,15,60,4)
def acacia2(img):
    pintardiagonalIzqDer(img,713,10,83,4)
def acacia3(img):
    pintardiagonalIzqDer(img,735,10,105,4)
def acacia4(img):
    pintardiagonalIzqDer(img,755,20,122,4)
def acacia5(img):
    pintardiagonalIzqDer(img,785,10,152,4)

def esquina1(img):
    pintardiagonalIzqDer(img,755,10,37,4)
def esquina2(img):
    pintardiagonalIzqDer(img,780,10,62,4)
    
def carnaby1(img):
    pintardiagonalIzqDer(img,715,8,45,4)
def carnaby2(img):
    pintardiagonalIzqDer(img,732,10,62,4)
def carnaby3(img):
    pintardiagonalIzqDer(img,758,10,86,4)
def carnaby4(img):
    pintardiagonalIzqDer(img,779,10,106,4)

def acme1(img):
    pintardiagonalIzqDer(img,675,10,76,4)
def acme2(img):
    pintardiagonalDerIzq(img,703,10,80,4)
def acme3(img):
    pintardiagonalDerIzq(img,722,10,62,4)

def b11(img):
    pintardiagonalIzqDer(img,620,10,124,4) 
def b12(img):
    pintardiagonalIzqDer(img,651,10,134,4) 
def b13(img):
    pintardiagonalIzqDer(img,681,10,164,4) 
    
def elm(img):
    pintardiagonalIzqDer(img,740,15,139,4)
    
def elmwood1(img):
    pintardiagonalDerIzq(img,730,8,140,4)
def elmwood2(img):
    pintardiagonalDerIzq(img,745,8,125,4)
def elmwood3(img):
    pintardiagonalDerIzq(img,765,10,105,4)
def elmwood4(img):
    pintardiagonalDerIzq(img,790,10,82,4)
    
def bourbon1(img):
    pintardiagonalDerIzq(img,710,10,210,4)
def bourbon2(img):
    pintardiagonalDerIzq(img,740,23,180,4)
def bourbon3(img):
    pintardiagonalDerIzq(img,758,8,164,4)
def bourbon4(img):
    pintardiagonalDerIzq(img,773,8,148,4)
def bourbon5(img):
    pintardiagonalDerIzq(img,793,10,130,4)

def baker1(img):
    pintarvertical(img,774,15,243,4)
def baker2(img):
    pintardiagonalIzqDer(img,756,15,218,4)
def baker3(img):
    pintardiagonalDerIzq(img,764,8,202,4)
def baker4(img):
    pintardiagonalDerIzq(img,794,20,172,4)

def melrose1(img):
    pintardiagonalDerIzq(img,588,15,184,4)
def melrose2(img):
    pintardiagonalDerIzq(img,610,12,162,4)
def melrose3(img):
    pintardiagonalDerIzq(img,630,6,143,4)
def melrose4(img):
    pintardiagonalDerIzq(img,665,15,110,4)
    
def southPark1(img):
    pintardiagonalDerIzq(img,635,10,185,6)
def southPark2(img):
    pintardiagonalDerIzq(img,663,15,158,6)
def southPark3(img):
    pintardiagonalDerIzq(img,690,15,133,6)
def southPark4(img):
    pintardiagonalDerIzq(img,720,20,103,6)  
def southPark5(img):
    pintardiagonalDerIzq(img,740,10,83,6)
def southPark6(img):
    pintardiagonalDerIzq(img,766,15,58,6)
def southPark7(img):
    pintardiagonalDerIzq(img,786,10,38,6)
def southPark8(img):
    pintarvertical(img,792,20,8,4)
    
def b21(img):
    pintardiagonalDerIzq(img,638,15,230,4)
def b22(img):
    pintardiagonalDerIzq(img,660,10,210,4)
def b23(img):
    pintardiagonalDerIzq(img,690,13,180,4)
def wallStreet1(img):
    pintarHorizontal(img,637,20,262,4)
def wallStreet2(img):
    pintarHorizontal(img,675,15,262,4)
def wallStreet3(img):
    pintarHorizontal(img,718,20,262,4)
def wallStreet4(img):
    pintarHorizontal(img,760,15,262,4)
def wallStreet5(img):
    pintarHorizontal(img,785,10,262,4)
    
def a11(img):
    pintarHorizontal(img,760,15,290,4)
def a21(img):
    pintarvertical(img,780,10,300,4)
def arkham1(img):
    pintardiagonalDerIzq(img,552,8,60,4)
def arkham2(img):
    pintardiagonalDerIzq(img,571,8,41,4)
def arkham3(img):
    pintardiagonalDerIzq(img,605,25,8,4)

def foster1(img):
    pintardiagonalIzqDer(img,557,15,17,4)
def foster2(img):
    pintardiagonalIzqDer(img,582,10,45,4)
    
def piedradura1(img):
    pintardiagonalIzqDer(img,510,10,8,4)
def piedradura2(img):
    pintardiagonalIzqDer(img,535,15,32,4)
def piedradura3(img):
    pintardiagonalIzqDer(img,565,10,60,4)
    
def nogal1(img):
    pintardiagonalIzqDer(img,577,12,162,4)
def nogal2(img):
    pintardiagonalIzqDer(img,600,15,185,4)
def nogal3(img):
    pintardiagonalIzqDer(img,627,12,210,4)
def nogal4(img):
    pintardiagonalIzqDer(img,650,15,240,4)

def c1(img):
    pintardiagonalDerIzq(img,502,10,8,4)
def c2(img):
    pintardiagonalDerIzq(img,520,10,32,4)
def c3(img):
    pintardiagonalIzqDer(img,625,15,5,4)
def mar1(img):
    pintardiagonalIzqDer(img,433,15,106,4)
def mar2(img):
    pintardiagonalIzqDer(img,469,8,122,4)
def mar3(img):
    pintardiagonalIzqDer(img,480,8,150,4)
    
def olmos1(img):
    pintardiagonalDerIzq(img,390,8,186,4)
def olmos2(img):
    pintardiagonalDerIzq(img,409,10,168,4)
def olmos3(img):
    pintardiagonalDerIzq(img,450,20,130,4)
def olmos4(img):
    pintardiagonalDerIzq(img,480,12,100,4)
def olmos5(img):
    pintardiagonalDerIzq(img,510,20,71,4)

def siempreviva1(img):
    pintardiagonalDerIzq(img,410,8,203,4)
def siempreviva2(img):
    pintardiagonalDerIzq(img,429,10,185,4)
def siempreviva3(img):
    pintardiagonalDerIzq(img,478,20,140,4)
def siempreviva4(img):
    pintardiagonalDerIzq(img,500,12,117,4)
    
def metroville1(img):
    pintardiagonalDerIzq(img,449,8,205,4)
def metroville2(img):
    pintardiagonalDerIzq(img,484,20,168,4)
    
def coronado1(img):
    pintardiagonalDerIzq(img,440,8,253,4)
def coronado2(img):
    pintardiagonalDerIzq(img,458,6,240,4)
def coronado3(img):
    pintardiagonalDerIzq(img,478,6,230,4)
def coronado4(img):
    pintarHorizontal(img,495,8,227,4)  
def coronado5(img):
    pintarHorizontal(img,516,15,227,4)  
    
def sol(img):
    pintarHorizontal(img,500,20,208,4)  
    
def salero1(img):
    pintarHorizontal(img,452,8,268,4)  
def salero2(img):
    pintarHorizontal(img,496,20,268,4)  
def salero3(img):
    pintardiagonalDerIzq(img,555,10,253,4)
    
def nintendo1(img):
    pintarHorizontal(img,453,15,293,4)  
def nintendo2(img):
    pintarHorizontal(img,496,15,293,4)  
def nintendo3(img):
    pintardiagonalIzqDer(img,520,10,298,5)

def abbeyroad1(img):
    pintardiagonalIzqDer(img,510,8,230,4)
def abbeyroad2(img):
    pintardiagonalIzqDer(img,525,12,248,4)
def abbeyroad3(img):
    pintardiagonalIzqDer(img,547,12,273,4)
def abbeyroad4(img):
    pintardiagonalIzqDer(img,565,8,298,4)
def abbeyroad5(img):
    pintardiagonalDerIzq(img,575,8,330,4)
def abbeyroad6(img):
    pintardiagonalDerIzq(img,565,14,346,4)
def abbeyroad7(img):
    pintarHorizontal(img,530,15,365,4)
    
def elmwood21(img):
    pintardiagonalIzqDer(img,400,10,185,4)
def elmwood22(img):
    pintardiagonalIzqDer(img,420,10,205,4)
def elmwood23(img):
    pintardiagonalIzqDer(img,440,12,222,4)
def elmwood24(img):
    pintarvertical(img,465,15,247,4)
    
def peachtree1(img):
    pintarvertical(img,446,10,255,4)
def peachtree2(img):
    pintarvertical(img,446,15,275,4)
def peachtree3(img):
    pintarvertical(img,446,10,300,4)
def peachtree4(img):
    pintardiagonalIzqDer(img,446,12,330,4)
def peachtree5(img):
    pintardiagonalIzqDer(img,456,12,350,4)
def peachtree6(img):
    pintarHorizontal(img,478,10,370,4)  
def peachtree7(img):
    pintarHorizontal(img,498,10,370,4)  
    
def d1(img):
    pintarHorizontal(img,498,15,247,4)
def luna(img):
    pintardiagonalDerIzq(img,582,10,278,4)
def luz(img):
    pintardiagonalDerIzq(img,450,15,350,4)
def vida(img):
    pintarvertical(img,490,20,380,4)
def nube1(img):
    pintardiagonalDerIzq(img,485,10,350,4)
def nube2(img):
    pintardiagonalDerIzq(img,470,15,373,4)
def alba(img):
    pintardiagonalDerIzq(img,577,14,363,4)
def brisa1(img):
    pintardiagonalIzqDer(img,572,8,345,4)
def brisa2(img):
    pintardiagonalIzqDer(img,590,8,358,4)

def aroma1(img):
    pintardiagonalIzqDer(img,255,8,4,6)
def aroma2(img):
    pintardiagonalIzqDer(img,305,20,52,6)
def aroma3(img):
    pintardiagonalIzqDer(img,345,8,92,6)
def aroma4(img):
    pintardiagonalIzqDer(img,363,8,108,6)
def aroma5(img):
    pintardiagonalIzqDer(img,410,6,150,6)
def aroma6(img):
    pintardiagonalIzqDer(img,426,8,165,6)
def aroma7(img):
    pintardiagonalIzqDer(img,441,8,180,6)
def aroma8(img):
    pintardiagonalIzqDer(img,465,15,204,6)

def elmore1(img):
    pintardiagonalIzqDer(img,465,15,4,6)
def elmore2(img):
    pintardiagonalIzqDer(img,492,10,29,6)
def elmore3(img):
    pintardiagonalIzqDer(img,513,6,50,6)
def elmore4(img):
    pintardiagonalIzqDer(img,525,6,62,6)
def elmore5(img):
    pintardiagonalIzqDer(img,545,6,82,6)
def elmore6(img):
    pintardiagonalIzqDer(img,565,12,102,6)
def elmore7(img):
    pintardiagonalIzqDer(img,605,8,142,6)
def elmore8(img):
    pintardiagonalIzqDer(img,625,10,162,6)
def elmore9(img):
    pintardiagonalIzqDer(img,648,15,185,6)
def elmore10(img):
    pintardiagonalIzqDer(img,672,15,207,6)
def elmore11(img):
    pintardiagonalIzqDer(img,698,15,237,6)
def elmore12(img):
    pintarvertical(img,705,15,275,6)

def springfield1(img):
    pintardiagonalDerIzq(img,308,10,350,6)
def springfield2(img): 
    pintardiagonalDerIzq(img,328,10,330,6)
def springfield3(img):
    pintarHorizontal(img,348,20,320,6)  
def springfield4(img):
    pintarHorizontal(img,390,15,317,6) 
def springfield5(img):
    pintarHorizontal(img,425,12,317,6) 
def springfield6(img):
    pintarHorizontal(img,455,10,317,6)  
def springfield7(img):
    pintardiagonalIzqDer(img,475,10,325,6)  
def springfield8(img):
    pintarHorizontal(img,495,10,340,6)  
def springfield9(img):
    pintardiagonalDerIzq(img,528,10,325,6)  
def springfield10(img):
    pintarHorizontal(img,542,20,317,6)  
def springfield11(img):
    pintarHorizontal(img,582,20,317,6)  
def springfield12(img):
    pintarHorizontal(img,622,20,317,6)  
def springfield13(img):
    pintarHorizontal(img,658,15,317,6)  
def springfield14(img):
    pintarHorizontal(img,732,15,317,6)  
def springfield15(img):
    pintarHorizontal(img,760,15,317,6)  
def springfield16(img):
    pintarHorizontal(img,785,10,317,6)  

def millaverde1(img):
    pintardiagonalDerIzq(img,485,10,298,6)
def millaverde2(img):
    pintarvertical(img,486,15,273,6)
def millaverde3(img):
    pintarvertical(img,486,15,252,6)
def millaverde4(img):
    pintarvertical(img,486,10,232,6)
def millaverde5(img):
    pintarvertical(img,488,10,212,6)
def millaverde6(img):
    pintarvertical(img,492,25,175,6)  
def millaverde7(img):
    pintardiagonalDerIzq(img,520,20,140,6) 
def millaverde8(img):
    pintardiagonalDerIzq(img,550,20,105,6)    

def ciruelos(img):
    pintarvertical(img,30,20,400,5)

def santiago1(img):
    pintarvertical(img,105,15,411,5)
def santiago2(img):
    pintarvertical(img,105,15,435,5)
def santiago3(img):
    pintarvertical(img,105,15,465,5)
def santiago4(img):
    pintardiagonalDerIzq(img,100,15,485,7)
def santiago5(img):
    pintardiagonalDerIzq(img,80,20,525,6)
    
def paris1(img):
    pintarvertical(img,130,20,400,5)
def paris2(img):
    pintarvertical(img,130,20,435,5)
def paris3(img):
    pintarvertical(img,130,20,470,5)

def calera1(img):
    pintardiagonalIzqDer(img,40,10,480,6) 
def calera2(img):
    pintardiagonalIzqDer(img,62,15,500,6) 
def calera3(img):
    pintardiagonalIzqDer(img,90,12,525,6) 
def calera4(img):
    pintardiagonalIzqDer(img,118,10,550,6) 

def pisiga1(img):
    pintardiagonalDerIzq(img,15,11,525,6)
def pisiga2(img):
    pintardiagonalDerIzq(img,32,7,510,6)
def pisiga3(img):
    pintardiagonalDerIzq(img,50,7,495,6)
def pisiga4(img):
    pintarvertical(img,75,14,470,5)
def pisiga5(img):
    pintarvertical(img,75,14,445,5)


def santaRosa1(img):
    pintardiagonalDerIzq(img,5,11,570,6)
def santaRosa2(img):
    pintardiagonalDerIzq(img,30,15,545,6)
def santaRosa3(img):
    pintardiagonalDerIzq(img,50,11,525,6)

def yumucu1(img):
    pintardiagonalIzqDer(img,23,10,525,6)
def yumucu2(img):
    pintardiagonalIzqDer(img,40,12,540,6) 
def yumucu3(img):
    pintardiagonalDerIzq(img,50,10,555,6) 
def yumucu4(img):
    pintardiagonalIzqDer(img,40,9,570,6) 
def yumucu5(img):
    pintardiagonalIzqDer(img,75,10,593,6) 

def joya1(img):
    pintardiagonalIzqDer(img,10,10,570,6) 
def joya2(img):
    pintardiagonalIzqDer(img,30,8,590,6) 
def joya3(img):
    pintardiagonalIzqDer(img,55,10,610,6) 
def joya4(img):
    pintardiagonalIzqDer(img,75,10,625,6) 
def joya5(img):
    pintardiagonalIzqDer(img,100,10,650,6)

def ballon1(img):
    pintardiagonalIzqDer(img,0,7,590,6)
def ballon2(img):
    pintardiagonalIzqDer(img,10,8,605,6) 
def ballon3(img):
    pintardiagonalIzqDer(img,35,10,625,6) 
def ballon4(img):
    pintardiagonalIzqDer(img,55,10,640,6) 

def lopez1(img):
    pintardiagonalIzqDer(img,70,20,685,6) 
def lopez2(img):
    pintardiagonalIzqDer(img,105,10,720,6) 
def lopez3(img):
    pintarHorizontal(img,125,18,735,5)

def sanLuis1(img):
    pintardiagonalIzqDer(img,100,10,565,6) 
def sanLuis2(img):
    pintardiagonalIzqDer(img,125,10,585,6) 
def sanLuis3(img):
    pintardiagonalIzqDer(img,165,20,640,6) 

def bruselas1(img):
    pintardiagonalIzqDer(img,165,10,505,6)
def bruselas2(img):
    pintardiagonalIzqDer(img,190,10,525,6) 
def bruselas3(img):
    pintardiagonalIzqDer(img,210,15,545,6)
def bruselas4(img):
    pintardiagonalIzqDer(img,240,15,575,6) 

def japon1(img):
    pintardiagonalIzqDer(img,258,15,550,6)
def japon2(img):
    pintardiagonalIzqDer(img,285,15,575,6) 

def lima(img):
    pintardiagonalIzqDer(img,280,10,535,6)

def paria1(img):
    pintardiagonalIzqDer(img,230,15,445,6)
def paria2(img):
    pintardiagonalIzqDer(img,260,10,470,6) 
def paria3(img):
    pintardiagonalIzqDer(img,280,10,490,6) 
def paria4(img):
    pintardiagonalIzqDer(img,300,10,510,6)
def paria5(img):
    pintardiagonalIzqDer(img,330,12,510,6)

def guzman(img):
    pintardiagonalIzqDer(img,250,15,420,6)

def pando1(img):
    pintardiagonalIzqDer(img,185,13,680,6)
def pando2(img):
    pintardiagonalIzqDer(img,210,9,700,6)
def pando3(img):
    pintardiagonalIzqDer(img,230,9,715,6)
def pando4(img):
    pintardiagonalIzqDer(img,250,11,730,6)

def inter1(img):
    pintardiagonalIzqDer(img,50,15,710,6)
def inter2(img):
    pintardiagonalIzqDer(img,80,9,740,6)
def inter3(img):
    pintardiagonalIzqDer(img,160,15,705,6)
def inter4(img):
    pintardiagonalIzqDer(img,190,10,725,6)
def inter5(img):
    pintardiagonalIzqDer(img,210,8,740,6)

def vandiola1(img):
    pintardiagonalIzqDer(img,220,15,652,6)
def vandiola2(img):
    pintardiagonalIzqDer(img,260,9,680,6)
def vandiola3(img):
    pintardiagonalIzqDer(img,280,9,695,6)
def vandiola4(img):
    pintardiagonalIzqDer(img,300,10,708,6)
def vandiola5(img):
    pintardiagonalDerIzq(img,310,15,730,6)

def lanza1(img):
    pintardiagonalIzqDer(img,290,15,655,6)
def lanza2(img):
    pintardiagonalIzqDer(img,332,15,682,6)

def torres(img):
    pintardiagonalIzqDer(img,350,15,655,6)

def daza1(img):
    pintardiagonalIzqDer(img,350,9,560,6)
def daza2(img):
    pintardiagonalIzqDer(img,370,10,572,6)
def daza3(img):
    pintardiagonalIzqDer(img,390,10,585,6)
def daza4(img):
    pintarHorizontal(img,415,20,598,5)
def daza5(img):
    pintarHorizontal(img,460,15,598,5)
def daza6(img):
    pintarHorizontal(img,490,15,598,5)

def zaruma1(img):
    pintardiagonalIzqDer(img,365,10,535,6)
def zaruma2(img):
    pintardiagonalIzqDer(img,387,10,548,6)
def zaruma3(img):
    pintardiagonalIzqDer(img,410,10,560,6)
def zaruma4(img):
    pintardiagonalIzqDer(img,430,12,575,6)
def zaruma5(img):
    pintarvertical(img,452,15,600,5)
def zaruma6(img):
    pintarvertical(img,452,15,620,5)

def peñas1(img):
    pintardiagonalIzqDer(img,330,10,408,6)
def peñas2(img):
    pintardiagonalIzqDer(img,348,15,433,6)
def peñas3(img):
    pintardiagonalIzqDer(img,370,9,455,6)
def peñas4(img):
    pintardiagonalIzqDer(img,385,9,470,6)
def peñas5(img):
    pintardiagonalIzqDer(img,410,15,490,6)
def peñas6(img):
    pintardiagonalIzqDer(img,445,15,515,6)

def castrilla1(img):
    pintardiagonalIzqDer(img,340,9,338,6)
def castrilla2(img):
    pintardiagonalIzqDer(img,350,9,352,6)
def castrilla3(img):
    pintardiagonalIzqDer(img,365,10,370,6)

def dulon1(img):
    pintardiagonalIzqDer(img,350,12,385,6)
def dulon2(img):
    pintardiagonalIzqDer(img,370,12,410,6)
def dulon3(img):
    pintardiagonalIzqDer(img,390,9,430,6)
def dulon4(img):
    pintardiagonalIzqDer(img,408,9,445,6)

def habana1(img):
    pintardiagonalDerIzq(img,40,30,650,6)
def habana2(img):
    pintardiagonalDerIzq(img,68,9,622,6)

def toledo1(img):
    pintardiagonalDerIzq(img,110,15,583,6)
def toledo2(img):
    pintardiagonalDerIzq(img,130,9,565,6)
def toledo3(img):
    pintardiagonalDerIzq(img,150,9,545,6)
def toledo4(img):
    pintardiagonalDerIzq(img,180,9,525,6)
def toledo5(img):
    pintardiagonalDerIzq(img,235,35,480,6)
def toledo6(img):
    pintardiagonalDerIzq(img,260,9,450,6)
def toledo7(img):
    pintardiagonalDerIzq(img,285,9,425,6)

def hungria1(img):
    pintardiagonalDerIzq(img,320,9,405,6)
def hungria2(img):
    pintarvertical(img,323,15,380,5)
def hungria3(img):
    pintardiagonalDerIzq(img,343,9,358,6)

def quito1(img):
    pintardiagonalDerIzq(img,355,9,415,6)
def quito2(img):
    pintardiagonalDerIzq(img,375,9,395,6)
def quito3(img):
    pintardiagonalDerIzq(img,390,9,380,6)

def bayern1(img):
    pintardiagonalDerIzq(img,30,40,700,6)
def bayern2(img):
    pintardiagonalDerIzq(img,52,12,678,6)
def bayern3(img):
    pintardiagonalDerIzq(img,70,9,665,6)
def bayern4(img):
    pintardiagonalDerIzq(img,90,9,645,6)
def bayern5(img):
    pintardiagonalDerIzq(img,130,30,605,6)
def bayern6(img):
    pintardiagonalDerIzq(img,170,15,570,6)
def bayern7(img):
    pintardiagonalDerIzq(img,200,9,540,6)
def bayern8(img):
    pintardiagonalDerIzq(img,250,35,498,6)

def pocoata1(img):
    pintarvertical(img,120,15,740,5)
def pocoata2(img):
    pintarvertical(img,120,15,710,5)
def pocoata3(img):
    pintarvertical(img,120,15,675,5)
def pocoata4(img):
    pintardiagonalDerIzq(img,140,9,650,6)
def pocoata5(img):
    pintardiagonalDerIzq(img,180,15,610,6)
def pocoata6(img):
    pintardiagonalDerIzq(img,200,9,590,6)
def pocoata7(img):
    pintardiagonalDerIzq(img,225,9,570,6)
def pocoata8(img):
    pintardiagonalDerIzq(img,245,9,550,6)
def pocoata9(img):
    pintardiagonalDerIzq(img,265,9,530,6)
def pocoata10(img):
    pintardiagonalDerIzq(img,285,9,510,6)

def sanJuan1(img):
    pintardiagonalDerIzq(img,170,9,685,6)
def sanJuan2(img):
    pintardiagonalDerIzq(img,190,8,668,6)
def sanJuan3(img):
    pintardiagonalDerIzq(img,210,9,650,6)
def sanJuan4(img):
    pintardiagonalDerIzq(img,235,9,625,6)
def sanJuan5(img):
    pintardiagonalDerIzq(img,260,9,595,6)
def sanJuan6(img):
    pintardiagonalDerIzq(img,280,10,575,6)
def sanJuan7(img):
    pintardiagonalDerIzq(img,295,9,555,6)
def sanJuan8(img):
    pintardiagonalDerIzq(img,305,8,538,6)
def sanJuan9(img):
    pintardiagonalDerIzq(img,320,9,520,6)
def sanJuan10(img):
    pintardiagonalDerIzq(img,340,13,490,6)
def sanJuan11(img):
    pintardiagonalDerIzq(img,362,9,460,6)
def sanJuan12(img):
    pintardiagonalDerIzq(img,382,9,435,6)
def sanJuan13(img):
    pintardiagonalDerIzq(img,400,9,410,6)

def alcala1(img):
    pintardiagonalDerIzq(img,267,5,743,6)
def alcala2(img):
    pintardiagonalDerIzq(img,288,15,715,6)
def alcala3(img):
    pintardiagonalDerIzq(img,310,9,685,6)
def alcala4(img):
    pintardiagonalDerIzq(img,330,9,655,6)
def alcala5(img):
    pintardiagonalDerIzq(img,355,9,620,6)
def alcala6(img):
    pintardiagonalDerIzq(img,375,9,595,6)
def alcala7(img):
    pintardiagonalDerIzq(img,398,9,565,6)
def alcala8(img):
    pintardiagonalDerIzq(img,415,9,540,6)
def alcala9(img):
    pintardiagonalDerIzq(img,435,9,515,6)
def alcala10(img):
    pintardiagonalDerIzq(img,455,12,490,6)
def alcala11(img):
    pintarHorizontal(img,470,12,490,5)
def alcala12(img):
    pintarHorizontal(img,500,12,495,5)

def guayacan1(img):
    pintardiagonalDerIzq(img,340,15,730,6)
def guayacan2(img):
    pintardiagonalDerIzq(img,355,9,710,6)
def guayacan3(img):
    pintardiagonalDerIzq(img,370,9,690,6)
def guayacan4(img):
    pintardiagonalDerIzq(img,390,9,660,6)
def guayacan5(img):
    pintarvertical(img,405,12,625,5)
def guayacan6(img):
    pintarvertical(img,405,12,605,5)
def guayacan7(img):
    pintardiagonalDerIzq(img,418,9,580,6)
def guayacan8(img):
    pintardiagonalDerIzq(img,450,9,555,6)
def guayacan9(img):
    pintardiagonalDerIzq(img,490,15,500,6)

def tunari1(img):
    pintardiagonalDerIzq(img,390,9,490,6)
def tunari2(img):
    pintardiagonalDerIzq(img,410,9,460,6)
def tunari3(img):
    pintardiagonalDerIzq(img,430,9,430,6)

def pool(img):
    pintardiagonalDerIzq(img,265,15,700,6)

def C4(img):
    pintarHorizontal(img,90,10,455,6)

def C5(img):
    pintarHorizontal(img,115,10,455,6)

def C6(img):
    pintarHorizontal(img,90,10,430,6)

def C7(img):
    pintarHorizontal(img,115,10,430,6)

def AB23(img):
    pintardiagonalDerIzq(img,95,9,720,6)

def C13(img):
    pintardiagonalDerIzq(img,220,9,605,6)

def C14(img):
    pintardiagonalDerIzq(img,200,9,705,6)

def C15(img):
    pintardiagonalDerIzq(img,20,9,590,6)

def C16(img):
    pintardiagonalDerIzq(img,360,9,370,6)

def C17(img):
    pintardiagonalDerIzq(img,380,9,350,6)

def C18(img):
    pintardiagonalDerIzq(img,395,9,450,6)

def RRivero1(img):
    pintardiagonalDerIzq(img,205,9,738,7)
def RRivero2(img):
    pintardiagonalDerIzq(img,218,9,720,7)
def RRivero3(img):
    pintardiagonalDerIzq(img,247,20,680,7)
def RRivero4(img):
    pintardiagonalDerIzq(img,270,15,650,7)
def RRivero5(img):
    pintardiagonalDerIzq(img,310,20,600,7)
def RRivero6(img):
    pintardiagonalDerIzq(img,330,15,570,7)
def RRivero7(img):
    pintardiagonalDerIzq(img,355,15,535,7)
def RRivero8(img):
    pintardiagonalDerIzq(img,370,9,515,7)


def springfield17(img):
    pintarvertical(img,290,15,375,5)
def springfield18(img):
    pintarHorizontal(img,262,15,365,5)
def springfield19(img):
    pintarvertical(img,250,15,385,5)
def springfield20(img):
    pintarHorizontal(img,265,15,405,5)
def springfield21(img):
    pintardiagonalDerIzq(img,250,10,405,6)
def springfield22(img):
    pintardiagonalDerIzq(img,230,10,420,6)
def springfield23(img):
    pintardiagonalDerIzq(img,200,30,450,6)
def springfield24(img):
    pintardiagonalDerIzq(img,160,10,490,6)
def springfield25(img):
    pintarHorizontal(img,137,10,500,5)
def springfield26(img):
    pintarvertical(img,150,15,510,5)
def springfield27(img):
    pintarHorizontal(img,125,15,532,5)
def springfield28(img):
    pintarvertical(img,115,15,510,5)
def springfield29(img):
    pintardiagonalDerIzq(img,115,10,530,6)
def springfield30(img):
    pintardiagonalDerIzq(img,100,10,545,6)
def springfield31(img):
    pintardiagonalDerIzq(img,85,15,560,6)
def springfield32(img):
    pintardiagonalDerIzq(img,60,10,585,6)
def springfield33(img):
    pintardiagonalDerIzq(img,40,10,605,6)
def springfield34(img):
    pintardiagonalDerIzq(img,20,15,620,6)

def heroinas1(img):
    pintardiagonalIzqDer(img,150,10,530,6)
def heroinas2(img):
    pintardiagonalIzqDer(img,165,10,545,6)
def heroinas3(img):
    pintardiagonalIzqDer(img,195,10,570,6)
def heroinas4(img):
    pintardiagonalIzqDer(img,215,10,590,6)
def heroinas5(img):
    pintardiagonalIzqDer(img,235,10,605,6)
def heroinas6(img):
    pintardiagonalIzqDer(img,255,10,620,6)
def heroinas7(img):
    pintarHorizontal(img,292,30,642,5)
def heroinas8(img):
    pintarHorizontal(img,360,30,642,5)
def heroinas9(img):
    pintarHorizontal(img,410,30,642,5)
def heroinas10(img):
    pintarHorizontal(img,460,20,642,5)
def heroinas11(img):
    pintarHorizontal(img,490,20,642,5)

def america1(img):
    pintardiagonalIzqDer(img,290,10,410,6)
def america2(img):
    pintardiagonalIzqDer(img,310,30,440,6)
def america3(img):
    pintardiagonalIzqDer(img,354,15,490,6)
def america4(img):
    pintardiagonalIzqDer(img,390,15,515,6)
def america5(img):
    pintardiagonalIzqDer(img,430,10,533,6)
def america6(img):
    pintarHorizontal(img,470,20,548,5)

def lizarraga1(img):
    pintarHorizontal(img,370,20,618,5)
def lizarraga2(img):
    pintarHorizontal(img,420,25,618,5)
def lizarraga3(img):
    pintarHorizontal(img,460,15,618,5)

def blink1(img):
    pintarHorizontal(img,350,25,730,5)
def blink2(img):
    pintarHorizontal(img,400,15,730,6)

def rasmus1(img):
    pintarvertical(img,150,30,710,5)
def rasmus2(img):
    pintarvertical(img,150,25,650,6)
def rasmus3(img):
    pintarvertical(img,150,25,610,6)

#cargarGrafico()
        


