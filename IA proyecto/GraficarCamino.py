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

"""Seccion Loida"""
Bayern1=Casilla("Bayern1",100,2)

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


        """Seccion de Loida"""
        if "Bayern1" in lista:
            bayern1(img)
            dist=dist+Bayern1.getDistancia()
            tiempo=tiempo+Bayern1.getTRecorrido()
        



    except Exception:
         print("problemassssssssssss")

    print(dist)
    print(tiempo)
        
    """
   
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
    #empieza victor
   
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

    ciruelos(img)
    santiago1(img)
    santiago2(img)
    santiago3(img)
    santiago4(img)
    santiago5(img)
    paris1(img)
    paris2(img)
    paris3(img)

    calera1(img)
    calera2(img)
    calera3(img)
    calera4(img)

    pisiga1(img)
    pisiga2(img)
    pisiga3(img)
    pisiga4(img)
    pisiga5(img)

    santaRosa1(img)
    santaRosa2(img)
    santaRosa3(img)

    yumucu1(img)
    yumucu2(img)
    yumucu3(img)
    yumucu4(img)
    yumucu5(img)

    joya1(img)
    joya2(img)
    joya3(img)
    joya4(img)
    joya5(img)

    ballon1(img)
    ballon2(img)
    ballon3(img)
    ballon4(img)

    sanLuis1(img)
    sanLuis2(img)
    sanLuis3(img)

    lopez1(img)
    lopez2(img)
    lopez3(img)
    
    bruselas1(img)
    bruselas2(img)
    bruselas3(img)
    bruselas4(img)

    japon1(img)
    japon2(img)

    lima(img)

    paria1(img)
    paria2(img)
    paria3(img)
    paria4(img)
    paria5(img)

    guzman(img)

    pando1(img)
    pando2(img)
    pando3(img)
    pando4(img)

    inter1(img)
    inter2(img)
    inter3(img)
    inter4(img)
    inter5(img)

    vandiola1(img)
    vandiola2(img)
    vandiola3(img)
    vandiola4(img)
    vandiola5(img)

    lanza1(img)
    lanza2(img)

    torres(img)
    daza1(img)
    daza2(img)
    daza3(img)
    daza4(img)
    daza5(img)
    daza6(img)
    zaruma1(img)
    zaruma2(img)
    zaruma3(img)
    zaruma4(img)
    zaruma5(img)
    zaruma6(img)

    peñas1(img)
    peñas2(img)
    peñas3(img)
    peñas4(img)
    peñas5(img)
    peñas6(img)

    castrilla1(img)
    castrilla2(img)
    castrilla3(img)

    dulon1(img)
    dulon2(img)
    dulon3(img)
    dulon4(img)

    habana1(img)
    habana2(img)

    toledo1(img)
    toledo2(img)
    toledo3(img)
    toledo4(img)
    toledo5(img)
    toledo6(img)
    toledo7(img)

    hungria1(img)
    hungria2(img)
    hungria3(img)

    quito1(img)
    quito2(img)
    quito3(img)

    bayern1(img)
    bayern2(img)
    bayern3(img)
    bayern4(img)
    bayern5(img)
    bayern6(img)
    bayern7(img)
    bayern8(img)

    pocoata1(img)
    pocoata2(img)
    pocoata3(img)
    pocoata4(img)
    pocoata5(img)
    pocoata6(img)
    pocoata7(img)
    pocoata8(img)
    pocoata9(img)
    pocoata10(img)

    sanJuan1(img)
    sanJuan2(img)
    sanJuan3(img)
    sanJuan4(img)
    sanJuan5(img)
    sanJuan6(img)
    sanJuan7(img)
    sanJuan8(img)
    sanJuan9(img)
    sanJuan10(img)
    sanJuan11(img)
    sanJuan12(img)
    sanJuan13(img)

    alcala1(img)
    alcala2(img)
    alcala3(img)
    alcala4(img)
    alcala5(img)
    alcala6(img)
    alcala7(img)
    alcala8(img)
    alcala9(img)
    alcala10(img)
    alcala11(img)
    alcala12(img)

    guayacan1(img)
    guayacan2(img)
    guayacan3(img)
    guayacan4(img)
    guayacan5(img)
    guayacan6(img)
    guayacan7(img)
    guayacan8(img)
    guayacan9(img)

    tunari1(img)
    tunari2(img)
    tunari3(img)

    pool(img)
    AB23(img)
    C13(img)
    C14(img)
    C15(img)
    C16(img)
    C17(img)
    C18(img)
    RRivero1(img)
    RRivero2(img)
    RRivero3(img)
    RRivero4(img)
    RRivero5(img)
    RRivero6(img)
    RRivero7(img)
    RRivero8(img)
    springfield17(img)
    springfield18(img)
    springfield19(img)
    springfield20(img)
    springfield21(img)
    springfield22(img)
    springfield23(img)
    springfield24(img)
    springfield25(img)
    springfield26(img)
    springfield27(img)
    springfield28(img)
    springfield29(img)
    springfield30(img)
    springfield31(img)
    springfield32(img)
    springfield33(img)
    springfield34(img)

    america1(img)
    america2(img)
    america3(img)
    america4(img)
    america5(img)
    america6(img)

    C4(img)
    C5(img)
    C6(img)
    C7(img)

    heroinas1(img)
    heroinas2(img)
    heroinas3(img)
    heroinas4(img)
    heroinas5(img)
    heroinas6(img)
    heroinas7(img)
    heroinas8(img)
    heroinas9(img)
    heroinas10(img)
    heroinas11(img)

    lizarraga1(img)
    lizarraga2(img)
    lizarraga3(img)

    blink1(img)
    blink2(img)

    rasmus1(img)
    rasmus2(img)
    rasmus3(img)
    """
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
        


