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

    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
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
        


