import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
img = cv2.imread('rose.jpg', 0)
cv2.imshow("Original Display", img)

# Define Prewitt masks
prewitt_mask_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_mask_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# Apply Prewitt masks for horizontal and vertical gradients
prewitt_x = cv2.filter2D(img, cv2.CV_64F, prewitt_mask_x)
prewitt_y = cv2.filter2D(img, cv2.CV_64F, prewitt_mask_y)

# Take the magnitude of the gradients
prewitt_image = cv2.magnitude(prewitt_x, prewitt_y)

# Normalize the result to fit within the 0-255 range
prewitt_image = cv2.normalize(prewitt_image, None, 0, 255, cv2.NORM_MINMAX)

# Convert to uint8
prewitt_image = np.uint8(prewitt_image)

# Display the result
cv2.imshow("Prewitt Operator Applied", prewitt_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
