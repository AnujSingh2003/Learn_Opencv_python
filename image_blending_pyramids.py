import cv2
import numpy as np

apple = cv2.imread('apple.jpeg')
orange = cv2.imread('orange.png')

# Resize the images to the same dimensions
apple = cv2.resize(apple, (300, 300))
orange = cv2.resize(orange, (300, 300))

# Make sure both images have the same number of channels (3)
orange = orange[:, :, :3]


# Blending using Laplacian pyramid
def blend_images_pyramid(image1, image2, levels=5):
    # Generate Gaussian pyramid for both images
    gp_image1 = [image1]
    gp_image2 = [image2]

    for i in range(levels):
        image1 = cv2.pyrDown(image1)
        image2 = cv2.pyrDown(image2)
        gp_image1.append(image1)
        gp_image2.append(image2)

    # Generate Laplacian pyramid for both images
    lp_image1 = [gp_image1[levels - 1]]
    lp_image2 = [gp_image2[levels - 1]]

    for i in range(levels - 1, 0, -1):
        expanded_image1 = cv2.pyrUp(gp_image1[i])
        expanded_image2 = cv2.pyrUp(gp_image2[i])

        laplacian1 = cv2.subtract(gp_image1[i - 1],
                                  cv2.resize(expanded_image1, (gp_image1[i - 1].shape[1], gp_image1[i - 1].shape[0])))
        laplacian2 = cv2.subtract(gp_image2[i - 1],
                                  cv2.resize(expanded_image2, (gp_image2[i - 1].shape[1], gp_image2[i - 1].shape[0])))
        lp_image1.append(laplacian1)
        lp_image2.append(laplacian2)

    # Combine the left and right halves of Laplacian images
    blended_pyramid = []
    for lap1, lap2 in zip(lp_image1, lp_image2):
        cols, rows, ch = lap1.shape
        blended = np.hstack((lap1[:, :cols // 2], lap2[:, cols // 2:]))
        blended_pyramid.append(blended)

    # Reconstruction
    reconstructed = blended_pyramid[0]
    for i in range(1, levels):
        reconstructed = cv2.pyrUp(reconstructed)
        rows, cols, _ = blended_pyramid[i].shape
        reconstructed = cv2.add(reconstructed, blended_pyramid[i][:reconstructed.shape[0], :reconstructed.shape[1]])

    return reconstructed


# Blend images using the function
blended_image = blend_images_pyramid(apple, orange)

# Show the result
cv2.imshow("Blended Image", blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
