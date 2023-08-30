# laplacian and guassian pyramid helps us to blend the images and the reconstruction of the image

import cv2
import numpy as np
img=cv2.imread("Lena.png",-1)
layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)
layer=gp[5]
cv2.imshow('upper level guassian pyramid',layer)
lapyr=[layer]
for i in range(5,0,-1):
    guassian_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],guassian_extended)
    cv2.imshow(str(i),laplacian)
cv2.imshow("Original Image",img)
cv2.waitKey()
cv2.destroyAllWindows()