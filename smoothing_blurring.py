import cv2
import numpy as np
from matplotlib import pyplot as plt
# img=cv2.imread('opencv-logo.png')
# img=cv2.imread('water.png')
img=cv2.imread('Lena.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5) #use water image
bilateralFilter=cv2.bilateralFilter(img,9,75,75) #use lena image


titles=['image','2DConvulation','blur','gblur','medianblur','bilateralFilter']
images=[img,dst,blur,gblur,median,bilateralFilter]

for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()