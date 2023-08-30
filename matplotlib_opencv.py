import cv2
from matplotlib import pyplot as plt
img =cv2.imread('Lena.png')
cv2.imshow('image',img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)# This line displays the RGB image using Matplotlib. Since the image is now in RGB format, it should be displayed with the correct colors.
plt.imshow(img) #opencv reads the image in BGR format and matplotlib reads the image in RGB format
plt.xticks([]),plt.yticks([])#it remove or hide the x and y coordinates in the image
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()