import cv2
import numpy as np
from matplotlib import pyplot as plt
img =cv2.imread('gradient.jpg',0)
_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,100,255,cv2.THRESH_TOZERO)

# using matplotlib
titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO']
images=[img,th1,th2,th3,th4]
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# ------ending matplolib---------


# cv2.imshow('image',img)
# cv2.imshow('th1',th1)
# cv2.imshow('th2',th2)
# cv2.imshow('th3',th3)
# cv2.imshow('th4',th4)
# cv2.waitKey(0)
# cv2.destroyAllWindows()