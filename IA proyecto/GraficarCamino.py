import cv2
from Casilla import *

sucre=Casilla('Sucre',1,50,1)

def GraficarRecorrido(listaRecorrido):
    lista=[]
    lista=listaRecorrido
    print(lista[1],"ejemplo de que funciona")
    cargarGrafico()

def cargarGrafico():
    img=cv2.imread("IA proyecto/mapaIA1.jpg")

    graficarSucre(img)
    Bascope(img)

    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def graficarSucre(img):
    for i in range(11,23):
        img[45,i]=(0,0,255) 
        img[46,i]=(0,0,255)
        img[47,i]=(0,0,255)
        img[48,i]=(0,0,255)
        img[49,i]=(0,0,255)

def Bascope(img):
    for i in range(62,75):
        img[i,42]=(0,0,255) 
        img[i,43]=(0,0,255) 
        img[i,44]=(0,0,255)
        img[i,45]=(0,0,255)
        


