import cv2

# Load the rgb image
rgb_image = cv2.imread('apple.jpg')

# Convert to YCbCr
YCbCr_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2YCrCb)

# Display original image
cv2.imshow('Original Image', rgb_image)

# Display the binary image
cv2.imshow('YCbCr Image', YCbCr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the binary image 
cv2.imwrite("YCbCr_image.jpg", YCbCr_image)
