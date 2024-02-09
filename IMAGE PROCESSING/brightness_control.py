import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('apple.jpg')
cv2.imshow('Original image', img1)

# Enhance brightness
a_enhance = 2
b_enhance = 50
enhanced = cv2.addWeighted(img1, a_enhance, np.zeros(img1.shape, img1.dtype), 0, b_enhance)
cv2.imshow('Brightness Enhanced', enhanced)

# Plot histogram of the enhanced image
histr_enhanced = cv2.calcHist([enhanced], [0], None, [256], [0, 255])
plt.plot(histr_enhanced)

# Compress brightness
a_compress = 0.2
b_compress = 50
compressed = cv2.addWeighted(img1, a_compress, np.zeros(img1.shape, img1.dtype), 0, b_compress)
cv2.imshow('Brightness Compressed', compressed)

# Plot histogram of the compressed image
histr_compressed = cv2.calcHist([compressed], [0], None, [256], [0, 255])
plt.plot(histr_compressed)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
