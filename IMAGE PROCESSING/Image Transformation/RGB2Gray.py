import cv2

# Load the RGB image
rgb_image = cv2.imread('apple.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

# show the grayscale image
cv2.imshow('gray_image.jpg', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the grayscale image
cv2.imwrite('gray_image.jpg', gray_image)