import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.jpg', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((2, 2), np.uint8)
dilation = cv2.dilate(mask, kernel)
erosion = cv2.erode(mask, kernel, iterations=1)

titles = ['image', 'mask', 'dilation', 'erosion']
images = [img, mask, dilation, erosion]  # Store the actual images here

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')  # Specify the color map
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
