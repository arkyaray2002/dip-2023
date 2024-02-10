import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the first image
img1 = cv2.imread('apple.jpg')

# Get dimensions of the first image
h, w, c = img1.shape

# Read the second image
img2 = cv2.imread('rose.jpg')

# Resize the second image to match the dimensions of the first image
img2 = cv2.resize(img2, (w, h))

# Ensure that img2 is not zero before performing division
img2[img2 == 0] = 1  # Avoid division by zero, set zero values to 1

# Perform element-wise division of the pixel values of the two images
new_img = img1 // img2

# Concatenate the original image, second image, and the divided image horizontally
imgs = np.hstack((img1, img2, new_img))

# Calculate and plot the histogram of the divided image
histr = cv2.calcHist([new_img], [0], None, [256], [0, 255])
plt.plot(histr)
plt.show()

# Display the concatenated image and wait for a key press
cv2.imshow('div', imgs)
cv2.waitKey(0)
