import cv2
import numpy as np

# Read the grayscale image
img = cv2.imread("rose.jpg", 0)

# Calculate the maximum and minimum pixel values in the image
max_value = img.max()
min_value = img.min()

# Define a function for threshold segmentation
def threshold_segmentation(img, thres):
    x, y = img.shape
    out_img = np.zeros_like(img)

    for i in range(x):
        for j in range(y):
            if img[i][j] <= thres:
                out_img[i][j] = 255
            else:
                out_img[i][j] = 0

    cv2.imshow("Output Image", out_img)

# Display max and min pixel values
print("Max Pixel:", max_value)
print("Min Pixel:", min_value)

# Get threshold value from user input
thres = int(input("Enter threshold value: "))

# Perform threshold segmentation and display the result
threshold_segmentation(img, thres)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
