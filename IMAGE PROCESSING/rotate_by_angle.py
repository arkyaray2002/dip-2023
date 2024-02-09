import cv2
import numpy as np

# Load the original image
original_image = cv2.imread('your_image.jpg')

# Rotate the image 45 degrees clockwise
rows, cols = original_image.shape[:2]
rotation_matrix_cw = cv2.getRotationMatrix2D((cols/2, rows/2), -45, 1)
rotated_image_cw = cv2.warpAffine(original_image, rotation_matrix_cw, (cols, rows))

# Rotate the image 45 degrees counterclockwise
rotation_matrix_ccw = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated_image_ccw = cv2.warpAffine(original_image, rotation_matrix_ccw, (cols, rows))

# Display the original image and its rotations
cv2.imshow('Original Image', original_image)
cv2.imshow('Rotated 45 Degrees Clockwise', rotated_image_cw)
cv2.imshow('Rotated 45 Degrees Counterclockwise', rotated_image_ccw)
cv2.waitKey(0)
cv2.destroyAllWindows()
