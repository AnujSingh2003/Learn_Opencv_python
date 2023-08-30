import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the grayscale image
img = cv2.imread("messi.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Laplacian edge detection
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)  # CV_64F is 64-bit float
lap_abs = np.uint8(np.absolute(lap))  # Convert Laplacian to uint8 for visualization

# Apply Sobel edge detection in both X and Y directions
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX_abs = np.uint8(np.absolute(sobelX))
sobelY_abs = np.uint8(np.absolute(sobelY))

# Titles and images for plotting
titles = ['Original Image', 'Laplacian', 'Sobel X', 'Sobel Y']
images = [img, lap_abs, sobelX_abs, sobelY_abs]

# Create subplots for the images
for i in range(4):
    plt.subplot(2, 2, i+1)  # 2 rows, 2 columns of subplots
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# Display the subplots
plt.show()
