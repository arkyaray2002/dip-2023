import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('rose.jpg', 0)
img = cv2.resize(img, [300, 300])

cv2.imshow("Original Display", img)

mask1 = [[1, 0], [0, -1]]
mask2 = [[0, 1], [-1, 0]]

h, w = img.shape
img_new1 = np.zeros_like(img, dtype=np.float32)
img_new2 = np.zeros_like(img, dtype=np.float32)

# Sobel operation for horizontal gradient
for i in range(1, h - 1):
    for j in range(1, w - 1):
        temp = abs(img[i-1][j-1] * mask1[0][0] + img[i-1][j] * mask1[0][1] +
                   img[i][j-1] * mask1[1][0] + img[i][j] * mask1[1][1])
        img_new1[i][j] = temp

# Sobel operation for vertical gradient
for i in range(1, h - 1):
    for j in range(1, w - 1):
        temp = abs(img[i-1][j-1] * mask2[0][0] + img[i-1][j] * mask2[0][1] +
                   img[i][j-1] * mask2[1][0] + img[i][j] * mask2[1][1])
        img_new2[i][j] = temp

# Combine horizontal and vertical gradients
sobel_image = cv2.addWeighted(img_new1, 0.5, img_new2, 0.5, 0)

cv2.imshow("Sobel Operator Applied", sobel_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
