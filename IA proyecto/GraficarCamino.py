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
    WallStreet5(img)
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
    Nogal1(img)
    Nogal2(img)
    Nogal3(img)
    Nogal4(img)
    C1(img)
    C2(img)
    C3(img)
    mar1(img)
    mar2(img)
    olmos1(img)
    olmos2(img)
    olmos3(img)
    olmos4(img)
    olmos5(img)
    siempreviva1(img)
    siempreviva2(img)
    siempreviva3(img)
    siempreviva4(img)
    metroville1(img)
    metroville2(img)
    coronado1(img)
    coronado2(img)
    coronado3(img)
    coronado4(img)
    coronado5(img)
    sol(img)
    salero1(img)
    salero2(img)
    salero3(img)
    nintendo1(img)
    nintendo2(img)
    nintendo3(img)
    abbeyroad1(img)
    abbeyroad2(img)
    abbeyroad3(img)
    abbeyroad4(img)
    abbeyroad5(img)
    abbeyroad6(img)
    abbeyroad7(img)
    elmwood21(img)
    elmwood22(img)
    elmwood23(img)
    elmwood24(img)
    peachtree1(img)
    peachtree2(img)
    peachtree3(img)
    peachtree4(img)
    peachtree5(img)
    peachtree6(img)
    peachtree7(img)
    luna(img)
    luz(img)
    d1(img)
    vida(img)
    nube1(img)
    nube2(img)
    alba(img)
    brisa1(img)
    brisa2(img)
    aroma1(img)
    aroma2(img)
    aroma3(img)
    aroma4(img)
    aroma5(img)
    aroma6(img)
    aroma7(img)
    aroma8(img)
    elmore1(img)
    elmore2(img)
    elmore3(img)
    elmore4(img)
    elmore5(img)
    elmore6(img)
    elmore7(img)
    elmore8(img)
    elmore9(img)
    elmore10(img)
    elmore11(img)
    springfield1(img)
    springfield2(img)
    springfield3(img)
    springfield4(img)
    springfield5(img)
    springfield6(img)
    springfield7(img)
    springfield8(img)
    springfield9(img)
    springfield10(img)
    springfield11(img)
    springfield12(img)
    springfield13(img)
    springfield14(img)
    springfield15(img)
    springfield16(img)
    millaverde1(img)
    millaverde2(img)
    millaverde3(img)
    millaverde4(img)
    millaverde5(img)
    millaverde6(img)
    millaverde7(img)
    millaverde8(img)
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
def WallStreet5(img):
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
    
def Nogal1(img):
    pintardiagonalIzqDer(img,577,12,162,4)
def Nogal2(img):
    pintardiagonalIzqDer(img,600,15,185,4)
def Nogal3(img):
    pintardiagonalIzqDer(img,627,12,210,4)
def Nogal4(img):
    pintardiagonalIzqDer(img,650,15,240,4)

def C1(img):
    pintardiagonalDerIzq(img,502,10,8,4)
def C2(img):
    pintardiagonalDerIzq(img,520,10,32,4)
def C3(img):
    pintardiagonalIzqDer(img,625,15,5,4)
def mar1(img):
    pintardiagonalIzqDer(img,433,15,106,4)
def mar2(img):
    pintardiagonalIzqDer(img,469,8,122,4)
    
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
    pintardiagonalIzqDer(img,672,25,207,6)
def elmore11(img):
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
        


