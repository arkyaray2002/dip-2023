import cv2
import numpy as np
import matplotlib.pyplot as plt

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

imgb = seperateChannel(just_blue, img.copy())
cv2.imshow('blue', imgb)
imgb = cv2.cvtColor(imgb, cv2.COLOR_BGR2GRAY)

imgg = seperateChannel(just_green, img.copy())
cv2.imshow('green', imgg)
imgg = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)

imgr = seperateChannel(just_red, img.copy())
cv2.imshow('red', imgr)
imgr = cv2.cvtColor(imgr, cv2.COLOR_BGR2GRAY)


# Add images using cv2.add to handle saturation properly
img2 = cv2.add(imgr, imgg)
new_img = cv2.add(img2, imgb)

# Display original images and the result
cv2.imshow('Original Image', img)
cv2.imshow('Summed Images', new_img)


# Calculate and display histogram of the summed image
histr = cv2.calcHist([new_img], [0], None, [256], [0, 255])
plt.plot(histr)
plt.title('Histogram of Summed Image')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
