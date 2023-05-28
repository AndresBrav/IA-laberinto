import cv2

#Cargar Imagen
img= cv2.imread("IA proyecto/mapaIA.jpg")
    
#Cargar Imagen a escala de grises
img= cv2.imread("IA proyecto/mapaIA.jpg",cv2.IMREAD_GRAYSCALE)

#Guardar una Imagen
#cv2.imwrite('ia.png',img)

 #Mostrar La imagen, esperar tecla para cerrar y destruir ventanas
cv2.imshow('Imagen IA',img)
cv2.waitKey(0)
cv2.destroyAllWindows()