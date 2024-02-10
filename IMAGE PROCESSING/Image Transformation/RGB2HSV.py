import cv2

# Load the rgb image
rgb_image = cv2.imread('apple.jpg')

# Convert to hsv
hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)

# Display original image
cv2.imshow('Original Image', rgb_image)

# Display the binary image
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the binary image
cv2.imwrite("hsv_image.jpg", hsv_image)
