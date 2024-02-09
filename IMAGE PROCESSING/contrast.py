import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('apple.jpg')
cv2.imshow('Original image', img1)

# Contrast enhancement parameters
a1 = 1.5
a2 = 0
b = 50

# Perform contrast enhancement
enhanced = cv2.addWeighted(img1, a1, np.zeros(img1.shape, img1.dtype), a2, b)
cv2.imshow('Contrast Enhanced', enhanced)

# Plot histogram of the enhanced image
histr_enhanced = cv2.calcHist([enhanced], [0], None, [256], [0, 255])
plt.plot(histr_enhanced)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
