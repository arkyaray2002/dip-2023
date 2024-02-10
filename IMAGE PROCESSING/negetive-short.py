import cv2
import numpy as np

img = cv2.imread('apple.jpg')
neg = 255 - img
cv2.imshow('negetive', neg)

cv2.waitKey(0)