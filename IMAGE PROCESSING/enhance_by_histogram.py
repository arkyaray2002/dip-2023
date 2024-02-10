import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
image = cv2.imread('apple.jpg', 0)
h, w = image.shape

# Padding the image
padding = np.zeros([h + 2, w + 2], int)
for i in range(1, h + 1):
    for j in range(1, w + 1):
        padding[i, j] = image[i - 1, j - 1]

# Define a 3x3 kernel
kernel = np.ones([3, 3], int)

# Create copies of the original image for different filters
median_img = image.copy()
max_img = image.copy()
min_img = image.copy()
mean_img = image.copy()

# Applying filters
for i in range(1, h + 1):
    for j in range(1, w + 1):
        kernel[0, 0] = padding[i - 1, j - 1]
        kernel[0, 1] = padding[i - 1, j]
        kernel[0, 2] = padding[i - 1, j + 1]
        kernel[1, 0] = padding[i, j - 1]
        kernel[1, 1] = padding[i, j]
        kernel[1, 2] = padding[i, j + 1]
        kernel[2, 0] = padding[i + 1, j - 1]
        kernel[2, 1] = padding[i + 1, j]
        kernel[2, 2] = padding[i + 1, j + 1]

        median = np.median(kernel)
        max_val = kernel.max()
        min_val = kernel.min()
        mean = kernel.mean()

        median_img[i - 1, j - 1] = median
        max_img[i - 1, j - 1] = max_val
        min_img[i - 1, j - 1] = min_val
        mean_img[i - 1, j - 1] = mean

# Display the results
images = np.hstack((image, median_img))
cv2.imshow("Before and after applying median filter", images)

images = np.hstack((image, max_img))
cv2.imshow("Before and after applying max filter", images)

images = np.hstack((image, min_img))
cv2.imshow("Before and after applying min filter", images)

images = np.hstack((image, mean_img))
cv2.imshow("Before and after applying mean filter", images)

# Weighted average filter
img = cv2.imread('Taj.jpg', 0)
cv2.imshow('Original image', img)

h, w = img.shape
new_img1 = img.copy()

mask = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]

for i in range(1, h - 1):
    for j in range(1, w - 1):
        temp = abs(img[i - 1][j - 1] * mask[0][0] + img[i - 1][j] * mask[0][1] + img[i - 1][j + 1] * mask[0][2] +
                   img[i][j - 1] * mask[1][0] + img[i][j] * mask[1][1] + img[i][j + 1] * mask[1][2] +
                   img[i + 1][j - 1] * mask[2][0] + img[i + 1][j] * mask[2][1] + img[i + 1][j + 1] * mask[2][2])
        new_img1[i][j] = (temp // 9)

cv2.imshow('Weighted average filter', new_img1)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
