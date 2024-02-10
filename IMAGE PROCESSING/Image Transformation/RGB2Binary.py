import cv2

# Load the rgb image
rgb_image = cv2.imread('apple.jpg')

# Load the rgb image
grey_image = cv2.imread('apple.jpg',0)

# Convert to binary
threshold_value, binary_image = cv2.threshold(grey_image, 128, 255, cv2.THRESH_BINARY)

# Display original image
cv2.imshow('Original Image', rgb_image)

# Display the binary image
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the binary image
cv2.imwrite("binary_image.jpg", binary_image)
