import cv2

# Load the HSV image
hsv_image = cv2.imread('hsv_image.jpg')

# Convert to BGR (RGB)
rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Display original image
cv2.imshow('Original Image', hsv_image)

# Display the RGB image
cv2.imshow('RGB Image', rgb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

