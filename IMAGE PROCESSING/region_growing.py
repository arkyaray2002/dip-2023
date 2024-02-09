import cv2
import numpy as np

def region_grow(img, seed, thres):
    x, y = img.shape
    out_img = np.zeros_like(img)

    for i in range(x):
        for j in range(y):
            p = abs(seed - img[i][j])
            if p <= thres:
                out_img[i][j] = 255
            else:
                out_img[i][j] = 0

    cv2.imshow("Output Image", out_img)

# Read the image
img = cv2.imread("Taj.jpg", 0)

# Calculate the maximum and minimum pixel values in the image
max_value = img.max()
min_value = img.min()

# Display max and min pixel values
print("Max Pixel:", max_value)
print("Min Pixel:", min_value)

# Get seed and threshold values from user input
seed = int(input("Enter seed value: "))
thres = int(input("Enter threshold value: "))

# Perform region growing and display the result
region_grow(img, seed, thres)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
