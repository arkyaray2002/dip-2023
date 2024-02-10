import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('rose.jpg')
h, w, c = img1.shape
img2 = cv2.imread('apple.jpg')
img2 = cv2.resize(img2, (w, h))

# Add images using cv2.add to handle saturation properly
new_img = cv2.add(img1, img2)

# Display original images and the result
imgs = np.hstack((img1, img2, new_img))
cv2.imshow('Original and Summed Images', imgs)

# Calculate and display histogram of the summed image
histr = cv2.calcHist([new_img], [0], None, [256], [0, 255])
plt.plot(histr)
plt.title('Histogram of Summed Image')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
