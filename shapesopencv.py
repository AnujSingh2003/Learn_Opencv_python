import cv2
import numpy as np
img1=np.zeros([512,512,3],np.uint8)
#img1=cv2.imread("D:\E-commerce website\images\\buy-1.jpg",1)#1 is used for rgb and 0 is used for grayscale image
img1=cv2.resize(img1,(980,700))
img1=cv2.line(img1,(0,0), (255,255),(0,0,255),2)
img1=cv2.arrowedLine(img1,(0,255), (255,255),(0,0,255),2)
img1=cv2.rectangle(img1, (384,0),(510,128),(0,0,255),5)#in place of thickness if you put -1 its will fill the reactange with given color
img1=cv2.circle(img1,(447,63), 63, (0,255,0),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
img1=cv2.putText(img1, 'opencv', (10,500),font , 4, (255,255,0),10,cv2.LINE_AA)
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()

