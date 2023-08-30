import cv2
import numpy as np
img=cv2.imread('Lena.png',-1)
lr=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr)
hr2=cv2.pyrUp(lr2)
cv2.imshow('original image',img)
cv2.imshow('pyr down 1 image',lr)
cv2.imshow('pyr down 2 image',lr2)# its reducing the resolution of an image using pyrDown and once you reduce the resolution of that image it will lose the operation of that image and using pyrup it will show a blur image
cv2.imshow('pyr up 1 image',hr2)#you will not get the same result it will show blurred img
cv2.waitKey()
cv2.destroyAllWindows()




# image pyramid is of two type:
# 1)Guassian pyramid--repeat filtering and subsampling of an image
# 2)Laplacian pyramid