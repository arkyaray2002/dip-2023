import cv2

# Load the grayscale image
gray_image = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Convert to binary
threshold_value, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Display original image
cv2.imshow('Grey Image', gray_image)

# Display the binary image
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the binary image
cv2.imwrite("binary_image.jpg", binary_image)
