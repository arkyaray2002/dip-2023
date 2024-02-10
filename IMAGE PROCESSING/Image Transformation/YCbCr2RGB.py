import cv2

# Load the YCbCr image
YCbCr_image = cv2.imread('YCbCr_image.jpg')

# Convert to BGR (RGB)
rgb_image = cv2.cvtColor(YCbCr_image, cv2.COLOR_YCrCb2BGR)

# Display original image
cv2.imshow('Original Image', YCbCr_image)

# Display the RGB image
cv2.imshow('RGB Image', rgb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

