import cv2
import numpy as np

# Read the grayscale image
img = cv2.imread("rose.jpg", 0)

# Define a function for threshold segmentation
def threshold_segmentation(img, thres):
    x, y = img.shape

    for i in range(x):
        for j in range(y):
            if img[i][j] <= thres:
                img[i][j] = 255
            else:
                img[i][j] = 0

    cv2.imshow("Output Image", img)


# Get threshold value from user input
thres = 130

# Perform threshold segmentation and display the result
threshold_segmentation(img, thres)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
