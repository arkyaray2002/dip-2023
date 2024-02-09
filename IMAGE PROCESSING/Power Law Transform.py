import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('apple.jpg', 0)
height, width = img.shape[:2]
gamma = 1 / 0.25
c = 255

def evaluatePixel(pixel):
    global gamma, c
    return c * ((pixel / 255) ** gamma)

for i in range(height):
    for j in range(width):
        img.itemset((i, j), evaluatePixel(img.item(i, j)))

cv2.imshow('Power', img)

histogram = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.plot(histogram)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
