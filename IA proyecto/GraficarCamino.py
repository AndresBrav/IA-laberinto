import cv2
from Casilla import *

#sucre=Casilla('Sucre',1,50,1)

def GraficarRecorrido(listaRecorrido):
    lista=[]
    lista=listaRecorrido
    print(lista[1],"ejemplo de que funciona")
    cargarGrafico()

def cargarGrafico():
    img=cv2.imread("IA proyecto/mapaIA5.jpg")

    graficarSucre(img)
    Bascope(img)
    perez1(img)
    perez2(img)
    perez3(img)
    perez4(img)
    lopez1(img)
    lopez2(img)
    lopez3(img)
    

    bravo1(img)
    bravo2(img)
    bravo3(img)
    frias(img)
    torrez1(img)
    torrez2(img)
    juan2(img)
    juan1(img)
    pasteur1(img)
    pasteur2(img)
    pasteur3(img)
    pasteur4(img)
    beni(img)
    
    Gotham1(img)
    Gotham2(img)
    Gotham3(img)
    Gotham4(img)
    Gotham5(img)
    Gotham6(img)
    
    Acacia1(img)
    Acacia2(img)
    Acacia3(img)
    Acacia4(img)
    Acacia5(img)
    
    esquina1(img)
    esquina2(img)
    carnaby1(img)
    carnaby2(img)
    carnaby3(img)
    carnaby4(img)
    
    acme1(img)
    acme2(img)
    acme3(img)
    
    B11(img)
    B12(img)
    B13(img)
    
    elm(img)
    
    elmwood1(img)
    elmwood2(img)
    elmwood3(img)
    elmwood4(img)
    
    bourbon1(img)
    bourbon2(img)
    bourbon3(img)
    bourbon4(img)
    bourbon5(img)
    
    baker1(img)
    baker2(img)
    baker3(img)
    baker4(img)
    melrose1(img)
    melrose2(img)
    melrose3(img)
    melrose4(img)
    SouthPark1(img)
    SouthPark2(img)
    SouthPark3(img)
    SouthPark4(img)
    SouthPark5(img)
    SouthPark6(img)
    SouthPark7(img)
    SouthPark8(img)
    b21(img)
    b22(img)
    b23(img)
    WallStreet1(img)
    WallStreet2(img)
    WallStreet3(img)
    WallStreet4(img)
    a11(img)
    a21(img)
    arkham1(img)
    arkham2(img)
    arkham3(img)
    foster1(img)
    foster2(img)
    piedradura1(img)
    piedradura2(img)
    piedradura3(img)
    C1(img)
    C2(img)
    C3(img)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
     
def pintarHorizontal(img,iniX,largo,iniY,ancho): 
    for i in range(iniX,iniX + largo):
        for j in range (iniY,iniY+ancho):
            img[j,i]=(0,0,255) 
    
         
def pintarvertical(img,iniX,largo,iniY,ancho): 
    for i in range(iniY,iniY + largo):
        for j in range (iniX,iniX+ancho):
            img[i,j]=(0,0,255) 

def pintardiagonalIzqDer(img,iniX,largo,iniY,ancho):
    for i in range(0,ancho):
        iniY=iniY+1
        for j in range(0,largo):
            img[iniY+j,iniX+j]=(0,0,255) 

def pintardiagonalDerIzq(img,iniX,largo,iniY,ancho):
    for i in range(0,ancho):
        iniY=iniY+1
        for j in range(0,largo):
            img[iniY+j,iniX-j]=(0,0,255)            

def Gotham1(img):
    pintardiagonalIzqDer(img,655,10,90,4)
def Gotham2(img):
    pintardiagonalIzqDer(img,675,12,110,4)
def Gotham3(img):
    pintardiagonalIzqDer(img,702,10,137,4)
def Gotham4(img):
    pintardiagonalIzqDer(img,725,15,157,4)  
def Gotham5(img):
    pintardiagonalIzqDer(img,752,10,182,4) 
def Gotham6(img):
    pintardiagonalIzqDer(img,773,20,203,4)
    
def Acacia1(img):
    pintardiagonalIzqDer(img,688,15,60,4)
def Acacia2(img):
    pintardiagonalIzqDer(img,713,10,83,4)
def Acacia3(img):
    pintardiagonalIzqDer(img,735,10,105,4)
def Acacia4(img):
    pintardiagonalIzqDer(img,755,20,122,4)
def Acacia5(img):
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

def B11(img):
    pintardiagonalIzqDer(img,620,10,124,4) 
def B12(img):
    pintardiagonalIzqDer(img,651,10,134,4) 
def B13(img):
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
    
def SouthPark1(img):
    pintardiagonalDerIzq(img,635,10,185,6)
def SouthPark2(img):
    pintardiagonalDerIzq(img,663,15,158,6)
def SouthPark3(img):
    pintardiagonalDerIzq(img,690,15,133,6)
def SouthPark4(img):
    pintardiagonalDerIzq(img,720,20,103,6)  
def SouthPark5(img):
    pintardiagonalDerIzq(img,740,10,83,6)
def SouthPark6(img):
    pintardiagonalDerIzq(img,766,15,58,6)
def SouthPark7(img):
    pintardiagonalDerIzq(img,786,10,38,6)
def SouthPark8(img):
    pintarvertical(img,792,20,8,4)
    
def b21(img):
    pintardiagonalDerIzq(img,638,15,230,4)
def b22(img):
    pintardiagonalDerIzq(img,660,10,210,4)
def b23(img):
    pintardiagonalDerIzq(img,690,13,180,4)
def WallStreet1(img):
    pintarHorizontal(img,637,20,262,4)
def WallStreet2(img):
    pintarHorizontal(img,675,15,262,4)
def WallStreet3(img):
    pintarHorizontal(img,718,20,262,4)
def WallStreet4(img):
    pintarHorizontal(img,760,15,262,4)
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
def C1(img):
    pintardiagonalDerIzq(img,500,10,8,4)
def C2(img):
    pintardiagonalDerIzq(img,520,10,32,4)
def C3(img):
    pintardiagonalIzqDer(img,625,15,5,4)
def graficarSucre(img):
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




cargarGrafico()
        


