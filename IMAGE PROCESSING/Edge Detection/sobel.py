import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
img = cv2.imread('panda.png', 0)
cv2.imshow("Original Display", img)

# Apply Sobel kernels for horizontal and vertical gradients
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine horizontal and vertical gradients
sobel_image = cv2.magnitude(sobel_x, sobel_y)
sobel_image = np.uint8(sobel_image)

# Display the result
cv2.imshow("Sobel Operator Applied", sobel_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
