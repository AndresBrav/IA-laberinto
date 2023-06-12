import cv2
from Casilla import *
lista=[]
sucre=Casilla('Sucre',50,1)
bascope=Casilla("Bascope",50,2)
Perez1=Casilla("Perez1",45,1)


def cargarGrafico(listaRecorrido):
    img=cv2.imread("IA proyecto/mapaIA5.jpg")
    lista=listaRecorrido
    dist=0
    tiempo=0
    try:
        if "Sucre" in lista:
                Sucre(img)
                dist=dist+sucre.getDistancia()
                tiempo=tiempo+sucre.getTRecorrido()

        if "Bascope" in lista:
             Bascope(img)
             dist=dist+bascope.getDistancia()
             tiempo=tiempo+bascope.getTRecorrido()
        if "Perez1" in lista:
             perez1(img)
             dist=dist+Perez1.getDistancia()
             tiempo=tiempo+Perez1.getTRecorrido()


    except Exception:
         print("problemassssssssssss")

    print(dist)
    print(tiempo)    
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""
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
    colombia1(img)
    colombia2(img)
    colombia3(img)
    colombia4(img)
    jordan1(img)
    jordan2(img)
    jordan3(img)
    jordan4(img)
    españa1(img)
    españa2(img)
    españa3(img)
    españa4(img)
    españa5(img)
    españa6(img)
    francia1(img)
    francia2(img)
    francia3(img)
    peru1(img)
    peru2(img)
    melgarejo1(img)
    melgarejo2(img)
    melgarejo3(img)
    portugal2(img)
    portugal1(img)
    brasil1(img)
    brasil2(img)
    jose1(img)
    jose2(img)
    jose3(img)
    jose4(img)
    italia1(img)
    italia2(img)


    santa(img)

    BGalindo1(img)
    BGalindo2(img)
    BGalindo3(img)
    BGalindo4(img)
    Suarez1(img)
    Suarez2(img)
    Suarez3(img)
    Suarez4(img)
    Bolivar1(img)
    Bolivar2(img)
    Bolivar3(img)
    Bolivar4(img)
    Polonia1(img)
    Polonia2(img)
    Polonia3(img)
    Polonia4(img)
    pinos1(img)
    pinos2(img)
    pinos3(img)
    nataniel1(img)
    nataniel2(img)
    nataniel3(img)
    aroma1(img)
    aroma2(img)
    aroma3(img)
    ayacucho1(img)
    ayacucho2(img)
    ayacucho3(img)
    """
    
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
#cargarGrafico()
        


