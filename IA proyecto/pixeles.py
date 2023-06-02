import cv2
import numpy as np
img=cv2.imread("IA proyecto/mapaIA1.jpg")
for i in range(4,15):
    img[2,i]=(0,0,255) 
    img[3,i]=(0,0,255)
    img[4,i]=(0,0,255)
    img[5,i]=(0,0,255)
    img[6,i]=(0,0,255)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
