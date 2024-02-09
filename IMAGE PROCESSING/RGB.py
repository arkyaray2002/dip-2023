import cv2
import numpy as np

img = cv2.imread('rose.jpg')
h, w, ch = img.shape
print(ch)

just_blue = [1, 0, 0]
just_green = [0, 1, 0]
just_red = [0, 0, 1]

def seperateChannel(channel, img2):
    for i in range(h):
        for j in range(w):
            temp = img2[i][j]
            img2[i][j] = np.multiply(temp, channel)
    return img2

img2 = seperateChannel(just_blue, img.copy())
cv2.imshow('blue', img2)

img2 = seperateChannel(just_green, img.copy())
cv2.imshow('green', img2)

img2 = seperateChannel(just_red, img.copy())
cv2.imshow('red', img2)

cv2.waitKey(0)
