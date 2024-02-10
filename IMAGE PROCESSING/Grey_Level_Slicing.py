import cv2
import matplotlib.pyplot as plt

# Read the image and resize it
i = cv2.imread('apple.jpg', 0)
i = cv2.resize(i, (300, 300))

# Create copies of the original image for processing
j = i.copy()
k = i.copy()  # Initialize k with a copy of i
row, col = i.shape

# Get user input for threshold values
T1 = int(input('Enter the Lowest threshold value:'))
T2 = int(input('Enter the Highest threshold value:'))

# Apply gray-level slicing without background
for x in range(1, row):
    for y in range(1, col):
        if (j[x][y] >= T1) and (j[x][y] <= T2):
            j[x][y] = i[x][y]
            k[x][y] = 255  # Set pixel to white for the selected range
        else:
            j[x][y] = 0
            k[x][y] = 0  # Set pixel to black for values outside the range

# Display the original image and its histogram
cv2.imshow('Original image', i)
histr = cv2.calcHist([i], [0], None, [256], [0, 255])
plt.plot(histr)
plt.title('Original Image Histogram')
plt.show()

# Display the processed image without background and its histogram
cv2.imshow('Graylevel slicing without background', k)
histr_k = cv2.calcHist([k], [0], None, [256], [0, 255])
plt.plot(histr_k)
plt.title('Processed Image Histogram')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
