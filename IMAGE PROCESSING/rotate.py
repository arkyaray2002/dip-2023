import cv2

# Load the image
original_image = cv2.imread('apple.jpg')

# Check if the image was loaded successfully
if original_image is not None:
    # Rotate the image clockwise (90 degrees)
    clockwise_rotated = cv2.rotate(original_image, cv2.ROTATE_90_CLOCKWISE)
    # Rotate the image anti-clockwise (90 degrees)
    anticlockwise_rotated = cv2.rotate(original_image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display the original and rotated images
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Clockwise Rotated Image", clockwise_rotated)
    cv2.imshow("Anti-clockwise Rotated Image", anticlockwise_rotated)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load the image.")
